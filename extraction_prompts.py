import langextract as lx
import textwrap

class ExtractionPrompts:
    """Class containing extraction prompts and examples"""
    
    @staticmethod
    def get_medical_prompt():
        """Get the medical entity extraction prompt"""
        return textwrap.dedent("""
        Extract medical entities, events, and relationships from adverse event reports.
        Use exact text for extractions. Do not paraphrase or overlap entities.
        Provide meaningful attributes for each entity to add context.
        Focus on identifying: report types, patient demographics, drugs, events, actions, outcomes, and conclusions.
        """)
    
    @staticmethod
    def get_medical_examples():
        """Get medical entity extraction examples"""
        return [
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
