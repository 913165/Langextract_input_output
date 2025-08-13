# This file is maintained for backward compatibility
# New implementations should use prompt_instructions.py and report_examples.py directly

from prompt_instructions import PromptInstructions
from report_examples import ReportExamples

class ExtractionPrompts:
    """Class containing extraction prompts and examples - maintained for backward compatibility"""
    
    @staticmethod
    def get_general_prompt():
        """Get the general entity extraction prompt"""
        return PromptInstructions.get_general_prompt()
    
    @staticmethod
    def get_medical_examples():
        """Get medical entity extraction examples"""
        return ReportExamples.get_medical_examples()
    
    @staticmethod
    def get_financial_examples():
        """Get financial entity extraction examples"""
        return ReportExamples.get_financial_examples()
    
    @staticmethod
    def get_legal_examples():
        """Get legal entity extraction examples"""
        return ReportExamples.get_legal_examples()