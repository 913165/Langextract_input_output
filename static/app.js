// Sample report data
const sampleReports = {
    cardiovascular: `PROTOCOL NUMBER: CARDIO-HTN-2024-892
STUDY TITLE: Phase III Double-Blind Study of Antihypertensive Agent ACE-X47
PRINCIPAL INVESTIGATOR: Dr. Michael Rodriguez, MD
REGULATORY STATUS: FDA IND 67891, EMA CTA 2024-002847-33
IRB APPROVAL: Metropolitan Medical Center IRB #2024-1456, Approved August 22, 2024

EFFICACY ANALYSIS:
Primary endpoint of systolic blood pressure reduction was achieved with statistical significance. Mean reduction from baseline was 18.4 mmHg in the treatment group versus 3.2 mmHg in placebo group (p<0.001). Diastolic blood pressure decreased by 11.7 mmHg versus 1.8 mmHg respectively (p<0.001). Response rate, defined as achieving target blood pressure <140/90 mmHg, was 78.3% in active treatment versus 24.1% in placebo group. Time to blood pressure control was significantly shorter at 4.2 weeks compared to 12.8 weeks.

PHARMACOKINETIC PARAMETERS:
Peak plasma concentration was reached at 2.8 hours post-dose. Half-life was 14.6 hours, supporting once-daily dosing. Steady-state achieved by day 5 with no significant accumulation.

SAFETY PROFILE:
Treatment-emergent adverse events occurred in 42% of patients versus 38% placebo. Most common events were dizziness (8.1%), headache (6.3%), and fatigue (4.7%). No serious drug-related adverse events reported. Laboratory parameters remained stable throughout the study period.

DOSING RECOMMENDATIONS:
Initiate therapy at 10mg once daily. Titrate to 20mg daily after 2 weeks if blood pressure target not achieved. Maximum recommended dose is 40mg daily.

REGULATORY COMPLIANCE:
Study conducted per Good Clinical Practice guidelines and FDA 21 CFR Part 312 requirements.`,

    oncology: `PROTOCOL NUMBER: DIABETES-2024-445
STUDY TITLE: Phase II Study of Novel Antidiabetic Agent DIA-X23
PRINCIPAL INVESTIGATOR: Dr. Jennifer Martinez, MD, PhD
REGULATORY STATUS: FDA IND 98765, EMA CTA 2024-003456-78
IRB APPROVAL: Diabetes Research Institute IRB #2024-2234, Approved May 10, 2024

EFFICACY ANALYSIS:
Primary endpoint of HbA1c reduction was achieved with statistical significance. Mean reduction from baseline was 1.2% in the treatment group versus 0.3% in placebo group (p<0.001). Secondary endpoints showed fasting glucose reduction of 45 mg/dL versus 12 mg/dL respectively (p<0.001). Proportion of patients achieving HbA1c <7.0% was 68% in active treatment versus 22% in placebo group.

SAFETY PROFILE:
Treatment-emergent adverse events occurred in 76% of patients versus 71% placebo. Most common events: nausea (12%), diarrhea (8%), headache (6%). No serious drug-related adverse events reported. Hypoglycemia occurred in 3% of treatment group versus 1% placebo.

DOSING RECOMMENDATIONS:
Recommended Phase II dose is 50mg twice daily with meals. Dose adjustment based on renal function and concomitant medications.

REGULATORY COMPLIANCE:
This study was conducted in accordance with GCP guidelines and FDA 21 CFR Part 312.`,

    pharmacokinetic: `STUDY ID: CV-STATIN-2024
COMPOUND: Atorvastatin 40mg
INDICATION: Cardiovascular disease prevention
STUDY DESIGN: Randomized, double-blind, placebo-controlled

PHARMACOKINETIC PARAMETERS:
Cmax was 42.3 ± 8.7 ng/mL achieved at Tmax of 2.1 ± 0.8 hours. Half-life was determined to be 14.2 ± 3.1 hours. AUC0-∞ was 287 ± 62 ng⋅hr/mL with apparent clearance of 139 ± 31 L/hr.

EFFICACY ENDPOINTS:
LDL cholesterol reduction was 48% from baseline (p<0.001). HDL cholesterol increased by 12% (p=0.023). Primary composite endpoint was reduced by 22% (HR=0.78, 95% CI: 0.65-0.94, p=0.009).

ADVERSE EVENTS:
Myalgia was reported in 8.2% of patients. Liver enzyme elevation >3x ULN occurred in 1.1% of patients.

CONTRAINDICATIONS:
Active liver disease or unexplained persistent liver enzyme elevations.

FDA APPROVAL STATUS: NDA 20-702, Approved December 17, 1996`,

    safety: `ADVERSE EVENT REPORT: AE-2024-001
REPORTING DATE: December 15, 2024
DRUG: NovelCardio (ACE-X47)
INDICATION: Hypertension
REPORTER: Dr. Emily Watson, MD

PATIENT INFORMATION:
Age: 67 years, Gender: Female, Weight: 72 kg
Medical History: Hypertension, Type 2 diabetes, mild renal impairment

ADVERSE EVENT DESCRIPTION:
Patient experienced severe dizziness and syncope 3 hours after taking NovelCardio 20mg. Event occurred while standing and resulted in fall with minor bruising. No loss of consciousness, but patient was disoriented for approximately 10 minutes.

TIMELINE:
- Drug administered: 08:00 AM
- Event onset: 11:00 AM
- Event resolution: 11:10 AM
- Medical attention: 11:15 AM

OUTCOME:
Patient recovered fully within 30 minutes. Drug discontinued. No permanent sequelae. Event classified as serious due to fall risk.

CAUSALITY ASSESSMENT:
Probable - temporal relationship, known side effect, dechallenge positive.`,

    regulatory: `REGULATORY SUBMISSION EXCERPT: NDA 20-789
DRUG: NovelCardio (ACE-X47)
INDICATION: Treatment of hypertension
APPLICANT: PharmaCorp Inc.
SUBMISSION DATE: November 30, 2024

REGULATORY STATUS:
- FDA Fast Track Designation: Granted March 2024
- Breakthrough Therapy Designation: Pending
- Priority Review: Requested
- Orphan Drug Status: Not applicable

CLINICAL DATA SUMMARY:
- Phase III studies completed: 3 studies, 2,847 patients
- Primary endpoints met: All studies achieved statistical significance
- Safety database: 3,156 patients, 2,847 patient-years exposure
- Post-marketing commitments: 5-year safety surveillance study

MANUFACTURING COMPLIANCE:
- GMP facility: FDA inspected and approved
- Quality control: All specifications met
- Stability data: 24-month data available
- Process validation: Complete

REGULATORY MILESTONES:
- Pre-NDA meeting: Completed September 2024
- Advisory Committee: Scheduled January 2025
- PDUFA date: March 15, 2025`
};

function loadSampleReport(reportType) {
    const reportText = sampleReports[reportType];
    if (reportText) {
        document.getElementById('inputText').value = reportText;
        showNotification(`Loaded ${reportType} sample report`, 'success');
        
        // Clear any previous output
        document.getElementById('outputContent').innerHTML = '';
        document.getElementById('sourceMapping').classList.remove('visible');
    }
}

// Global variables for entity tracking
let currentEntities = [];
let inputTextWithHighlights = '';

// Initialize the application
document.addEventListener('DOMContentLoaded', function() {
    setupEventListeners();
    loadSampleData();
});

function setupEventListeners() {
    document.getElementById('processBtn').addEventListener('click', processText);
    
    // Checkbox event listeners
    document.getElementById('lxPrompt').addEventListener('change', function() {
        console.log('LX Generated Prompt:', this.checked);
        // You can add functionality here to show/hide prompt information
    });
    
    document.getElementById('lxData').addEventListener('change', function() {
        console.log('LX Structured Output:', this.checked);
        // You can add functionality here to show/hide data information
    });
    
    // Add keyboard shortcuts
    document.addEventListener('keydown', function(e) {
        if (e.ctrlKey && e.key === 'Enter') {
            e.preventDefault();
            processText();
        }
    });
}

function loadSampleData() {
    // Load the cardiovascular report by default
    loadSampleReport('cardiovascular');
}

function getDocumentType() {
    // Get the selected document type from checkboxes
    const useLXPrompt = document.getElementById('lxPrompt').checked;
    const useLXData = document.getElementById('lxData').checked;
    
    // Determine examples type based on checkboxes
    let examplesType = "medical"; // default to medical examples
    
    if (useLXData) {
        examplesType = "legal"; // Use legal examples for structured output (regulatory focus)
    } else if (useLXPrompt) {
        examplesType = "medical"; // Use medical examples for generated prompt
    } else {
        // Neither checked - use medical examples (default)
        examplesType = "medical";
    }
    
    return { examplesType };
}

async function processText() {
    const inputText = document.getElementById('inputText').value;
    const outputContent = document.getElementById('outputContent');
    const sourceMapping = document.getElementById('sourceMapping');
    const processBtn = document.getElementById('processBtn');
    const modelSelect = document.getElementById('modelSelect');
    
    if (!inputText.trim()) {
        outputContent.innerHTML = '<p style="color: #888;">Please enter some text.</p>';
        return;
    }
    
    // Set loading state
    setLoadingState(true);
    outputContent.innerHTML = '<p style="color: #888;">Processing...</p>';
    sourceMapping.classList.remove('visible');
    
    try {
        // Get document type selection and selected model
        const { examplesType } = getDocumentType();
        const selectedModel = modelSelect.value;
        
        console.log(`Processing with model: ${selectedModel}`);
        
        const response = await fetch('/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ 
                text: inputText,
                examples_type: examplesType,
                model_id: selectedModel
            })
        });
        
        const data = await response.json();
        
        if (data.error) {
            outputContent.innerHTML = `<p style="color: #ff6b6b;">Error: ${data.error}</p>`;
            return;
        }
        
        // Process and display the results
        displayExtractions(inputText, data.result);
        
        // Show success message with extraction count, type info, and model used
        let message = `Extraction completed! Found ${data.extractions_count} entities using ${selectedModel}.`;
        if (data.examples_type) {
            message += ` (Examples: ${data.examples_type})`;
        }
        showNotification(message, 'success');
        
    } catch (err) {
        outputContent.innerHTML = `<p style="color: #ff6b6b;">Error: ${err.message}</p>`;
        showNotification('Error during extraction', 'error');
    } finally {
        setLoadingState(false);
    }
}

function setLoadingState(loading) {
    const processBtn = document.getElementById('processBtn');
    const container = document.querySelector('.container');
    
    if (loading) {
        processBtn.disabled = true;
        processBtn.textContent = 'Processing...';
        container.classList.add('loading');
    } else {
        processBtn.disabled = false;
        processBtn.textContent = 'Process';
        container.classList.remove('loading');
    }
}

function displayExtractions(inputText, result) {
    const outputContent = document.getElementById('outputContent');
    
    if (!result || !result.extractions || result.extractions.length === 0) {
        outputContent.innerHTML = '<p style="color: #888;">No extractions found.</p>';
        return;
    }
    
    // Debug: Log the extraction data to understand the structure
    console.log('Raw extraction data:', result.extractions);
    console.log('Input text length:', inputText.length);
    console.log('Input text sample:', inputText.substring(0, 200) + '...');
    
    // Store entities globally for hover functionality
    currentEntities = result.extractions;
    
    // Create structured output similar to the image
    let outputHTML = '';
    
    // Group extractions by class for better organization
    const groupedExtractions = groupExtractionsByClass(result.extractions);
    
    // Display each group with medical findings styling
    Object.keys(groupedExtractions).forEach(className => {
        const extractions = groupedExtractions[className];
        const displayName = formatClassName(className);
        
        outputHTML += `<div class="extraction-group" data-category="${className}">`;
        outputHTML += `<h4>${displayName}:</h4>`;
        
        extractions.forEach((extraction, index) => {
            const entityId = `entity-${className}-${index}`;
            // Debug: Log each extraction for debugging
            console.log(`Extraction ${index}:`, {
                text: extraction.extraction_text,
                class: extraction.extraction_class,
                attributes: extraction.attributes
            });
            outputHTML += `<span class="entity" id="${entityId}" data-entity-index="${index}" data-entity-class="${className}">${extraction.extraction_text}</span>`;
        });
        
        outputHTML += `</div>`;
    });
    
    outputContent.innerHTML = outputHTML;
    
    // Add hover event listeners to entities
    addEntityHoverListeners();
    
    // Only highlight entities in input if we have input text
    if (inputText) {
        highlightEntitiesInInput(inputText, result.extractions);
    }
}

function groupExtractionsByClass(extractions) {
    const grouped = {};
    
    extractions.forEach(extraction => {
        const className = extraction.extraction_class || 'unknown';
        if (!grouped[className]) {
            grouped[className] = [];
        }
        grouped[className].push(extraction);
    });
    
    return grouped;
}

function formatClassName(className) {
    // Convert snake_case to Title Case
    return className
        .split('_')
        .map(word => word.charAt(0).toUpperCase() + word.slice(1))
        .join(' ');
}

function addEntityHoverListeners() {
    const entities = document.querySelectorAll('.entity');
    
    entities.forEach(entity => {
        entity.addEventListener('mouseenter', function() {
            const entityIndex = parseInt(this.dataset.entityIndex);
            const entityClass = this.dataset.entityClass;
            const extraction = currentEntities.find((ex, idx) => 
                ex.extraction_class === entityClass && 
                currentEntities.filter(e => e.extraction_class === entityClass).indexOf(ex) === entityIndex
            );
            
            if (extraction) {
                highlightSourceInInput(extraction);
                showSourceMapping(extraction);
                this.classList.add('highlighted');
            }
        });
        
        entity.addEventListener('mouseleave', function() {
            clearInputHighlights();
            hideSourceMapping();
            this.classList.remove('highlighted');
        });
        
        // Add click functionality for mobile devices
        entity.addEventListener('click', function() {
            const entityIndex = parseInt(this.dataset.entityIndex);
            const entityClass = this.dataset.entityClass;
            const extraction = currentEntities.find((ex, idx) => 
                ex.extraction_class === entityClass && 
                currentEntities.filter(e => e.extraction_class === entityClass).indexOf(ex) === entityIndex
            );
            
            if (extraction) {
                // Toggle highlight on click for mobile
                if (this.classList.contains('highlighted')) {
                    clearInputHighlights();
                    hideSourceMapping();
                    this.classList.remove('highlighted');
                } else {
                    clearInputHighlights();
                    hideSourceMapping();
                    highlightSourceInInput(extraction);
                    showSourceMapping(extraction);
                    this.classList.add('highlighted');
                }
            }
        });
    });
}

function highlightSourceInInput(extraction) {
    const inputText = document.getElementById('inputText');
    const text = inputText.value;
    
    // If no input text is available, don't try to highlight
    if (!text || !extraction.extraction_text) return;
    
    const searchText = extraction.extraction_text.trim();
    
    // Debug: Log what we're searching for
    console.log(`Searching for: "${searchText}"`);
    console.log(`Input text length: ${text.length}`);
    console.log(`Extraction object:`, extraction);
    
    // Strategy 0: Use LangExtract's source span information if available
    if (extraction.source_span && extraction.source_span.start >= 0 && extraction.source_span.end > extraction.source_span.start) {
        const sourceText = text.substring(extraction.source_span.start, extraction.source_span.end);
        console.log(`Using source span: ${extraction.source_span.start}-${extraction.source_span.end}, text: "${sourceText}"`);
        
        if (sourceText && sourceText.length > 0) {
            // Highlight the exact source text
            highlightExactText(sourceText, extraction.source_span.start);
            return;
        }
    }
    
    // Try multiple strategies to find the text
    let startPos = -1;
    let matchedText = searchText;
    let matchStrategy = 'none';
    
    // Strategy 1: Exact match (case-insensitive)
    startPos = text.toLowerCase().indexOf(searchText.toLowerCase());
    if (startPos !== -1) {
        matchStrategy = 'exact';
        console.log(`Exact match found at position ${startPos}`);
    }
    
    // Strategy 2: If exact match fails, try to find the most similar text
    if (startPos === -1) {
        // Split the search text into meaningful phrases
        const phrases = searchText.split(/[.!?]+/).filter(phrase => phrase.trim().length > 10);
        
        if (phrases.length > 0) {
            // Try to find the longest phrase first
            phrases.sort((a, b) => b.trim().length - a.trim().length);
            
            for (const phrase of phrases) {
                const cleanPhrase = phrase.trim();
                if (cleanPhrase.length > 10) {
                    const pos = text.toLowerCase().indexOf(cleanPhrase.toLowerCase());
                    if (pos !== -1) {
                        startPos = pos;
                        matchedText = cleanPhrase;
                        matchStrategy = 'phrase';
                        console.log(`Phrase match found: "${cleanPhrase}" at position ${pos}`);
                        break;
                    }
                }
            }
        }
    }
    
    // Strategy 3: If still no match, try to find text with high word overlap
    if (startPos === -1) {
        const searchWords = searchText.toLowerCase().split(/\s+/).filter(word => word.length > 2);
        const textWords = text.toLowerCase().split(/\s+/);
        
        let bestMatch = { pos: -1, score: 0, text: '', overlap: 0 };
        
        // Look for sequences of words that have high overlap
        for (let i = 0; i < textWords.length; i++) {
            for (let len = Math.min(searchWords.length, 10); len >= 3; len--) {
                if (i + len > textWords.length) continue;
                
                const textSequence = textWords.slice(i, i + len);
                let overlap = 0;
                
                for (const searchWord of searchWords) {
                    if (textSequence.some(textWord => 
                        textWord.includes(searchWord) || searchWord.includes(textWord) ||
                        textWord === searchWord
                    )) {
                        overlap++;
                    }
                }
                
                const overlapRatio = overlap / searchWords.length;
                if (overlapRatio > bestMatch.overlap && overlapRatio > 0.6) {
                    bestMatch = { 
                        pos: i, 
                        score: overlap, 
                        text: textSequence.join(' '), 
                        overlap: overlapRatio 
                    };
                }
            }
        }
        
        if (bestMatch.overlap > 0.6) {
            startPos = text.toLowerCase().indexOf(bestMatch.text.toLowerCase());
            matchedText = bestMatch.text;
            matchStrategy = 'overlap';
            console.log(`Overlap match found: "${bestMatch.text}" with ${Math.round(bestMatch.overlap * 100)}% overlap`);
        }
    }
    
    // If we found a match, highlight it
    if (startPos !== -1) {
        console.log(`Final match: "${matchedText}" using strategy: ${matchStrategy}`);
        highlightExactText(matchedText, startPos);
        
        // Update source mapping to show what was actually matched
        if (matchedText !== searchText) {
            console.log(`Matched "${matchedText}" instead of "${searchText}"`);
            // Show a notification about the match difference
            showNotification(`Matched: "${matchedText}"`, 'info');
        }
    } else {
        console.log(`Could not find match for: "${searchText}"`);
        // Show a notification that highlighting failed
        showNotification(`Could not highlight source text for: ${searchText}`, 'error');
    }
}

function highlightExactText(textToHighlight, startPosition) {
    const inputText = document.getElementById('inputText');
    const text = inputText.value;
    
    // Create highlighted version of input text
    const regex = new RegExp(`(${textToHighlight.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')})`, 'gi');
    inputTextWithHighlights = text.replace(regex, '<span class="source-highlight">$1</span>');
    
    // Create a temporary div to show highlighted text
    const tempDiv = document.createElement('div');
    tempDiv.innerHTML = inputTextWithHighlights;
    tempDiv.style.cssText = `
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: #1e2a3a;
        color: #e0e0e0;
        padding: 18px;
        font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
        font-size: 14px;
        line-height: 1.6;
        overflow-y: auto;
        white-space: pre-wrap;
        z-index: 10;
        pointer-events: none;
    `;
    
    const inputPanel = document.querySelector('.input-panel .panel-content');
    inputPanel.style.position = 'relative';
    inputPanel.appendChild(tempDiv);
    
    // Store reference for cleanup
    inputPanel._tempHighlight = tempDiv;
    
    // Hide the original textarea
    inputText.style.visibility = 'hidden';
    
    // Scroll to the highlighted text
    const lineHeight = 22; // Approximate line height in pixels
    const charsPerLine = Math.floor(inputText.clientWidth / 8); // Approximate chars per line
    const lineNumber = Math.floor(startPosition / charsPerLine);
    const scrollTop = Math.max(0, (lineNumber * lineHeight) - (inputText.clientHeight / 2));
    
    // Apply scroll to both the original textarea and the highlight div
    inputText.scrollTop = scrollTop;
    tempDiv.scrollTop = scrollTop;
}

function clearInputHighlights() {
    const inputPanel = document.querySelector('.input-panel .panel-content');
    const inputText = document.getElementById('inputText');
    
    if (inputPanel._tempHighlight) {
        inputPanel.removeChild(inputPanel._tempHighlight);
        inputPanel._tempHighlight = null;
    }
    
    // Restore original textarea visibility
    if (inputText.style.visibility === 'hidden') {
        inputText.style.visibility = 'visible';
    }
}

function showSourceMapping(extraction) {
    const sourceMapping = document.getElementById('sourceMapping');
    
    let mappingHTML = `
        <h4>Source Mapping</h4>
        <div style="margin: 15px 0;">
            <strong>Entity:</strong> <span class="entity">${extraction.extraction_text}</span><br>
            <strong>Class:</strong> ${formatClassName(extraction.extraction_class)}<br>
            <strong>Source Text:</strong> <span class="source-highlight">${extraction.extraction_text}</span><br>
    `;
    
    if (extraction.attributes && Object.keys(extraction.attributes).length > 0) {
        mappingHTML += `<strong>Attributes:</strong><br>`;
        Object.entries(extraction.attributes).forEach(([key, value]) => {
            mappingHTML += `&nbsp;&nbsp;• ${key}: ${value}<br>`;
        });
    }
    
    mappingHTML += `</div>`;
    
    sourceMapping.innerHTML = mappingHTML;
    sourceMapping.classList.add('visible');
}

function hideSourceMapping() {
    const sourceMapping = document.getElementById('sourceMapping');
    sourceMapping.classList.remove('visible');
}

function showNotification(message, type = 'info') {
    // Create notification element
    const notification = document.createElement('div');
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: ${type === 'success' ? '#4CAF50' : type === 'error' ? '#f44336' : '#2196F3'};
        color: white;
        padding: 15px 20px;
        border-radius: 6px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        z-index: 1000;
        animation: slideInRight 0.3s ease-out;
        max-width: 300px;
    `;
    notification.textContent = message;
    
    // Add animation CSS
    const style = document.createElement('style');
    style.textContent = `
        @keyframes slideInRight {
            from { transform: translateX(100%); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }
    `;
    document.head.appendChild(style);
    
    document.body.appendChild(notification);
    
    // Remove notification after 3 seconds
    setTimeout(() => {
        notification.style.animation = 'slideOutRight 0.3s ease-in';
        notification.style.transform = 'translateX(100%)';
        setTimeout(() => {
            if (notification.parentNode) {
                notification.parentNode.removeChild(notification);
            }
        }, 300);
    }, 3000);
}

function highlightEntitiesInInput(inputText, extractions) {
    // This function can be used to show all entities highlighted in the input
    // Currently not used but available for future features
    let highlightedText = inputText;
    
    extractions.forEach(extraction => {
        if (extraction.extraction_text) {
            const regex = new RegExp(`(${extraction.extraction_text.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')})`, 'gi');
            highlightedText = highlightedText.replace(regex, '<span class="source-highlight">$1</span>');
        }
    });
    
    return highlightedText;
}

// Get the currently selected model
function getCurrentModel() {
    const modelSelect = document.getElementById('modelSelect');
    return modelSelect ? modelSelect.value : 'gemini-2.5-pro';
}

// Update model display when selection changes
function updateModelDisplay() {
    const modelSelect = document.getElementById('modelSelect');
    if (modelSelect) {
        const selectedModel = modelSelect.value;
        console.log(`Model changed to: ${selectedModel}`);
        
        // You can add additional UI updates here if needed
        // For example, updating a status indicator or showing model capabilities
    }
}

// Add event listener for model selection changes
document.addEventListener('DOMContentLoaded', function() {
    const modelSelect = document.getElementById('modelSelect');
    const modelSelection = document.querySelector('.model-selection');
    
    if (modelSelect) {
        modelSelect.addEventListener('change', updateModelDisplay);
        
        // Add focus/blur events for visual feedback
        modelSelect.addEventListener('focus', function() {
            if (modelSelection) {
                modelSelection.classList.add('active');
            }
        });
        
        modelSelect.addEventListener('blur', function() {
            if (modelSelection) {
                modelSelection.classList.remove('active');
            }
        });
        
        // Log initial model selection
        console.log(`Initial model selected: ${modelSelect.value}`);
    }
});