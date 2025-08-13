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
        console.log('LX Prompt:', this.checked);
        // You can add functionality here to show/hide prompt information
    });
    
    document.getElementById('lxData').addEventListener('change', function() {
        console.log('LX Data:', this.checked);
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
    const sampleText = `PROTOCOL NUMBER: CARDIO-HTN-2024-892
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
Study conducted per Good Clinical Practice guidelines and FDA 21 CFR Part 312 requirements.`;
    
    document.getElementById('inputText').value = sampleText;
}

function getDocumentType() {
    // Get the selected document type from checkboxes
    const useClinicalTrialExamples = document.getElementById('lxPrompt').checked;
    const useDrugSafetyExamples = document.getElementById('lxData').checked;
    
    // Determine examples type based on checkboxes
    let examplesType = "medical"; // default to medical examples
    
    if (useDrugSafetyExamples) {
        examplesType = "legal"; // Use legal examples for drug safety (regulatory focus)
    } else if (useClinicalTrialExamples) {
        examplesType = "medical"; // Use medical examples for clinical trials
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
    
    if (!inputText.trim()) {
        outputContent.innerHTML = '<p style="color: #888;">Please enter some text.</p>';
        return;
    }
    
    // Set loading state
    setLoadingState(true);
    outputContent.innerHTML = '<p style="color: #888;">Processing...</p>';
    sourceMapping.classList.remove('visible');
    
    try {
        // Get document type selection
        const { examplesType } = getDocumentType();
        
        const response = await fetch('/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ 
                text: inputText,
                examples_type: examplesType
            })
        });
        
        const data = await response.json();
        
        if (data.error) {
            outputContent.innerHTML = `<p style="color: #ff6b6b;">Error: ${data.error}</p>`;
            return;
        }
        
        // Process and display the results
        displayExtractions(inputText, data.result);
        
        // Show success message with extraction count and type info
        let message = `Extraction completed! Found ${data.extractions_count} entities.`;
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
        processBtn.textContent = 'Process Text';
        container.classList.remove('loading');
    }
}

function displayExtractions(inputText, result) {
    const outputContent = document.getElementById('outputContent');
    
    if (!result || !result.extractions || result.extractions.length === 0) {
        outputContent.innerHTML = '<p style="color: #888;">No extractions found.</p>';
        return;
    }
    
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
    
    const searchText = extraction.extraction_text;
    
    // Create highlighted version of input text
    const regex = new RegExp(`(${searchText.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')})`, 'gi');
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
        background: #404040;
        color: #ffffff;
        padding: 20px;
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
    const startPos = text.toLowerCase().indexOf(searchText.toLowerCase());
    if (startPos !== -1) {
        const lineHeight = 22; // Approximate line height in pixels
        const charsPerLine = Math.floor(inputText.clientWidth / 8); // Approximate chars per line
        const lineNumber = Math.floor(startPos / charsPerLine);
        const scrollTop = Math.max(0, (lineNumber * lineHeight) - (inputText.clientHeight / 2));
        
        // Apply scroll to both the original textarea and the highlight div
        inputText.scrollTop = scrollTop;
        tempDiv.scrollTop = scrollTop;
    }
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