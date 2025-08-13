# PharmExtract - Pharmaceutical Report Analysis

A professional-grade web application for analyzing and structuring pharmaceutical reports using advanced AI-powered entity extraction. PharmExtract specializes in categorizing pharmaceutical documents into semantic sections with clinical significance and regulatory compliance annotations.

## Features

- **Pharmaceutical Specialization**: Expert-level analysis of clinical trial reports, drug safety assessments, and regulatory submissions
- **Semantic Sectioning**: Automatic categorization into report_header, analysis_body, recommendations_section, and regulatory_footer
- **Clinical Significance Assessment**: AI-powered evaluation of findings with clinical impact ratings
- **Regulatory Compliance**: Built-in FDA/EMA compliance checking and regulatory impact assessment
- **Dark Theme UI**: Modern, professional interface optimized for medical professionals
- **Interactive Entity Mapping**: Hover over any extracted entity to see source text highlighting
- **Rich Attribute System**: Comprehensive metadata including safety levels, evidence quality, and regulatory impact
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Keyboard Shortcuts**: Use Ctrl+Enter for quick text processing
- **Real-time Analysis**: Instant pharmaceutical report structuring with visual feedback

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd langextract_input_output
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set your LangExtract API key:
   ```bash
   export LANGEXTRACT_API_KEY="your-api-key-here"
   ```
   
   Or create a `.env` file:
   ```bash
   echo "LANGEXTRACT_API_KEY=your-api-key-here" > .env
   ```

## Usage

1. Start the PharmExtract application:
   ```bash
   python app.py
   ```

2. Open your browser and navigate to `http://localhost:5000`

3. Use the sample cardiovascular clinical trial report or enter your own pharmaceutical text

4. Select document type:
   - **Clinical Trial Reports**: For efficacy and safety studies
   - **Drug Safety Reports**: For pharmacovigilance and regulatory reports

5. Click "Process Text" or press Ctrl+Enter

6. View structured pharmaceutical entities organized by semantic sections

7. Hover over any entity to see source mapping and clinical significance details

## Pharmaceutical Report Structure

PharmExtract automatically categorizes pharmaceutical reports into four main sections:

### 1. Report Header (`report_header`)
- **Protocol Summary**: Study IDs, objectives, and overview
- **Regulatory Status**: FDA/EMA submissions, IND numbers, CTA references
- **Study Design**: Methodology, population, and study phases
- **Investigator Information**: Principal investigators and institutions
- **Approval Information**: IRB approvals and regulatory milestones

### 2. Analysis Body (`analysis_body`)
- **Efficacy Analysis**: Primary/secondary endpoints, statistical significance
- **Safety Profile**: Adverse events, tolerability, and safety monitoring
- **Pharmacokinetics**: PK parameters, bioavailability, and drug interactions
- **Clinical Outcomes**: Patient responses, biomarkers, and therapeutic effects
- **Population Analysis**: Subgroup analyses and special populations

### 3. Recommendations Section (`recommendations_section`)
- **Dosing Guidelines**: Initial doses, titration schedules, and maximum doses
- **Patient Selection**: Inclusion/exclusion criteria and contraindications
- **Monitoring Requirements**: Safety monitoring and follow-up protocols
- **Special Populations**: Pediatric, geriatric, and renal/hepatic dosing

### 4. Regulatory Footer (`regulatory_footer`)
- **Approval Status**: FDA/EMA approval numbers and dates
- **Compliance Statements**: GCP adherence and regulatory requirements
- **Manufacturing Quality**: GMP compliance and facility approvals
- **Post-marketing Requirements**: Surveillance and risk management

## Clinical Significance Attributes

Each analysis_body extraction includes comprehensive clinical assessment:

- **Clinical Significance**: normal, minor, significant, critical, not_applicable
- **Regulatory Impact**: low, medium, high, critical
- **Safety Level**: routine, caution, warning, contraindication
- **Evidence Quality**: preliminary, moderate, strong, definitive

## Therapeutic Areas Supported

PharmExtract handles specialized pharmaceutical domains:

- **Oncology**: Cancer drug development and biomarker analysis
- **Cardiovascular**: Heart disease prevention and treatment
- **Central Nervous System**: Psychiatric and neurological disorders
- **Infectious Disease**: Antimicrobial resistance and treatment
- **Pediatrics**: Age-specific dosing and safety
- **Rare Diseases**: Orphan drug development and orphan designations
- **Biosimilars**: Generic drug equivalence and interchangeability

## UI Components

### Input Panel (Left)
- Large text area for pharmaceutical reports
- Sample cardiovascular clinical trial report pre-loaded
- Real-time source highlighting during entity hover

### Output Panel (Right)
- Structured pharmaceutical entities grouped by semantic sections
- Color-coded categories with professional medical styling
- Interactive entities with hover and click functionality

### Document Type Selection
- **Clinical Trial Reports**: Optimized for efficacy and safety studies
- **Drug Safety Reports**: Focused on pharmacovigilance and regulatory compliance

### Source Mapping Display
- Detailed entity information below the panels
- Clinical significance and regulatory impact details
- Source text highlighting in the input panel

## Sample Data

The application includes a comprehensive cardiovascular clinical trial report example:

- **Protocol**: CARDIO-HTN-2024-892
- **Study**: Phase III Double-Blind Study of Antihypertensive Agent ACE-X47
- **Endpoints**: Blood pressure reduction, response rates, time to control
- **Safety**: Adverse event profiles and laboratory monitoring
- **Dosing**: Titration schedules and maximum recommended doses

## Customization

### Adding New Therapeutic Areas
Edit `prompt_instructions.py` to modify pharmaceutical prompt instructions for different therapeutic domains.

### Expanding Examples
Add new pharmaceutical report examples in `report_examples.py` for different document types.

### Styling
Modify `static/style.css` to customize colors, fonts, and medical report styling.

### Functionality
Extend `static/app.js` to add new pharmaceutical analysis features and interactions.

## Technical Architecture

- **Backend**: Flask with LangExtract AI integration
- **AI Engine**: Advanced pharmaceutical prompt engineering
- **Frontend**: Vanilla JavaScript with medical-optimized CSS
- **API**: RESTful endpoint for pharmaceutical text processing
- **Data Structure**: JSON-based pharmaceutical entity extraction
- **Responsive**: Mobile-first design for clinical workflow integration

## Keyboard Shortcuts

- `Ctrl + Enter`: Process pharmaceutical text
- `Tab`: Navigate between input and output panels
- `Escape`: Clear entity highlights and source mapping

## Browser Support

- Chrome/Edge (recommended for medical applications)
- Firefox
- Safari
- Mobile browsers (optimized for clinical tablet use)

## Troubleshooting

### API Key Issues
- Ensure `LANGEXTRACT_API_KEY` environment variable is set
- Check API key validity and LangExtract service status
- Verify `.env` file configuration

### Processing Errors
- Verify pharmaceutical text input is not empty
- Check browser console for JavaScript errors
- Ensure Flask server is running and accessible

### UI Issues
- Clear browser cache and reload
- Check browser compatibility for medical applications
- Verify all static files are properly loaded

### Pharmaceutical Analysis Issues
- Ensure text follows standard pharmaceutical report format
- Check that clinical significance attributes are properly formatted
- Verify regulatory compliance information is complete

## Regulatory Compliance

PharmExtract is designed to support pharmaceutical industry standards:

- **Good Clinical Practice (GCP)**: ICH guidelines compliance
- **FDA Requirements**: 21 CFR Part 312 and Part 314 compliance
- **EMA Standards**: European regulatory submission requirements
- **Pharmacovigilance**: Drug safety monitoring and reporting
- **Clinical Data Integrity**: ALCOA+ principles support

## License

This project is open source and available under the MIT License.

## Support

For pharmaceutical industry users and clinical research organizations, please refer to the comprehensive documentation in the `prompt_instructions.py` and `report_examples.py` files for detailed pharmaceutical analysis guidelines.