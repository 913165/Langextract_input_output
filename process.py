import textwrap
import langextract as lx

import os


LANGEXTRACT_API_KEY = os.getenv("LANGEXTRACT_API_KEY")


prompt = textwrap.dedent("""\
Extract financial entities, sentiments, and relationships in order of appearance.
Use exact text for extractions. Do not paraphrase or overlap entities.
Provide meaningful attributes for each entity to add context.""")


examples = [
    lx.data.ExampleData(
        text=(
            "JPMorgan Chase announces a strong quarter, beating analyst expectations."
        ),
        extractions=[
            lx.data.Extraction(
                extraction_class="financial_entity",
                extraction_text="JPMorgan Chase",
                attributes={"type": "bank"},
            ),
            lx.data.Extraction(
                extraction_class="sentiment",
                extraction_text="strong quarter",
                attributes={"direction": "positive"},
            ),
            lx.data.Extraction(
                extraction_class="relationship",
                extraction_text="beating analyst expectations",
                attributes={"context": "performance metric"},
            ),
        ],
    )
]

input_text = (
    "Tesla stock plummets after a negative earnings report, impacting the Nasdaq index."
)
result = lx.extract(
    text_or_documents=input_text,
    prompt_description=prompt,
    examples=examples,
    model_id="gemini-2.5-pro",
    api_key=LANGEXTRACT_API_KEY,
)

lx.io.save_annotated_documents([result], output_name="extraction_results_finance.jsonl")

# Generate the interactive visualization from the file
html_content = lx.visualize("test_output/extraction_results_finance.jsonl")
with open("visualization_finance.html", "w", encoding="utf-8") as f:
    f.write(html_content)
