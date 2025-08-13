"""Example pharmaceutical reports for training the structuring model.

This module contains curated examples of pharmaceutical reports with their
corresponding structured extractions. These examples are used for few-shot
learning with PharmExtract to train the model on proper categorization of
report sections into header, analysis, recommendations, and regulatory footer
components with appropriate clinical significance and regulatory impact labels.

The examples cover various pharmaceutical document types including clinical
trial reports, drug safety assessments, pharmacovigilance reports, regulatory
submissions, and pharmacokinetic studies across different therapeutic areas.
"""

import textwrap
from enum import Enum

import langextract as lx


class PharmSectionType(Enum):
    HEADER = "report_header"
    ANALYSIS = "analysis_body"
    RECOMMENDATIONS = "recommendations_section"
    FOOTER = "regulatory_footer"


def get_examples_for_model() -> list[lx.data.ExampleData]:
    """Examples that structure pharmaceutical reports into semantic sections.

    Returns:
        List of ExampleData objects containing pharmaceutical report examples
        with their corresponding structured extractions for training
        the language model.
    """
    return [
        lx.data.ExampleData(
            text=textwrap.dedent(
                """\
                PROTOCOL NUMBER: ONCO-2024-157
                STUDY TITLE: Phase III Randomized Trial of Novel Oncology Agent XK-429
                PRINCIPAL INVESTIGATOR: Dr. Sarah Chen, MD, PhD
                REGULATORY STATUS: FDA IND 123456, EMA CTA 2024-001234-15
                IRB APPROVAL: Western University IRB #2024-0892, Approved March 15, 2024

                EFFICACY ANALYSIS:
                The primary endpoint of overall survival was met with statistical significance (HR=0.68, 95% CI: 0.52-0.89, p=0.005). Median overall survival was 24.3 months in the treatment arm versus 16.8 months in the control arm.

                Secondary endpoints showed progression-free survival of 12.1 months versus 7.4 months (HR=0.61, p<0.001).

                SAFETY PROFILE:
                Treatment-emergent adverse events occurred in 94% of patients. Grade 3-4 adverse events were reported in 42% of treatment group versus 31% in control group.

                DOSING RECOMMENDATIONS:
                Recommended Phase III dose is 200mg twice daily with food. Dose reduction to 150mg twice daily for Grade 2 toxicities.

                REGULATORY COMPLIANCE:
                This study was conducted in accordance with GCP guidelines and FDA 21 CFR Part 312.
                """
            ).rstrip(),
            extractions=[
                lx.data.Extraction(
                    extraction_text="PROTOCOL NUMBER: ONCO-2024-157",
                    extraction_class="report_header",
                    attributes={
                        "section": "Protocol Summary",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="STUDY TITLE: Phase III Randomized Trial of Novel Oncology Agent XK-429",
                    extraction_class="report_header",
                    attributes={
                        "section": "Protocol Summary",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="PRINCIPAL INVESTIGATOR: Dr. Sarah Chen, MD, PhD",
                    extraction_class="report_header",
                    attributes={
                        "section": "Investigator Information",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="REGULATORY STATUS: FDA IND 123456, EMA CTA 2024-001234-15",
                    extraction_class="report_header",
                    attributes={
                        "section": "Regulatory Status",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="IRB APPROVAL: Western University IRB #2024-0892, Approved March 15, 2024",
                    extraction_class="report_header",
                    attributes={
                        "section": "Approval Information",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="The primary endpoint of overall survival was met with statistical significance (HR=0.68, 95% CI: 0.52-0.89, p=0.005).",
                    extraction_class="analysis_body",
                    attributes={
                        "section": "Efficacy Analysis",
                        "clinical_significance": "significant",
                        "regulatory_impact": "high",
                        "evidence_quality": "strong",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="Median overall survival was 24.3 months in the treatment arm versus 16.8 months in the control arm.",
                    extraction_class="analysis_body",
                    attributes={
                        "section": "Efficacy Analysis",
                        "clinical_significance": "significant",
                        "regulatory_impact": "high",
                        "evidence_quality": "strong",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="Secondary endpoints showed progression-free survival of 12.1 months versus 7.4 months (HR=0.61, p<0.001).",
                    extraction_class="analysis_body",
                    attributes={
                        "section": "Efficacy Analysis",
                        "clinical_significance": "significant",
                        "regulatory_impact": "medium",
                        "evidence_quality": "strong",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="Treatment-emergent adverse events occurred in 94% of patients.",
                    extraction_class="analysis_body",
                    attributes={
                        "section": "Safety Profile",
                        "clinical_significance": "significant",
                        "regulatory_impact": "medium",
                        "safety_level": "caution",
                        "evidence_quality": "strong",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="Grade 3-4 adverse events were reported in 42% of treatment group versus 31% in control group.",
                    extraction_class="analysis_body",
                    attributes={
                        "section": "Safety Profile",
                        "clinical_significance": "significant",
                        "regulatory_impact": "high",
                        "safety_level": "warning",
                        "evidence_quality": "strong",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="Recommended Phase III dose is 200mg twice daily with food.",
                    extraction_class="recommendations_section",
                    attributes={
                        "section": "Dosing",
                        "safety_level": "routine",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="Dose reduction to 150mg twice daily for Grade 2 toxicities.",
                    extraction_class="recommendations_section",
                    attributes={
                        "section": "Dosing",
                        "safety_level": "caution",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="This study was conducted in accordance with GCP guidelines and FDA 21 CFR Part 312.",
                    extraction_class="regulatory_footer",
                    attributes={},
                ),
            ],
        ),
        lx.data.ExampleData(
            text=textwrap.dedent(
                """\
                STUDY ID: CV-STATIN-2024
                COMPOUND: Atorvastatin 40mg
                INDICATION: Cardiovascular disease prevention
                STUDY DESIGN: Randomized, double-blind, placebo-controlled

                PHARMACOKINETIC PARAMETERS:
                Cmax was 42.3 ± 8.7 ng/mL achieved at Tmax of 2.1 ± 0.8 hours. Half-life was determined to be 14.2 ± 3.1 hours.

                AUC0-∞ was 287 ± 62 ng⋅hr/mL with apparent clearance of 139 ± 31 L/hr.

                EFFICACY ENDPOINTS:
                LDL cholesterol reduction was 48% from baseline (p<0.001). HDL cholesterol increased by 12% (p=0.023).

                CARDIOVASCULAR OUTCOMES:
                Primary composite endpoint was reduced by 22% (HR=0.78, 95% CI: 0.65-0.94, p=0.009).

                ADVERSE EVENTS:
                Myalgia was reported in 8.2% of patients. Liver enzyme elevation >3x ULN occurred in 1.1% of patients.

                CONTRAINDICATIONS:
                Active liver disease or unexplained persistent liver enzyme elevations.

                FDA APPROVAL STATUS: NDA 20-702, Approved December 17, 1996
                """
            ).rstrip(),
            extractions=[
                lx.data.Extraction(
                    extraction_text="STUDY ID: CV-STATIN-2024",
                    extraction_class="report_header",
                    attributes={
                        "section": "Protocol Summary",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="COMPOUND: Atorvastatin 40mg",
                    extraction_class="report_header",
                    attributes={
                        "section": "Protocol Summary",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="INDICATION: Cardiovascular disease prevention",
                    extraction_class="report_header",
                    attributes={
                        "section": "Protocol Summary",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="STUDY DESIGN: Randomized, double-blind, placebo-controlled",
                    extraction_class="report_header",
                    attributes={
                        "section": "Study Design",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="Cmax was 42.3 ± 8.7 ng/mL achieved at Tmax of 2.1 ± 0.8 hours.",
                    extraction_class="analysis_body",
                    attributes={
                        "section": "Pharmacokinetics",
                        "clinical_significance": "normal",
                        "regulatory_impact": "medium",
                        "evidence_quality": "strong",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="Half-life was determined to be 14.2 ± 3.1 hours.",
                    extraction_class="analysis_body",
                    attributes={
                        "section": "Pharmacokinetics",
                        "clinical_significance": "normal",
                        "regulatory_impact": "medium",
                        "evidence_quality": "strong",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="AUC0-∞ was 287 ± 62 ng⋅hr/mL with apparent clearance of 139 ± 31 L/hr.",
                    extraction_class="analysis_body",
                    attributes={
                        "section": "Pharmacokinetics",
                        "clinical_significance": "normal",
                        "regulatory_impact": "medium",
                        "evidence_quality": "strong",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="LDL cholesterol reduction was 48% from baseline (p<0.001).",
                    extraction_class="analysis_body",
                    attributes={
                        "section": "Efficacy Analysis",
                        "clinical_significance": "significant",
                        "regulatory_impact": "high",
                        "evidence_quality": "strong",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="HDL cholesterol increased by 12% (p=0.023).",
                    extraction_class="analysis_body",
                    attributes={
                        "section": "Efficacy Analysis",
                        "clinical_significance": "minor",
                        "regulatory_impact": "medium",
                        "evidence_quality": "moderate",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="Primary composite endpoint was reduced by 22% (HR=0.78, 95% CI: 0.65-0.94, p=0.009).",
                    extraction_class="analysis_body",
                    attributes={
                        "section": "Cardiovascular Outcomes",
                        "clinical_significance": "significant",
                        "regulatory_impact": "critical",
                        "evidence_quality": "strong",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="Myalgia was reported in 8.2% of patients.",
                    extraction_class="analysis_body",
                    attributes={
                        "section": "Adverse Events",
                        "clinical_significance": "minor",
                        "regulatory_impact": "medium",
                        "safety_level": "caution",
                        "evidence_quality": "strong",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="Liver enzyme elevation >3x ULN occurred in 1.1% of patients.",
                    extraction_class="analysis_body",
                    attributes={
                        "section": "Adverse Events",
                        "clinical_significance": "significant",
                        "regulatory_impact": "high",
                        "safety_level": "warning",
                        "evidence_quality": "strong",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="Active liver disease or unexplained persistent liver enzyme elevations.",
                    extraction_class="recommendations_section",
                    attributes={
                        "section": "Contraindications",
                        "safety_level": "contraindication",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="FDA APPROVAL STATUS: NDA 20-702, Approved December 17, 1996",
                    extraction_class="regulatory_footer",
                    attributes={},
                ),
            ],
        ),
        lx.data.ExampleData(
            text=textwrap.dedent(
                """\
                PROTOCOL: PSYCH-ANX-2024-089
                INVESTIGATIONAL PRODUCT: Anxiolytic Compound ZY-334
                THERAPEUTIC AREA: Generalized Anxiety Disorder
                PHASE: Phase II, multicenter study

                HAMILTON ANXIETY RATING SCALE:
                Mean HAM-A score reduction was 12.4 points from baseline (SD=4.2, p<0.001) in the treatment group versus 3.8 points in placebo group.

                CLINICAL GLOBAL IMPRESSION:
                CGI-I scores showed 68% of patients with much improved or very much improved ratings.

                PHARMACOKINETIC ANALYSIS:
                Steady-state concentrations achieved by day 7. No accumulation observed with twice-daily dosing.

                COGNITIVE FUNCTION:
                No significant impairment in cognitive testing batteries compared to placebo.

                WITHDRAWAL SYMPTOMS:
                Discontinuation syndrome was minimal with gradual taper protocol.

                DOSING GUIDANCE:
                Initiate at 5mg twice daily, titrate to 10mg twice daily based on response and tolerability.

                REGULATORY SUBMISSION: FDA Pre-IND meeting scheduled for Q2 2024
                """
            ).rstrip(),
            extractions=[
                lx.data.Extraction(
                    extraction_text="PROTOCOL: PSYCH-ANX-2024-089",
                    extraction_class="report_header",
                    attributes={
                        "section": "Protocol Summary",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="INVESTIGATIONAL PRODUCT: Anxiolytic Compound ZY-334",
                    extraction_class="report_header",
                    attributes={
                        "section": "Protocol Summary",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="THERAPEUTIC AREA: Generalized Anxiety Disorder",
                    extraction_class="report_header",
                    attributes={
                        "section": "Protocol Summary",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="PHASE: Phase II, multicenter study",
                    extraction_class="report_header",
                    attributes={
                        "section": "Study Design",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="Mean HAM-A score reduction was 12.4 points from baseline (SD=4.2, p<0.001) in the treatment group versus 3.8 points in placebo group.",
                    extraction_class="analysis_body",
                    attributes={
                        "section": "Efficacy Analysis",
                        "clinical_significance": "significant",
                        "regulatory_impact": "high",
                        "evidence_quality": "strong",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="CGI-I scores showed 68% of patients with much improved or very much improved ratings.",
                    extraction_class="analysis_body",
                    attributes={
                        "section": "Clinical Global Impression",
                        "clinical_significance": "significant",
                        "regulatory_impact": "high",
                        "evidence_quality": "strong",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="Steady-state concentrations achieved by day 7.",
                    extraction_class="analysis_body",
                    attributes={
                        "section": "Pharmacokinetics",
                        "clinical_significance": "normal",
                        "regulatory_impact": "medium",
                        "evidence_quality": "strong",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="No accumulation observed with twice-daily dosing.",
                    extraction_class="analysis_body",
                    attributes={
                        "section": "Pharmacokinetics",
                        "clinical_significance": "normal",
                        "regulatory_impact": "medium",
                        "evidence_quality": "strong",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="No significant impairment in cognitive testing batteries compared to placebo.",
                    extraction_class="analysis_body",
                    attributes={
                        "section": "Cognitive Function",
                        "clinical_significance": "normal",
                        "regulatory_impact": "medium",
                        "safety_level": "routine",
                        "evidence_quality": "strong",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="Discontinuation syndrome was minimal with gradual taper protocol.",
                    extraction_class="analysis_body",
                    attributes={
                        "section": "Withdrawal Assessment",
                        "clinical_significance": "minor",
                        "regulatory_impact": "medium",
                        "safety_level": "routine",
                        "evidence_quality": "moderate",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="Initiate at 5mg twice daily, titrate to 10mg twice daily based on response and tolerability.",
                    extraction_class="recommendations_section",
                    attributes={
                        "section": "Dosing",
                        "safety_level": "routine",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="REGULATORY SUBMISSION: FDA Pre-IND meeting scheduled for Q2 2024",
                    extraction_class="regulatory_footer",
                    attributes={},
                ),
            ],
        ),
        lx.data.ExampleData(
            text=textwrap.dedent(
                """\
                ANTIMICROBIAL AGENT: Ceftriaxone 2g IV
                INDICATION: Community-acquired pneumonia
                MICROBIOLOGICAL ANALYSIS: Streptococcus pneumoniae susceptibility

                MINIMUM INHIBITORY CONCENTRATION:
                MIC90 for S. pneumoniae was 0.25 μg/mL, demonstrating excellent in vitro activity.

                CLINICAL CURE RATES:
                Clinical success rate was 94.2% (95% CI: 89.1-97.3%) in the per-protocol population.

                MICROBIOLOGICAL ERADICATION:
                Pathogen eradication achieved in 91.8% of evaluable patients at test-of-cure visit.

                RESISTANCE DEVELOPMENT:
                No resistance emergence detected during the 14-day treatment course.

                SAFETY MONITORING:
                Clostridioides difficile infection rate was 2.1%, consistent with other beta-lactam antibiotics.

                RENAL DOSING:
                No dose adjustment required for creatinine clearance >30 mL/min. Reduce to 1g daily for CrCl 10-30 mL/min.

                ANTIMICROBIAL STEWARDSHIP: Use restricted to documented resistant organisms per institutional guidelines.
                """
            ).rstrip(),
            extractions=[
                lx.data.Extraction(
                    extraction_text="ANTIMICROBIAL AGENT: Ceftriaxone 2g IV",
                    extraction_class="report_header",
                    attributes={
                        "section": "Protocol Summary",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="INDICATION: Community-acquired pneumonia",
                    extraction_class="report_header",
                    attributes={
                        "section": "Protocol Summary",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="MICROBIOLOGICAL ANALYSIS: Streptococcus pneumoniae susceptibility",
                    extraction_class="report_header",
                    attributes={
                        "section": "Study Design",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="MIC90 for S. pneumoniae was 0.25 μg/mL, demonstrating excellent in vitro activity.",
                    extraction_class="analysis_body",
                    attributes={
                        "section": "Microbiological Analysis",
                        "clinical_significance": "significant",
                        "regulatory_impact": "high",
                        "evidence_quality": "strong",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="Clinical success rate was 94.2% (95% CI: 89.1-97.3%) in the per-protocol population.",
                    extraction_class="analysis_body",
                    attributes={
                        "section": "Efficacy Analysis",
                        "clinical_significance": "significant",
                        "regulatory_impact": "high",
                        "evidence_quality": "strong",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="Pathogen eradication achieved in 91.8% of evaluable patients at test-of-cure visit.",
                    extraction_class="analysis_body",
                    attributes={
                        "section": "Microbiological Analysis",
                        "clinical_significance": "significant",
                        "regulatory_impact": "high",
                        "evidence_quality": "strong",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="No resistance emergence detected during the 14-day treatment course.",
                    extraction_class="analysis_body",
                    attributes={
                        "section": "Resistance Analysis",
                        "clinical_significance": "normal",
                        "regulatory_impact": "medium",
                        "safety_level": "routine",
                        "evidence_quality": "strong",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="Clostridioides difficile infection rate was 2.1%, consistent with other beta-lactam antibiotics.",
                    extraction_class="analysis_body",
                    attributes={
                        "section": "Safety Profile",
                        "clinical_significance": "minor",
                        "regulatory_impact": "medium",
                        "safety_level": "caution",
                        "evidence_quality": "strong",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="No dose adjustment required for creatinine clearance >30 mL/min.",
                    extraction_class="recommendations_section",
                    attributes={
                        "section": "Dosing",
                        "safety_level": "routine",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="Reduce to 1g daily for CrCl 10-30 mL/min.",
                    extraction_class="recommendations_section",
                    attributes={
                        "section": "Dosing",
                        "safety_level": "caution",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="ANTIMICROBIAL STEWARDSHIP: Use restricted to documented resistant organisms per institutional guidelines.",
                    extraction_class="regulatory_footer",
                    attributes={},
                ),
            ],
        ),
        lx.data.ExampleData(
            text=textwrap.dedent(
                """\
                PEDIATRIC STUDY: PED-EPILEPSY-2024
                INVESTIGATIONAL DRUG: Levetiracetam oral solution
                AGE GROUPS: 6 months to 16 years
                INDICATION: Partial-onset seizures

                SEIZURE FREQUENCY REDUCTION:
                Median seizure frequency decreased by 67% from baseline in the treatment group.

                AGE-STRATIFIED ANALYSIS:
                Children 6-24 months showed 52% reduction. Ages 2-12 years had 71% reduction. Adolescents 13-16 years achieved 69% reduction.

                PHARMACOKINETIC DIFFERENCES:
                Clearance was 40% higher in pediatric patients compared to adults, requiring dose adjustment.

                BEHAVIORAL ASSESSMENTS:
                No significant behavioral changes or cognitive impairment observed using validated pediatric scales.

                DOSING IN CHILDREN:
                Start 10mg/kg twice daily, increase to 30mg/kg twice daily based on response and tolerance.

                SAFETY IN PEDIATRICS:
                Somnolence occurred in 18% versus 9% in placebo. Growth parameters remained normal.

                PEDIATRIC EXCLUSIVITY: FDA granted 6-month pediatric exclusivity extension under PREA.
                """
            ).rstrip(),
            extractions=[
                lx.data.Extraction(
                    extraction_text="PEDIATRIC STUDY: PED-EPILEPSY-2024",
                    extraction_class="report_header",
                    attributes={
                        "section": "Protocol Summary",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="INVESTIGATIONAL DRUG: Levetiracetam oral solution",
                    extraction_class="report_header",
                    attributes={
                        "section": "Protocol Summary",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="AGE GROUPS: 6 months to 16 years",
                    extraction_class="report_header",
                    attributes={
                        "section": "Study Design",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="INDICATION: Partial-onset seizures",
                    extraction_class="report_header",
                    attributes={
                        "section": "Protocol Summary",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="Median seizure frequency decreased by 67% from baseline in the treatment group.",
                    extraction_class="analysis_body",
                    attributes={
                        "section": "Efficacy Analysis",
                        "clinical_significance": "significant",
                        "regulatory_impact": "high",
                        "evidence_quality": "strong",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="Children 6-24 months showed 52% reduction.",
                    extraction_class="analysis_body",
                    attributes={
                        "section": "Age-Stratified Analysis",
                        "clinical_significance": "significant",
                        "regulatory_impact": "high",
                        "evidence_quality": "strong",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="Ages 2-12 years had 71% reduction.",
                    extraction_class="analysis_body",
                    attributes={
                        "section": "Age-Stratified Analysis",
                        "clinical_significance": "significant",
                        "regulatory_impact": "high",
                        "evidence_quality": "strong",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="Adolescents 13-16 years achieved 69% reduction.",
                    extraction_class="analysis_body",
                    attributes={
                        "section": "Age-Stratified Analysis",
                        "clinical_significance": "significant",
                        "regulatory_impact": "high",
                        "evidence_quality": "strong",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="Clearance was 40% higher in pediatric patients compared to adults, requiring dose adjustment.",
                    extraction_class="analysis_body",
                    attributes={
                        "section": "Pharmacokinetics",
                        "clinical_significance": "significant",
                        "regulatory_impact": "high",
                        "evidence_quality": "strong",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="No significant behavioral changes or cognitive impairment observed using validated pediatric scales.",
                    extraction_class="analysis_body",
                    attributes={
                        "section": "Behavioral Assessment",
                        "clinical_significance": "normal",
                        "regulatory_impact": "medium",
                        "safety_level": "routine",
                        "evidence_quality": "strong",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="Somnolence occurred in 18% versus 9% in placebo.",
                    extraction_class="analysis_body",
                    attributes={
                        "section": "Safety Profile",
                        "clinical_significance": "minor",
                        "regulatory_impact": "medium",
                        "safety_level": "caution",
                        "evidence_quality": "strong",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="Growth parameters remained normal.",
                    extraction_class="analysis_body",
                    attributes={
                        "section": "Safety Profile",
                        "clinical_significance": "normal",
                        "regulatory_impact": "medium",
                        "safety_level": "routine",
                        "evidence_quality": "strong",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="Start 10mg/kg twice daily, increase to 30mg/kg twice daily based on response and tolerance.",
                    extraction_class="recommendations_section",
                    attributes={
                        "section": "Pediatric Dosing",
                        "safety_level": "routine",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="PEDIATRIC EXCLUSIVITY: FDA granted 6-month pediatric exclusivity extension under PREA.",
                    extraction_class="regulatory_footer",
                    attributes={},
                ),
            ],
        ),
        lx.data.ExampleData(
            text=textwrap.dedent(
                """\
                BIOSIMILAR STUDY: BIO-ADALIMUMAB-2024
                REFERENCE PRODUCT: Humira® (adalimumab)
                INDICATION: Rheumatoid arthritis
                STUDY TYPE: Pharmacokinetic and pharmacodynamic equivalence

                BIOEQUIVALENCE ANALYSIS:
                AUC ratio (test/reference) was 1.02 (90% CI: 0.95-1.09), meeting bioequivalence criteria.

                Cmax ratio was 0.98 (90% CI: 0.91-1.06), within acceptable range.

                IMMUNOGENICITY COMPARISON:
                Anti-drug antibody incidence was 12.3% for biosimilar versus 11.8% for reference product (p=0.843).

                CLINICAL EFFICACY:
                ACR20 response rates were equivalent: 68.2% biosimilar versus 66.9% reference (95% CI for difference: -8.1 to 10.7).

                MANUFACTURING COMPLIANCE:
                Production facility inspected and approved by FDA. All lots released meet quality specifications.

                INTERCHANGEABILITY:
                Not established. Switching should be done under physician supervision.

                FDA APPROVAL: BLA 761071, Approved under 351(k) pathway, September 2024
                """
            ).rstrip(),
            extractions=[
                lx.data.Extraction(
                    extraction_text="BIOSIMILAR STUDY: BIO-ADALIMUMAB-2024",
                    extraction_class="report_header",
                    attributes={
                        "section": "Protocol Summary",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="REFERENCE PRODUCT: Humira® (adalimumab)",
                    extraction_class="report_header",
                    attributes={
                        "section": "Protocol Summary",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="INDICATION: Rheumatoid arthritis",
                    extraction_class="report_header",
                    attributes={
                        "section": "Protocol Summary",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="STUDY TYPE: Pharmacokinetic and pharmacodynamic equivalence",
                    extraction_class="report_header",
                    attributes={
                        "section": "Study Design",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="AUC ratio (test/reference) was 1.02 (90% CI: 0.95-1.09), meeting bioequivalence criteria.",
                    extraction_class="analysis_body",
                    attributes={
                        "section": "Bioequivalence Analysis",
                        "clinical_significance": "significant",
                        "regulatory_impact": "critical",
                        "evidence_quality": "strong",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="Cmax ratio was 0.98 (90% CI: 0.91-1.06), within acceptable range.",
                    extraction_class="analysis_body",
                    attributes={
                        "section": "Bioequivalence Analysis",
                        "clinical_significance": "significant",
                        "regulatory_impact": "critical",
                        "evidence_quality": "strong",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="Anti-drug antibody incidence was 12.3% for biosimilar versus 11.8% for reference product (p=0.843).",
                    extraction_class="analysis_body",
                    attributes={
                        "section": "Immunogenicity Analysis",
                        "clinical_significance": "normal",
                        "regulatory_impact": "high",
                        "safety_level": "routine",
                        "evidence_quality": "strong",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="ACR20 response rates were equivalent: 68.2% biosimilar versus 66.9% reference (95% CI for difference: -8.1 to 10.7).",
                    extraction_class="analysis_body",
                    attributes={
                        "section": "Clinical Efficacy",
                        "clinical_significance": "significant",
                        "regulatory_impact": "critical",
                        "evidence_quality": "strong",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="Production facility inspected and approved by FDA. All lots released meet quality specifications.",
                    extraction_class="analysis_body",
                    attributes={
                        "section": "Manufacturing Quality",
                        "clinical_significance": "normal",
                        "regulatory_impact": "critical",
                        "evidence_quality": "definitive",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="Not established. Switching should be done under physician supervision.",
                    extraction_class="recommendations_section",
                    attributes={
                        "section": "Interchangeability",
                        "safety_level": "caution",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="FDA APPROVAL: BLA 761071, Approved under 351(k) pathway, September 2024",
                    extraction_class="regulatory_footer",
                    attributes={},
                ),
            ],
        ),
        lx.data.ExampleData(
            text=textwrap.dedent(
                """\
                RARE DISEASE PROTOCOL: ORPHAN-HEMOPHILIA-2024
                INVESTIGATIONAL THERAPY: Factor IX gene therapy (AAV-FIX)
                ORPHAN DESIGNATION: FDA Orphan Drug Designation #24-5678
                TARGET POPULATION: Severe hemophilia B patients

                FACTOR IX ACTIVITY:
                Mean Factor IX activity increased from <1% to 42% of normal (range: 28-67%) at 26 weeks.

                BLEEDING EPISODES:
                Annualized bleeding rate decreased by 96% compared to baseline (0.8 vs 19.2 events/year).

                FACTOR IX CONCENTRATE USE:
                Complete elimination of prophylactic Factor IX concentrate in 89% of patients.

                IMMUNOLOGICAL RESPONSE:
                Transient ALT elevation observed in 23% of patients, managed with prednisolone.

                LONG-TERM FOLLOW-UP:
                Sustained Factor IX expression maintained at 3-year follow-up with no safety concerns.

                DOSING REGIMEN:
                Single intravenous infusion of 2×10¹³ vg/kg administered over 60 minutes.

                SPECIAL POPULATION:
                Limited to patients without pre-existing AAV antibodies and normal liver function.

                ORPHAN DRUG EXCLUSIVITY: FDA granted 7-year market exclusivity under Orphan Drug Act
                """
            ).rstrip(),
            extractions=[
                lx.data.Extraction(
                    extraction_text="RARE DISEASE PROTOCOL: ORPHAN-HEMOPHILIA-2024",
                    extraction_class="report_header",
                    attributes={
                        "section": "Protocol Summary",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="INVESTIGATIONAL THERAPY: Factor IX gene therapy (AAV-FIX)",
                    extraction_class="report_header",
                    attributes={
                        "section": "Protocol Summary",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="ORPHAN DESIGNATION: FDA Orphan Drug Designation #24-5678",
                    extraction_class="report_header",
                    attributes={
                        "section": "Regulatory Status",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="TARGET POPULATION: Severe hemophilia B patients",
                    extraction_class="report_header",
                    attributes={
                        "section": "Study Design",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="Mean Factor IX activity increased from <1% to 42% of normal (range: 28-67%) at 26 weeks.",
                    extraction_class="analysis_body",
                    attributes={
                        "section": "Efficacy Analysis",
                        "clinical_significance": "critical",
                        "regulatory_impact": "critical",
                        "evidence_quality": "strong",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="Annualized bleeding rate decreased by 96% compared to baseline (0.8 vs 19.2 events/year).",
                    extraction_class="analysis_body",
                    attributes={
                        "section": "Clinical Outcomes",
                        "clinical_significance": "critical",
                        "regulatory_impact": "critical",
                        "evidence_quality": "strong",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="Complete elimination of prophylactic Factor IX concentrate in 89% of patients.",
                    extraction_class="analysis_body",
                    attributes={
                        "section": "Treatment Impact",
                        "clinical_significance": "critical",
                        "regulatory_impact": "high",
                        "evidence_quality": "strong",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="Transient ALT elevation observed in 23% of patients, managed with prednisolone.",
                    extraction_class="analysis_body",
                    attributes={
                        "section": "Safety Profile",
                        "clinical_significance": "minor",
                        "regulatory_impact": "medium",
                        "safety_level": "caution",
                        "evidence_quality": "strong",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="Sustained Factor IX expression maintained at 3-year follow-up with no safety concerns.",
                    extraction_class="analysis_body",
                    attributes={
                        "section": "Long-term Safety",
                        "clinical_significance": "significant",
                        "regulatory_impact": "high",
                        "safety_level": "routine",
                        "evidence_quality": "strong",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="Single intravenous infusion of 2×10¹³ vg/kg administered over 60 minutes.",
                    extraction_class="recommendations_section",
                    attributes={
                        "section": "Administration",
                        "safety_level": "routine",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="Limited to patients without pre-existing AAV antibodies and normal liver function.",
                    extraction_class="recommendations_section",
                    attributes={
                        "section": "Patient Selection",
                        "safety_level": "contraindication",
                    },
                ),
                lx.data.Extraction(
                    extraction_text="ORPHAN DRUG EXCLUSIVITY: FDA granted 7-year market exclusivity under Orphan Drug Act",
                    extraction_class="regulatory_footer",
                    attributes={},
                ),
            ],
        ),
    ]


class ReportExamples:
    """Class containing pharmaceutical report examples for different document types"""
    
    @staticmethod
    def get_medical_examples():
        """Get medical entity extraction examples"""
        return get_examples_for_model()
    
    @staticmethod
    def get_financial_examples():
        """Get financial entity extraction examples"""
        # For now, return medical examples as placeholder
        # This can be expanded with financial examples later
        return get_examples_for_model()
    
    @staticmethod
    def get_legal_examples():
        """Get legal entity extraction examples"""
        # For now, return medical examples as placeholder
        # This can be expanded with legal examples later
        return get_examples_for_model()
