import os
from dotenv import load_dotenv

# Load environment variables from .env file BEFORE importing langextract
load_dotenv()

# Set the API key as an environment variable
os.environ["LANGEXTRACT_API_KEY"] = os.getenv("LANGEXTRACT_API_KEY", "")

from flask import Flask, request, jsonify, send_from_directory, render_template
import langextract as lx
import textwrap

app = Flask(__name__, static_folder="static", template_folder="templates")

LANGEXTRACT_API_KEY = os.getenv("LANGEXTRACT_API_KEY")

# Check if API key is available
if not LANGEXTRACT_API_KEY:
    print("Warning: LANGEXTRACT_API_KEY not found in environment variables")
    print("Please set LANGEXTRACT_API_KEY in your .env file")
else:
    print(f"API Key loaded successfully: {LANGEXTRACT_API_KEY[:10]}...")

prompt = textwrap.dedent("""
Extract medical entities, events, and relationships from adverse event reports.
Use exact text for extractions. Do not paraphrase or overlap entities.
Provide meaningful attributes for each entity to add context.
Focus on identifying: report types, patient demographics, drugs, events, actions, outcomes, and conclusions.
""")

examples = [
    lx.data.ExampleData(
        text=(
            "REPORT TYPE: Adverse Event\n"
            "PATIENT: 54-year-old female\n"
            "DRUG: Drug LMN\n"
            "EVENT: Severe rash and pruritus after 3 days of therapy.\n"
            "ACTIONS: Drug discontinued, antihistamines administered.\n"
            "OUTCOME: Rash resolved within 5 days.\n"
            "CONCLUSIONS: Likely drug-induced hypersensitivity reaction."
        ),
        extractions=[
            lx.data.Extraction(
                extraction_class="report_type",
                extraction_text="Adverse Event",
                attributes={"category": "safety_report"},
            ),
            lx.data.Extraction(
                extraction_class="patient",
                extraction_text="54-year-old female",
                attributes={"age": "54", "gender": "female"},
            ),
            lx.data.Extraction(
                extraction_class="drug",
                extraction_text="Drug LMN",
                attributes={"type": "medication"},
            ),
            lx.data.Extraction(
                extraction_class="event",
                extraction_text="Severe rash and pruritus after 3 days of therapy",
                attributes={"severity": "severe", "timing": "3 days"},
            ),
            lx.data.Extraction(
                extraction_class="actions",
                extraction_text="Drug discontinued, antihistamines administered",
                attributes={"intervention": "drug_discontinuation", "treatment": "antihistamines"},
            ),
            lx.data.Extraction(
                extraction_class="outcome",
                extraction_text="Rash resolved within 5 days",
                attributes={"resolution": "resolved", "duration": "5 days"},
            ),
            lx.data.Extraction(
                extraction_class="conclusions",
                extraction_text="Likely drug-induced hypersensitivity reaction",
                attributes={"assessment": "probable", "mechanism": "hypersensitivity"},
            ),
        ],
    )
]

@app.route("/")
def index():
    return send_from_directory("templates", "index.html")

@app.route("/static/<path:path>")
def send_static(path):
    return send_from_directory("static", path)

@app.route("/saved_results")
def get_saved_results():
    """Get the most recently saved extraction results"""
    try:
        import json
        output_filename = "extraction_results.jsonl"
        
        if not os.path.exists(output_filename):
            return jsonify({"error": "No saved results found"}), 404
        
        # Read the last line from the JSONL file (most recent result)
        with open(output_filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            if not lines:
                return jsonify({"error": "No results in file"}), 404
            
            # Get the last line (most recent result)
            last_line = lines[-1].strip()
            if last_line:
                result_data = json.loads(last_line)
                return jsonify({
                    "result": result_data,
                    "message": "Loaded from saved results",
                    "extractions_count": len(result_data.get("extractions", []))
                })
            else:
                return jsonify({"error": "Empty result file"}), 404
                
    except Exception as e:
        return jsonify({"error": f"Error reading saved results: {str(e)}"}), 500

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    input_text = data.get("text", "")
    if not input_text:
        return jsonify({"error": "No input text provided."}), 400
    
    if not LANGEXTRACT_API_KEY:
        return jsonify({"error": "API key not configured. Please check your .env file."}), 500
    
    try:
        print(f"Processing text with {len(input_text)} characters...")
        
        result = lx.extract(
            text_or_documents=input_text,
            prompt_description=prompt,
            examples=examples,
            model_id="gemini-2.5-pro",
            api_key=LANGEXTRACT_API_KEY,
        )
        
        print(f"Extraction completed successfully. Result type: {type(result)}")
        
        # Save the results to a file
        output_filename = "extraction_results.jsonl"
        try:
            lx.io.save_annotated_documents([result], output_name=output_filename, output_dir=".")
            print(f"Results saved to {output_filename}")
        except Exception as save_error:
            print(f"Warning: Could not save results to file: {save_error}")
        
        # Extract only the essential data that can be serialized
        try:
            extractions = []
            if hasattr(result, 'extractions'):
                for extraction in result.extractions:
                    extraction_data = {
                        'extraction_class': extraction.extraction_class,
                        'extraction_text': extraction.extraction_text,
                        'attributes': {}
                    }
                    
                    # Safely extract attributes
                    if hasattr(extraction, 'attributes') and extraction.attributes:
                        for key, value in extraction.attributes.items():
                            # Convert any non-serializable objects to strings
                            if isinstance(value, (str, int, float, bool)) or value is None:
                                extraction_data['attributes'][key] = value
                            else:
                                extraction_data['attributes'][key] = str(value)
                    
                    extractions.append(extraction_data)
            
            extractions_count = len(extractions)
            print(f"Found {extractions_count} extractions")
            
        except Exception as convert_error:
            print(f"Error converting result: {convert_error}")
            extractions = []
            extractions_count = 0
        
        # Return the serializable results for the UI
        return jsonify({
            "result": {"extractions": extractions},
            "message": f"Extraction completed and saved to {output_filename}",
            "extractions_count": extractions_count
        })
            
    except Exception as e:
        print(f"Error during extraction: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({"error": f"Extraction failed: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)

