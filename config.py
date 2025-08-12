import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Configuration class for the application"""
    
    # LangExtract API configuration
    LANGEXTRACT_API_KEY = os.getenv("LANGEXTRACT_API_KEY", "")
    
    # Model configuration
    MODEL_ID = "gemini-2.5-pro"
    
    # File paths
    OUTPUT_FILENAME = "extraction_results.jsonl"
    
    @classmethod
    def validate_api_key(cls):
        """Validate that the API key is available"""
        if not cls.LANGEXTRACT_API_KEY:
            print("Warning: LANGEXTRACT_API_KEY not found in environment variables")
            print("Please set LANGEXTRACT_API_KEY in your .env file")
            return False
        else:
            print(f"API Key loaded successfully: {cls.LANGEXTRACT_API_KEY[:10]}...")
            return True
