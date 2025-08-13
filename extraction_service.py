import langextract as lx
import json
import os
from config import Config

class ExtractionService:
    """Service class for handling text extraction operations"""
    
    def __init__(self):
        self.config = Config
    
    def extract_entities(self, input_text, examples_type="medical", model_id=None):
        """Extract entities from input text using LangExtract"""
        if not self.config.LANGEXTRACT_API_KEY:
            raise ValueError("API key not configured. Please check your .env file.")
        
        # Use provided model_id or fall back to config default
        model_to_use = model_id if model_id else self.config.MODEL_ID
        
        print(f"Processing text with {len(input_text)} characters...")
        print(f"Using examples type: {examples_type}")
        print(f"Using model: {model_to_use}")
        
        # Import here to avoid circular imports
        from prompt_instructions import PromptInstructions
        from report_examples import ReportExamples
        
        # Always use general prompt
        prompt = PromptInstructions.get_general_prompt()
        
        # Select examples based on type
        if examples_type == "financial":
            examples = ReportExamples.get_financial_examples()
        elif examples_type == "legal":
            examples = ReportExamples.get_legal_examples()
        else:  # default to medical
            examples = ReportExamples.get_medical_examples()
        
        result = lx.extract(
            text_or_documents=input_text,
            prompt_description=prompt,
            examples=examples,
            model_id=model_to_use,
            api_key=self.config.LANGEXTRACT_API_KEY,
        )
        
        print(f"Extraction completed successfully. Result type: {type(result)}")
        return result
    
    def save_results(self, result):
        """Save extraction results to file"""
        try:
            lx.io.save_annotated_documents(
                [result], 
                output_name=self.config.OUTPUT_FILENAME, 
                output_dir="."
            )
            print(f"Results saved to {self.config.OUTPUT_FILENAME}")
            return True
        except Exception as save_error:
            print(f"Warning: Could not save results to file: {save_error}")
            return False
    
    def serialize_extractions(self, result):
        """Convert extraction results to JSON-serializable format"""
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
            
            return extractions, extractions_count
            
        except Exception as convert_error:
            print(f"Error converting result: {convert_error}")
            return [], 0
    
    def load_saved_results(self):
        """Load the most recently saved extraction results"""
        try:
            if not os.path.exists(self.config.OUTPUT_FILENAME):
                return None, "No saved results found"
            
            # Read the last line from the JSONL file (most recent result)
            with open(self.config.OUTPUT_FILENAME, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                if not lines:
                    return None, "No results in file"
                
                # Get the last line (most recent result)
                last_line = lines[-1].strip()
                if last_line:
                    result_data = json.loads(last_line)
                    return result_data, "Loaded from saved results"
                else:
                    return None, "Empty result file"
                    
        except Exception as e:
            return None, f"Error reading saved results: {str(e)}"
