import os
from dotenv import load_dotenv

# Load environment variables from .env file BEFORE importing langextract
load_dotenv()

# Set the API key as an environment variable
os.environ["LANGEXTRACT_API_KEY"] = os.getenv("LANGEXTRACT_API_KEY", "")

from flask import Flask, request, jsonify, render_template
import traceback

# Import our refactored modules
from config import Config
from extraction_service import ExtractionService

# Initialize Flask app
app = Flask(__name__, static_folder="static", template_folder="templates")

# Initialize services
extraction_service = ExtractionService()

# Validate configuration on startup
Config.validate_api_key()

@app.route("/")
def index():
    """Serve the main application page"""
    return render_template("index.html")

@app.route("/static/<path:path>")
def send_static(path):
    """Serve static files"""
    return send_from_directory("static", path)

@app.route("/saved_results")
def get_saved_results():
    """Get the most recently saved extraction results"""
    try:
        result_data, message = extraction_service.load_saved_results()
        
        if result_data is None:
            return jsonify({"error": message}), 404
        
        return jsonify({
            "result": result_data,
            "message": message,
            "extractions_count": len(result_data.get("extractions", []))
        })
        
    except Exception as e:
        return jsonify({"error": f"Error reading saved results: {str(e)}"}), 500

@app.route("/predict", methods=["POST"])
def predict():
    """Process text and extract entities"""
    try:
        # Get input data
        data = request.get_json()
        input_text = data.get("text", "")
        examples_type = data.get("examples_type", "medical")
        model_id = data.get("model_id", "gemini-2.5-pro")  # Default to current config model
        
        if not input_text:
            return jsonify({"error": "No input text provided."}), 400
        
        print(f"Processing with model: {model_id}")
        
        # Extract entities with selected examples type and model
        result = extraction_service.extract_entities(
            input_text, 
            examples_type=examples_type,
            model_id=model_id
        )
        
        # Save results
        extraction_service.save_results(result)
        
        # Serialize results for JSON response
        extractions, extractions_count = extraction_service.serialize_extractions(result)
        
        # Return response
        return jsonify({
            "result": {"extractions": extractions},
            "message": f"Extraction completed and saved to {Config.OUTPUT_FILENAME}",
            "extractions_count": extractions_count,
            "examples_type": examples_type,
            "model_used": model_id
        })
            
    except ValueError as e:
        # API key or configuration errors
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        # Unexpected errors
        print(f"Error during extraction: {str(e)}")
        traceback.print_exc()
        return jsonify({"error": f"Extraction failed: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)

