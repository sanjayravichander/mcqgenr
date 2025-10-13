# 🎓 MCQ Generator

### Intelligent Multiple Choice Question Generator powered by AI

![Version](https://img.shields.io/badge/version-0.0.1-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-green.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)
![Build](https://img.shields.io/badge/build-passing-brightgreen.svg)
![LangChain](https://img.shields.io/badge/LangChain-enabled-purple.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5-turbo-red.svg)

---

## 📋 Table of Contents

- [Project Description](#-project-description)
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [API Documentation](#-api-documentation)
- [Configuration and Customization](#-configuration-and-customization)
- [Examples and Tutorials](#-examples-and-tutorials)
- [Architecture and Technical Details](#-architecture-and-technical-details)
- [Troubleshooting and FAQ](#-troubleshooting-and-faq)
- [Contributing Guidelines](#-contributing-guidelines)
- [Testing Information](#-testing-information)
- [Deployment Guide](#-deployment-guide)
- [Changelog and Versioning](#-changelog-and-versioning)
- [License and Legal](#-license-and-legal)
- [Acknowledgments and Credits](#-acknowledgments-and-credits)
- [Contact and Support](#-contact-and-support)
- [Additional Resources](#-additional-resources)

---

## 📖 Project Description

### Overview

The **MCQ Generator** is an advanced AI-powered application that automatically generates high-quality multiple-choice questions (MCQs) from text documents and PDF files. Leveraging the power of OpenAI's GPT-3.5-turbo model through LangChain, this tool transforms educational content into comprehensive quizzes with minimal effort.

### Target Audience

- **Educators and Teachers**: Create quick assessments for students
- **Content Creators**: Generate quiz content for educational platforms
- **Students**: Practice with custom-generated questions from study materials
- **Corporate Trainers**: Develop training assessments efficiently
- **EdTech Companies**: Integrate intelligent quiz generation into their platforms

### Key Benefits and Value Proposition

✅ **Time-Saving**: Generate multiple MCQs in seconds instead of hours  
✅ **AI-Powered Quality**: Leverages advanced language models for contextually relevant questions  
✅ **Customizable Complexity**: Adjust difficulty levels to match your audience  
✅ **Subject Flexibility**: Works across all subjects and domains  
✅ **Multiple Formats**: Supports both PDF and text file inputs  
✅ **Quality Review**: Built-in evaluation chain ensures question quality  
✅ **User-Friendly Interface**: Simple Streamlit web interface requires no coding knowledge  
✅ **Cost Tracking**: Monitor OpenAI API usage and costs in real-time

---

## ✨ Features

### Core Features

#### 🤖 Intelligent Question Generation
- **AI-Powered MCQ Creation**: Uses OpenAI's GPT-3.5-turbo model to generate contextually accurate questions
- **Customizable Question Count**: Generate anywhere from 3 to 50 MCQs per session
- **Subject-Specific Questions**: Tailor questions to specific subjects or topics
- **Complexity Control**: Adjust question difficulty with tone settings (Simple, Medium, Complex)

#### 📄 Document Processing
- **PDF Support**: Extract and process text from PDF documents
- **Text File Support**: Process plain text files (.txt)
- **Automatic Text Extraction**: Seamless extraction from uploaded documents
- **Multi-Page PDF Handling**: Process documents of any length

#### 🎯 Quality Assurance
- **Automated Question Review**: Built-in evaluation chain assesses question quality
- **Complexity Analysis**: AI evaluates if questions match the target audience
- **Duplicate Prevention**: Ensures no repeated questions in the generated set
- **Text Conformity Check**: Validates questions align with source material

### Advanced Features

#### 📊 Interactive Web Interface
- **Streamlit-Based UI**: Clean, intuitive interface for all users
- **Real-Time Generation**: See questions generated in real-time
- **File Upload**: Drag-and-drop file uploading
- **Form Validation**: Ensures all required fields are completed

#### 💰 Cost Tracking
- **Token Usage Monitoring**: Track OpenAI API token consumption
- **Cost Calculation**: Real-time cost estimation for each generation
- **Callback Integration**: Detailed breakdown of prompt and completion tokens

#### 📈 Data Visualization
- **Tabular Display**: Generated MCQs displayed in clean, readable tables
- **Formatted Output**: Structured display of questions, options, and correct answers
- **Review Section**: Dedicated area for AI-generated quality reviews

### Export Options

#### 📥 Output Formats
- **Interactive Tables**: View questions in formatted tables with pandas DataFrames
- **JSON Format**: Structured JSON output for programmatic access
- **CSV Export**: Export questions for use in other applications
- **Text Review**: Plain text analysis and recommendations

---

## 🚀 Installation

### System Requirements

#### Prerequisites
- **Python**: Version 3.8 or higher
- **Operating System**: Windows, macOS, or Linux
- **Memory**: Minimum 4GB RAM recommended
- **Internet Connection**: Required for OpenAI API access

#### Required Accounts
- **OpenAI API Key**: Required for question generation ([Get one here](https://platform.openai.com/api-keys))

### Installation Methods

#### Method 1: Standard Installation (Recommended)

1. **Clone the Repository**
```bash
git clone https://github.com/sanjayravichander/mcqgenr.git
cd mcqgenr
```

2. **Create Virtual Environment**
```bash
# On Windows
python -m venv env39
env39\Scripts\activate

# On macOS/Linux
python3 -m venv env39
source env39/bin/activate
```

3. **Install Dependencies**
```bash
pip install -r Requirements.txt
```

4. **Set Up Environment Variables**
```bash
# Create a .env file in the project root
echo "OPENAI_API_KEY=your_api_key_here" > .env
```

#### Method 2: Development Installation

```bash
# Clone and navigate
git clone https://github.com/sanjayravichander/mcqgenr.git
cd mcqgenr

# Install in editable mode
pip install -e .
```

#### Method 3: Docker Installation (Coming Soon)

Docker support is planned for future releases.

### Verification Steps

1. **Verify Installation**
```bash
python test.py
```
Expected output: Log file created in `logs/` directory

2. **Check Dependencies**
```bash
pip list | grep -E "openai|langchain|streamlit"
```

3. **Test Application Launch**
```bash
streamlit run StreamlitApp.py
```
Expected: Browser opens to `http://localhost:8501`

---

## 📚 Usage

### Quick Start Guide

#### Basic Usage

1. **Launch the Application**
```bash
streamlit run StreamlitApp.py
```

2. **Access the Web Interface**
- Open your browser to `http://localhost:8501`
- The MCQ Generator interface will load

3. **Generate Your First Quiz**
   - Upload a PDF or text file (sample: `data.txt` included)
   - Set the number of MCQs (3-50)
   - Specify the subject (e.g., "Machine Learning")
   - Set complexity level (e.g., "Simple")
   - Click "Create MCQs"

4. **View Results**
   - Generated questions appear in a formatted table
   - Review the AI's quality assessment
   - Questions include options and correct answers

### Advanced Usage Scenarios

#### Scenario 1: Academic Assessment Creation

```python
# Configuration for university-level exam
Number of MCQs: 25
Subject: "Quantum Physics"
Complexity Level: "Advanced"
```

#### Scenario 2: Corporate Training Quiz

```python
# Configuration for employee training
Number of MCQs: 15
Subject: "Workplace Safety"
Complexity Level: "Simple"
```

#### Scenario 3: Student Self-Assessment

```python
# Configuration for study practice
Number of MCQs: 10
Subject: "Biology"
Complexity Level: "Medium"
```

### Command-Line Interface Documentation

Currently, the application uses a web interface. CLI support is planned for future releases.

### Web Interface Walkthrough

#### Step-by-Step Guide

1. **File Upload Section**
   - Click "Browse files" or drag-and-drop
   - Supported formats: .pdf, .txt
   - Maximum file size: Limited by browser

2. **Configuration Panel**
   - **Number of MCQs**: Use slider or input box (3-50 range)
   - **Subject**: Text input, max 20 characters
   - **Complexity Level**: Text input, max 20 characters (e.g., "Simple", "Medium", "Complex")

3. **Generation Process**
   - Click "Create MCQs" button
   - Loading spinner indicates processing
   - Wait time varies based on document size and question count

4. **Results Display**
   - **Questions Table**: MCQ, Choices, Correct Answer
   - **Review Section**: AI-generated quality feedback
   - **Error Messages**: Displayed if issues occur

### Configuration Options and Customization

#### Environment Variables

Create a `.env` file with the following:

```bash
# Required
OPENAI_API_KEY=sk-your-api-key-here

# Optional (future use)
OPENAI_MODEL=gpt-3.5-turbo
TEMPERATURE=0.5
MAX_TOKENS=2000
```

#### Application Settings

Modify `StreamlitApp.py` for customizations:

```python
# Change response JSON path
RESPONSE_JSON_PATH = "response.json"

# Adjust logging level
logging.basicConfig(level=logging.INFO)  # Change to DEBUG for verbose

# Modify model parameters in MCQgenerator.py
temperature=0.5  # Adjust creativity (0.0-1.0)
model_name="gpt-3.5-turbo"  # Change model
```

---

## 🔌 API Documentation

### Core Modules

#### MCQgenerator Module

**Location**: `src/mcqgenerator/MCQgenerator.py`

##### `generate_eval_chain(inputs)`

Main function to generate and evaluate MCQs.

**Parameters**:
```python
{
    "text": str,              # Source text content
    "number": int,            # Number of MCQs (3-50)
    "subject": str,           # Subject area
    "tone": str,              # Complexity level
    "response_json": str      # JSON template for response format
}
```

**Returns**:
```python
{
    "quiz": str,      # JSON string of generated MCQs
    "review": str     # Quality assessment text
}
```

**Example**:
```python
from src.mcqgenerator.MCQgenerator import generate_eval_chain
import json

with open("response.json", 'r') as file:
    RESPONSE_JSON = json.load(file)

response = generate_eval_chain({
    "text": "Your content here...",
    "number": 5,
    "subject": "Machine Learning",
    "tone": "Simple",
    "response_json": json.dumps(RESPONSE_JSON)
})

quiz_data = json.loads(response["quiz"])
review_text = response["review"]
```

#### Utils Module

**Location**: `src/mcqgenerator/utils.py`

##### `read_file(file)`

Reads content from uploaded files.

**Parameters**:
- `file`: File object from Streamlit uploader

**Returns**: String containing file content

**Supported Formats**: .pdf, .txt

**Example**:
```python
from src.mcqgenerator.utils import read_file

text = read_file(uploaded_file)
```

##### `get_table_data(quiz_str)`

Converts quiz JSON string to table format.

**Parameters**:
- `quiz_str`: JSON string of quiz data

**Returns**: List of dictionaries with MCQ, Choices, Correct keys

**Example**:
```python
from src.mcqgenerator.utils import get_table_data
import pandas as pd

table_data = get_table_data(quiz_json_string)
df = pd.DataFrame(table_data)
```

### Authentication Details

Authentication is handled through environment variables:

```bash
# Set your OpenAI API key
export OPENAI_API_KEY="sk-your-key-here"

# Or use .env file (recommended)
OPENAI_API_KEY=sk-your-key-here
```

### Rate Limiting Information

#### OpenAI API Limits

- **Free Tier**: Limited requests per minute
- **Pay-as-you-go**: Higher rate limits based on usage
- **Token Limits**: GPT-3.5-turbo supports up to 4,096 tokens per request

#### Cost Considerations

Average costs per generation:
- 10 MCQs: ~$0.002-0.005
- 25 MCQs: ~$0.005-0.010
- 50 MCQs: ~$0.010-0.020

Costs vary based on document length and complexity.

---

## ⚙️ Configuration and Customization

### Configuration File Examples

#### response.json Template

The `response.json` file defines the structure for generated MCQs:

```json
{
    "1": {
        "mcq": "multiple choice question",
        "options": {
            "a": "choice here",
            "b": "choice here",
            "c": "choice here",
            "d": "choice here"
        },
        "correct": "correct answer"
    }
}
```

**Customization Options**:
- Add more option keys (e, f, etc.)
- Modify field names (must update utils.py accordingly)
- Change numbering scheme

### Environment Variables

Complete `.env` file example:

```bash
# OpenAI Configuration
OPENAI_API_KEY=sk-your-api-key-here

# Model Settings (optional - defaults shown)
OPENAI_MODEL=gpt-3.5-turbo
TEMPERATURE=0.5

# SSL Configuration (for corporate environments)
SSL_CERT_FILE=/path/to/certifi/cacert.pem

# Logging Configuration
LOG_LEVEL=INFO
```

### Customization Options

#### Prompt Customization

Edit `src/mcqgenerator/MCQgenerator.py`:

```python
# Customize the MCQ generation prompt
TEMPLATE="""
Text:{text}
You are an expert MCQ maker. Given the above text, create a quiz of {number} 
multiple choice questions for {subject} students in {tone} tone.

[Your custom instructions here]

### RESPONSE_JSON
{response_json}
"""
```

#### Review Chain Customization

```python
# Customize the evaluation prompt
TEMPLATE2="""
You are an expert evaluator. Analyze the quiz for {subject} students.
[Your custom evaluation criteria here]

Quiz_MCQs:
{quiz}
"""
```

### Themes and Styling

#### Streamlit Themes

Create `.streamlit/config.toml`:

```toml
[theme]
primaryColor="#FF6B6B"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="sans serif"
```

#### Custom CSS

Add to `StreamlitApp.py`:

```python
st.markdown("""
<style>
    .main {
        background-color: #f5f5f5;
    }
    h1 {
        color: #2E86AB;
    }
</style>
""", unsafe_allow_html=True)
```

---

## 💡 Examples and Tutorials

### Basic Usage Examples

#### Example 1: Simple Quiz Generation

```python
# Using the Streamlit interface:
# 1. Upload data.txt (included in repo)
# 2. Set parameters:
#    - Number: 5
#    - Subject: Machine Learning
#    - Tone: Simple
# 3. Click "Create MCQs"

# Expected Output:
# 5 MCQs about Machine Learning basics
# AI review confirming appropriate complexity
```

#### Example 2: Custom Text Processing

```python
from src.mcqgenerator.MCQgenerator import generate_eval_chain
import json

# Load template
with open("response.json", 'r') as file:
    RESPONSE_JSON = json.load(file)

# Your custom text
custom_text = """
Python is a high-level programming language...
[Your content]
"""

# Generate MCQs
response = generate_eval_chain({
    "text": custom_text,
    "number": 10,
    "subject": "Python Programming",
    "tone": "Intermediate",
    "response_json": json.dumps(RESPONSE_JSON)
})

# Parse results
quiz = json.loads(response["quiz"])
for key, question in quiz.items():
    print(f"Q{key}: {question['mcq']}")
    print(f"Answer: {question['correct']}\n")
```

### Advanced Use Cases

#### Use Case 1: Batch Processing Multiple Documents

```python
import os
from src.mcqgenerator.utils import read_file
from src.mcqgenerator.MCQgenerator import generate_eval_chain

# Process multiple files
for filename in os.listdir("documents/"):
    if filename.endswith(".txt"):
        with open(f"documents/{filename}", 'rb') as file:
            text = file.read().decode('utf-8')
            
            response = generate_eval_chain({
                "text": text,
                "number": 15,
                "subject": filename.replace(".txt", ""),
                "tone": "Medium",
                "response_json": json.dumps(RESPONSE_JSON)
            })
            
            # Save results
            with open(f"output/{filename}_quiz.json", 'w') as output:
                json.dump(response, output, indent=2)
```

#### Use Case 2: Integration with Learning Management System

```python
def generate_quiz_for_lms(course_material, course_name):
    """
    Generate quiz compatible with LMS import formats
    """
    from src.mcqgenerator.MCQgenerator import generate_eval_chain
    
    response = generate_eval_chain({
        "text": course_material,
        "number": 20,
        "subject": course_name,
        "tone": "Medium",
        "response_json": json.dumps(RESPONSE_JSON)
    })
    
    # Convert to LMS format (e.g., Moodle XML)
    quiz_data = json.loads(response["quiz"])
    lms_xml = convert_to_moodle_xml(quiz_data)
    
    return lms_xml
```

### Integration Examples

#### Integration with Flask API

```python
from flask import Flask, request, jsonify
from src.mcqgenerator.MCQgenerator import generate_eval_chain
import json

app = Flask(__name__)

@app.route('/generate-mcqs', methods=['POST'])
def generate_mcqs():
    data = request.json
    
    response = generate_eval_chain({
        "text": data['text'],
        "number": data['number'],
        "subject": data['subject'],
        "tone": data['tone'],
        "response_json": json.dumps(RESPONSE_JSON)
    })
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
```

### Best Practices

#### 1. Text Preparation
- **Clean Input**: Remove special characters and formatting
- **Optimal Length**: 500-2000 words works best
- **Clear Content**: Well-structured source material produces better questions

#### 2. Question Count Guidelines
- **Short texts (< 500 words)**: 3-10 MCQs
- **Medium texts (500-1500 words)**: 10-25 MCQs
- **Long texts (> 1500 words)**: 25-50 MCQs

#### 3. Subject and Tone Specification
- **Be Specific**: Use detailed subjects ("Quantum Mechanics" vs "Physics")
- **Consistent Tone**: Use standard descriptors (Simple, Medium, Complex, Advanced)
- **Match Audience**: Align complexity with target learners

#### 4. API Usage Optimization
- **Batch Processing**: Process multiple small documents together
- **Cache Results**: Store generated quizzes to avoid regeneration
- **Monitor Costs**: Use callback tracking to stay within budget

---

## 🏗️ Architecture and Technical Details

### System Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                     Streamlit Web Interface                  │
│                      (StreamlitApp.py)                       │
└────────────────────┬───────────────────────────────┬─────────┘
                     │                               │
                     ▼                               ▼
         ┌───────────────────┐           ┌──────────────────┐
         │   Utils Module    │           │  Logger Module   │
         │   (utils.py)      │           │  (logger.py)     │
         │  - read_file()    │           │  - Log tracking  │
         │  - get_table_data()│          └──────────────────┘
         └─────────┬─────────┘
                   │
                   ▼
         ┌───────────────────────────────┐
         │    MCQ Generator Module       │
         │    (MCQgenerator.py)          │
         │                               │
         │  ┌─────────────────────────┐  │
         │  │  Quiz Generation Chain  │  │
         │  │  (LLMChain)            │  │
         │  └──────────┬──────────────┘  │
         │             │                 │
         │             ▼                 │
         │  ┌─────────────────────────┐  │
         │  │  Quiz Evaluation Chain  │  │
         │  │  (LLMChain)            │  │
         │  └──────────┬──────────────┘  │
         │             │                 │
         │  ┌──────────▼──────────────┐  │
         │  │   Sequential Chain      │  │
         │  │   (Combines both)       │  │
         │  └─────────────────────────┘  │
         └───────────┬───────────────────┘
                     │
                     ▼
         ┌───────────────────────┐
         │   OpenAI API          │
         │   (GPT-3.5-turbo)     │
         └───────────────────────┘
```

### Technology Stack

#### Core Technologies

| Technology | Version | Purpose |
|------------|---------|---------|
| Python | 3.8+ | Primary programming language |
| Streamlit | Latest | Web interface framework |
| LangChain | Latest | LLM orchestration framework |
| OpenAI API | GPT-3.5-turbo | Language model for generation |

#### Key Dependencies

```python
# AI/ML Libraries
openai              # OpenAI API client
langchain           # LLM framework
langchain_community # Community integrations

# Document Processing
PyPDF2              # PDF parsing

# Web Framework
streamlit           # Web interface

# Utilities
python-dotenv       # Environment management
pandas              # Data manipulation
certifi             # SSL certificates
httpx               # HTTP client
```

### Dependencies Explanation

#### LangChain Framework
- **PromptTemplate**: Structures prompts for consistent output
- **LLMChain**: Manages single LLM call sequences
- **SequentialChain**: Chains multiple LLM calls together
- **ChatOpenAI**: Wrapper for OpenAI's chat models

#### Document Processing Pipeline
1. **File Upload**: Streamlit file uploader widget
2. **Format Detection**: Check file extension (.pdf or .txt)
3. **Content Extraction**: 
   - PDF: PyPDF2.PdfReader
   - TXT: Direct UTF-8 decoding
4. **Text Cleaning**: Normalize and prepare for LLM

#### LLM Processing Chain
1. **Quiz Generation**:
   - Input: Source text + parameters
   - Process: GPT-3.5-turbo generates MCQs
   - Output: JSON-formatted quiz

2. **Quiz Evaluation**:
   - Input: Generated quiz + subject
   - Process: GPT-3.5-turbo evaluates quality
   - Output: Review text with recommendations

### Performance Considerations

#### Optimization Strategies

1. **Token Management**
   - Average token usage: 1500-2000 per generation
   - Cost per 1K tokens: ~$0.0015-0.002
   - Optimize prompt length to reduce costs

2. **Response Time**
   - PDF processing: 1-3 seconds
   - LLM generation: 5-15 seconds
   - Total time: 6-18 seconds for typical request

3. **Concurrent Processing**
   - Single-threaded by default
   - Can implement async processing for batch jobs
   - Consider queue system for high-volume usage

4. **Caching Strategies**
   - Cache OpenAI responses for identical inputs
   - Store processed documents to avoid re-parsing
   - Implement result database for common queries

#### Scalability Considerations

- **Horizontal Scaling**: Deploy multiple Streamlit instances behind load balancer
- **API Rate Limits**: Implement request queuing and retry logic
- **Database Integration**: Store generated quizzes for reuse
- **CDN Integration**: Cache static assets and common results

---

## 🔧 Troubleshooting and FAQ

### Common Issues and Solutions

#### Issue 1: OpenAI API Key Error

**Error Message**:
```
openai.error.AuthenticationError: Incorrect API key provided
```

**Solutions**:
1. Verify API key in `.env` file
2. Check for leading/trailing spaces
3. Ensure `.env` file is in project root
4. Reload environment variables:
```bash
source .env  # Linux/Mac
# or restart application
```

#### Issue 2: SSL Certificate Verification Failed

**Error Message**:
```
ssl.SSLCertVerificationError: certificate verify failed
```

**Solutions**:
1. Update certifi package:
```bash
pip install --upgrade certifi
```

2. Set certificate path in code (already implemented):
```python
import certifi
os.environ['SSL_CERT_FILE'] = certifi.where()
```

3. For corporate networks, use custom certificate:
```bash
export SSL_CERT_FILE=/path/to/your/certificate.pem
```

#### Issue 3: PDF Parsing Errors

**Error Message**:
```
Exception: error loading the pdf file
```

**Solutions**:
1. Verify PDF is not corrupted
2. Ensure PDF has extractable text (not scanned image)
3. Try converting PDF to text using online tools first
4. Check PyPDF2 version:
```bash
pip install --upgrade PyPDF2
```

#### Issue 4: Response Format Errors

**Error Message**:
```
Error in the table data
```

**Solutions**:
1. Check `response.json` format is correct
2. Verify OpenAI response contains valid JSON
3. Increase temperature for more creative responses
4. Review logs in `logs/` directory for details

#### Issue 5: Streamlit Port Already in Use

**Error Message**:
```
OSError: [Errno 98] Address already in use
```

**Solutions**:
```bash
# Find and kill process using port 8501
lsof -ti:8501 | xargs kill -9

# Or use different port
streamlit run StreamlitApp.py --server.port 8502
```

### Error Messages and Fixes

| Error | Cause | Fix |
|-------|-------|-----|
| `ModuleNotFoundError: No module named 'langchain'` | Dependencies not installed | Run `pip install -r Requirements.txt` |
| `FileNotFoundError: response.json` | Missing template file | Ensure `response.json` exists in project root |
| `KeyError: 'quiz'` | Invalid response structure | Check OpenAI API response format |
| `ValueError: Number of MCQs must be between 3 and 50` | Invalid input range | Adjust MCQ count in UI |

### Performance Optimization Tips

#### 1. Reduce API Costs
```python
# Use shorter, focused text excerpts
# Example: Extract key paragraphs instead of entire document
def extract_key_sections(text, max_length=1000):
    sentences = text.split('.')
    return '.'.join(sentences[:max_length])
```

#### 2. Improve Response Time
```python
# Reduce temperature for faster, more deterministic responses
llm = ChatOpenAI(
    openai_api_key=KEY,
    model_name="gpt-3.5-turbo",
    temperature=0.3  # Lower = faster
)
```

#### 3. Optimize Token Usage
- Keep subject and tone descriptions concise
- Use response.json as compact as possible
- Remove unnecessary whitespace from prompts

### Frequently Asked Questions

#### Q1: How much does it cost to generate MCQs?

**A**: Costs vary based on document length:
- Small documents (< 500 words): $0.001-0.003
- Medium documents (500-1500 words): $0.003-0.008
- Large documents (> 1500 words): $0.008-0.020

#### Q2: Can I use GPT-4 instead of GPT-3.5-turbo?

**A**: Yes, modify `MCQgenerator.py`:
```python
llm = ChatOpenAI(
    openai_api_key=KEY,
    model_name="gpt-4",  # Change here
    temperature=0.5
)
```
Note: GPT-4 is more expensive but produces higher quality questions.

#### Q3: What's the maximum document size?

**A**: 
- PDF: Limited by OpenAI token limits (~4096 tokens = ~3000 words)
- TXT: Same limitation applies
- For larger documents, split into sections

#### Q4: Can I generate questions in languages other than English?

**A**: Yes, GPT-3.5-turbo supports multiple languages. Provide source text in your target language.

#### Q5: How do I ensure questions are not duplicated across sessions?

**A**: Implement a deduplication system:
```python
import hashlib

def hash_question(question):
    return hashlib.md5(question.encode()).hexdigest()

# Store hashes and check before using
```

#### Q6: Can I customize the number of options per question?

**A**: Yes, modify `response.json`:
```json
{
    "options": {
        "a": "choice",
        "b": "choice",
        "c": "choice",
        "d": "choice",
        "e": "choice"  // Add more options
    }
}
```

#### Q7: How do I export questions to different formats?

**A**: Add export functionality:
```python
def export_to_csv(quiz_data, filename):
    df = pd.DataFrame(quiz_data)
    df.to_csv(filename, index=False)

def export_to_json(quiz_data, filename):
    with open(filename, 'w') as f:
        json.dump(quiz_data, f, indent=2)
```

#### Q8: Can I run this offline?

**A**: No, internet connection is required for OpenAI API access. Consider using local LLMs (e.g., LLaMA, Mistral) for offline usage.

#### Q9: How accurate are the generated questions?

**A**: Accuracy depends on:
- Source material quality (clear, factual content = better questions)
- Subject complexity (simpler topics = more accurate)
- Model configuration (lower temperature = more factual)

#### Q10: Can I integrate this with my existing LMS?

**A**: Yes, you can create API endpoints or export to standard formats (SCORM, QTI, Moodle XML). See integration examples in the Examples section.

---

## 🤝 Contributing Guidelines

We welcome contributions from the community! Here's how you can help improve the MCQ Generator project.

### How to Contribute

#### Types of Contributions

1. **Bug Reports**: Found a bug? Let us know!
2. **Feature Requests**: Have an idea? We'd love to hear it!
3. **Code Contributions**: Submit pull requests for fixes or enhancements
4. **Documentation**: Improve or translate documentation
5. **Testing**: Help test new features and report issues

### Development Setup

#### 1. Fork and Clone

```bash
# Fork the repository on GitHub
# Then clone your fork
git clone https://github.com/YOUR_USERNAME/mcqgenr.git
cd mcqgenr
```

#### 2. Create Development Environment

```bash
# Create virtual environment
python -m venv env39
source env39/bin/activate  # or env39\Scripts\activate on Windows

# Install in development mode
pip install -e .
pip install -r Requirements.txt
```

#### 3. Create Feature Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b bugfix/issue-number-description
```

### Coding Standards

#### Python Style Guide

Follow PEP 8 guidelines:

```python
# Good
def generate_quiz(text, number_of_questions, subject):
    """
    Generate MCQs from text content.
    
    Args:
        text (str): Source text content
        number_of_questions (int): Number of MCQs to generate
        subject (str): Subject area
        
    Returns:
        dict: Generated quiz data
    """
    # Implementation
    pass

# Avoid
def genQuiz(t,n,s):
    # No docstring, unclear variable names
    pass
```

#### Code Quality Requirements

1. **Docstrings**: All functions must have docstrings
2. **Type Hints**: Use type hints where appropriate
3. **Comments**: Add comments for complex logic
4. **Error Handling**: Implement proper try-except blocks
5. **Logging**: Use the logger module for debugging

#### File Organization

```
mcqgenr/
├── src/
│   └── mcqgenerator/
│       ├── __init__.py
│       ├── MCQgenerator.py    # Core generation logic
│       ├── utils.py            # Utility functions
│       └── logger.py           # Logging configuration
├── tests/                      # Test files (future)
├── experiment/                 # Jupyter notebooks
├── docs/                       # Additional documentation (future)
└── StreamlitApp.py            # Main application
```

### Pull Request Process

#### Step 1: Make Your Changes

```bash
# Make changes to files
# Test your changes locally
streamlit run StreamlitApp.py
```

#### Step 2: Commit Your Changes

```bash
# Stage changes
git add .

# Commit with descriptive message
git commit -m "feat: Add support for DOCX files"
# or
git commit -m "fix: Resolve SSL certificate issue #123"
```

#### Commit Message Convention

Use conventional commits:
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes (formatting)
- `refactor:` Code refactoring
- `test:` Adding tests
- `chore:` Maintenance tasks

#### Step 3: Push and Create PR

```bash
# Push to your fork
git push origin feature/your-feature-name

# Create Pull Request on GitHub
# Fill out the PR template with:
# - Description of changes
# - Related issue number
# - Testing performed
# - Screenshots (if UI changes)
```

#### Step 4: Code Review

- Respond to reviewer feedback
- Make requested changes
- Push updates to the same branch
- PR will auto-update

### Issue Reporting Guidelines

#### Bug Reports

Use this template:

```markdown
**Bug Description**
Clear description of the bug

**Steps to Reproduce**
1. Step one
2. Step two
3. Step three

**Expected Behavior**
What should happen

**Actual Behavior**
What actually happens

**Environment**
- OS: [e.g., Windows 10, macOS 12, Ubuntu 20.04]
- Python Version: [e.g., 3.9.7]
- Package Versions: [run `pip list`]

**Screenshots**
If applicable

**Additional Context**
Any other relevant information
```

#### Feature Requests

```markdown
**Feature Description**
Clear description of the proposed feature

**Use Case**
Why is this feature needed?

**Proposed Solution**
How should it work?

**Alternatives Considered**
Other approaches you've thought about

**Additional Context**
Any other relevant information
```

### Development Guidelines

#### Adding New Features

1. **Discuss First**: Open an issue to discuss major changes
2. **Small PRs**: Keep pull requests focused and small
3. **Tests**: Add tests for new functionality (when test infrastructure exists)
4. **Documentation**: Update README and inline docs
5. **Backward Compatibility**: Maintain compatibility when possible

#### Code Review Checklist

Before submitting PR, ensure:
- [ ] Code follows PEP 8 style guide
- [ ] All functions have docstrings
- [ ] No hardcoded credentials or API keys
- [ ] Error handling is implemented
- [ ] Logging statements are appropriate
- [ ] README is updated if needed
- [ ] Code is tested locally
- [ ] Commit messages are clear

---

## 🧪 Testing Information

### Current Testing Status

The project currently uses manual testing through the Streamlit interface. Automated test infrastructure is planned for future releases.

### Manual Testing Guide

#### How to Test the Application

1. **Launch Application**
```bash
streamlit run StreamlitApp.py
```

2. **Test Case 1: Basic MCQ Generation**
   - Upload `data.txt`
   - Set: 5 MCQs, "Machine Learning", "Simple"
   - Verify: 5 questions generated with options and answers

3. **Test Case 2: PDF Processing**
   - Upload a PDF file
   - Set appropriate parameters
   - Verify: Text extracted and MCQs generated

4. **Test Case 3: Edge Cases**
   - Test minimum MCQs (3)
   - Test maximum MCQs (50)
   - Test with very short text
   - Test with very long text

5. **Test Case 4: Error Handling**
   - Try without uploading file
   - Try with unsupported file format
   - Verify appropriate error messages

### Testing Guidelines for Contributors

When contributing, please test:

1. **Functionality**: Does the feature work as intended?
2. **Error Cases**: How does it handle invalid input?
3. **Edge Cases**: Test boundary conditions
4. **Integration**: Does it work with existing features?
5. **Performance**: Is response time acceptable?

### Future Test Infrastructure

Planned testing framework:

```python
# tests/test_mcqgenerator.py (future)
import pytest
from src.mcqgenerator.MCQgenerator import generate_eval_chain

def test_quiz_generation():
    """Test basic quiz generation"""
    response = generate_eval_chain({
        "text": "Sample text here",
        "number": 5,
        "subject": "Test Subject",
        "tone": "Simple",
        "response_json": "{}"
    })
    
    assert "quiz" in response
    assert "review" in response

def test_invalid_input():
    """Test error handling for invalid input"""
    with pytest.raises(Exception):
        generate_eval_chain({
            "text": "",
            "number": 0,
            "subject": "",
            "tone": ""
        })
```

### Running Tests (Future)

```bash
# Install test dependencies
pip install pytest pytest-cov

# Run tests
pytest tests/

# Run with coverage
pytest --cov=src tests/

# Generate coverage report
pytest --cov=src --cov-report=html tests/
```

---

## 🚀 Deployment Guide

### Production Deployment Instructions

#### Option 1: Streamlit Cloud (Recommended for Quick Deployment)

1. **Prepare Repository**
```bash
# Ensure all files are committed
git add .
git commit -m "Prepare for deployment"
git push origin main
```

2. **Deploy to Streamlit Cloud**
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select repository: `sanjayravichander/mcqgenr`
   - Main file path: `StreamlitApp.py`
   - Add secrets: `OPENAI_API_KEY=your_key`
   - Click "Deploy"

3. **Configure Secrets**
   - In Streamlit Cloud dashboard
   - Go to Settings > Secrets
   - Add:
```toml
OPENAI_API_KEY = "sk-your-api-key-here"
```

#### Option 2: Local Server Deployment

```bash
# Install dependencies
pip install -r Requirements.txt

# Set environment variables
export OPENAI_API_KEY="your-key-here"

# Run on specific port
streamlit run StreamlitApp.py --server.port 8080

# Run on specific address
streamlit run StreamlitApp.py --server.address 0.0.0.0
```

#### Option 3: Docker Deployment (Future)

```dockerfile
# Dockerfile (example for future implementation)
FROM python:3.9-slim

WORKDIR /app

COPY Requirements.txt .
RUN pip install -r Requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "StreamlitApp.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

```bash
# Build and run
docker build -t mcqgenr .
docker run -p 8501:8501 -e OPENAI_API_KEY=your_key mcqgenr
```

#### Option 4: AWS EC2 Deployment

```bash
# On EC2 instance
sudo apt update
sudo apt install python3-pip

# Clone repository
git clone https://github.com/sanjayravichander/mcqgenr.git
cd mcqgenr

# Install dependencies
pip3 install -r Requirements.txt

# Set environment variables
echo "OPENAI_API_KEY=your_key" >> .env

# Run with nohup for background execution
nohup streamlit run StreamlitApp.py --server.port 8501 &
```

### Environment Setup

#### Production Environment Variables

Create `.env` file:
```bash
# Required
OPENAI_API_KEY=sk-your-production-key

# Optional Configuration
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
LOG_LEVEL=INFO

# Security
STREAMLIT_SERVER_ENABLE_CORS=false
STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION=true
```

### Security Considerations

#### 1. API Key Protection

```python
# Never commit API keys
# Always use environment variables
# Use .gitignore to exclude .env files

# .gitignore
.env
*.key
secrets/
```

#### 2. Input Validation

```python
# Implement input sanitization
def sanitize_input(text):
    # Remove potentially harmful characters
    import re
    return re.sub(r'[^\w\s.,!?-]', '', text)
```

#### 3. Rate Limiting

```python
# Implement rate limiting for API calls
from functools import lru_cache
import time

@lru_cache(maxsize=100)
def cached_generate(text_hash, number, subject, tone):
    return generate_eval_chain(...)
```

#### 4. HTTPS Configuration

```bash
# For production, use HTTPS
# Configure reverse proxy (nginx/Apache)
# Or use Streamlit Cloud's built-in HTTPS
```

### Performance Tuning

#### 1. Optimize Streamlit

```python
# .streamlit/config.toml
[server]
maxUploadSize = 10  # Limit file size to 10MB
enableCORS = false
enableXsrfProtection = true

[browser]
gatherUsageStats = false

[runner]
magicEnabled = false
```

#### 2. Caching Strategy

```python
import streamlit as st

@st.cache_data
def load_response_json():
    with open("response.json", 'r') as file:
        return json.load(file)

@st.cache_resource
def get_llm_instance():
    return ChatOpenAI(...)
```

#### 3. Resource Optimization

```bash
# Use gunicorn for production (if converting to Flask)
gunicorn -w 4 -b 0.0.0.0:8501 app:app

# Monitor resource usage
pip install psutil
```

### Monitoring and Logging

#### Production Logging

```python
# Enhanced logging for production
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/production.log'),
        logging.StreamHandler()
    ]
)
```

#### Health Checks

```python
# Add health check endpoint (for future API version)
@app.route('/health')
def health_check():
    return {"status": "healthy", "timestamp": datetime.now()}
```

---

## 📝 Changelog and Versioning

### Version History

#### Version 0.0.1 (Current)
**Release Date**: 2025-10-13

**Initial Release Features**:
- ✅ AI-powered MCQ generation using GPT-3.5-turbo
- ✅ Support for PDF and text file inputs
- ✅ Streamlit web interface
- ✅ Customizable question count (3-50)
- ✅ Subject and complexity level controls
- ✅ Built-in quality evaluation chain
- ✅ Cost tracking with OpenAI callback
- ✅ Tabular display of generated questions
- ✅ Logging infrastructure

**Known Issues**:
- Response JSON path is hardcoded (Windows-specific)
- Limited to single-file processing
- No export functionality
- Manual testing only

### Release Notes

#### Upcoming Features (Roadmap)

**Version 0.1.0 (Planned)**:
- [ ] Export to multiple formats (CSV, JSON, XML)
- [ ] Batch processing support
- [ ] Docker containerization
- [ ] CLI interface
- [ ] Enhanced error handling
- [ ] Unit test suite
- [ ] CI/CD pipeline

**Version 0.2.0 (Planned)**:
- [ ] Support for DOCX files
- [ ] Multiple LLM backend support (GPT-4, Claude, etc.)
- [ ] Question difficulty analysis
- [ ] Custom prompt templates
- [ ] Database integration for question storage
- [ ] User authentication

**Version 0.3.0 (Planned)**:
- [ ] RESTful API
- [ ] Question bank management
- [ ] Quiz session management
- [ ] Analytics dashboard
- [ ] Multi-language support

### Breaking Changes

No breaking changes yet (initial release).

Future breaking changes will be documented here with migration guides.

### Migration Guides

#### Future: Migrating from 0.0.1 to 0.1.0

When version 0.1.0 is released, migration guide will include:
- Configuration file format changes
- API endpoint updates
- Deprecated feature removals

---

## 📄 License and Legal

### License Information

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2025 Sanjay Ravichander

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### Copyright Details

**Copyright © 2025 Sanjay Ravichander**  
All rights reserved.

### Third-Party Licenses

This project uses the following open-source libraries:

| Library | License | Purpose |
|---------|---------|---------|
| OpenAI Python | MIT | OpenAI API client |
| LangChain | MIT | LLM orchestration |
| Streamlit | Apache 2.0 | Web interface |
| PyPDF2 | BSD 3-Clause | PDF processing |
| python-dotenv | BSD 3-Clause | Environment management |
| pandas | BSD 3-Clause | Data manipulation |

### Attribution Requirements

When using this software:
1. Include the MIT License text
2. Provide attribution to Sanjay Ravichander
3. Keep copyright notices intact

### Disclaimer

This software is provided "as is" without warranty of any kind. The generated MCQs should be reviewed by educators before use in formal assessments.

### OpenAI Usage Compliance

This application uses OpenAI's API and is subject to:
- [OpenAI Terms of Use](https://openai.com/terms/)
- [OpenAI Usage Policies](https://openai.com/policies/usage-policies)

Users are responsible for:
- Maintaining their own API keys
- Complying with OpenAI's usage policies
- Monitoring and managing API costs

---

## 🙏 Acknowledgments and Credits

### Project Creator

**Sanjay Ravichander**  
*AI/ML Enthusiast and Developer*

- Email: sanjay.1991999@gmail.com
- GitHub: [@sanjayravichander](https://github.com/sanjayravichander)
- Project: [mcqgenr](https://github.com/sanjayravichander/mcqgenr)

### Contributors

This is the initial release. Contributors will be listed here as the project grows.

Want to be listed here? Check out our [Contributing Guidelines](#-contributing-guidelines)!

### Third-Party Libraries

Special thanks to the developers and maintainers of:

#### Core Technologies
- **OpenAI**: For providing the GPT-3.5-turbo API
- **LangChain**: For the excellent LLM orchestration framework
- **Streamlit**: For making Python web apps incredibly easy
- **PyPDF2**: For reliable PDF text extraction

#### Supporting Libraries
- **python-dotenv**: Environment variable management
- **pandas**: Data manipulation and display
- **certifi**: SSL certificate handling
- **httpx**: Modern HTTP client

### Inspiration Sources

This project was inspired by:
- The growing need for automated assessment tools in education
- LangChain's powerful prompt engineering capabilities
- The educational technology community's feedback and needs

### Special Thanks

- OpenAI for democratizing access to powerful language models
- The Python community for excellent documentation and support
- Early testers and feedback providers (you know who you are!)

### Educational Resources

Learning resources that helped build this project:
- [LangChain Documentation](https://python.langchain.com/)
- [OpenAI Cookbook](https://github.com/openai/openai-cookbook)
- [Streamlit Documentation](https://docs.streamlit.io/)

---

## 📞 Contact and Support

### Developer Contact Information

**Sanjay Ravichander**

📧 **Email**: [sanjay.1991999@gmail.com](mailto:sanjay.1991999@gmail.com)  
🐙 **GitHub**: [@sanjayravichander](https://github.com/sanjayravichander)  
🔗 **Repository**: [mcqgenr](https://github.com/sanjayravichander/mcqgenr)

### Support Channels

#### GitHub Issues
For bug reports, feature requests, and technical issues:
- [Create an Issue](https://github.com/sanjayravichander/mcqgenr/issues/new)
- Search [Existing Issues](https://github.com/sanjayravichander/mcqgenr/issues)

#### Discussion Forum
For general questions and discussions:
- [GitHub Discussions](https://github.com/sanjayravichander/mcqgenr/discussions) (Coming Soon)

#### Email Support
For direct inquiries:
- Email: sanjay.1991999@gmail.com
- Response time: 24-48 hours typically

### Community Resources

#### Getting Help

1. **Check Documentation**: Most questions are answered in this README
2. **Search Issues**: Someone may have had the same problem
3. **Ask in Discussions**: Community members can help
4. **Open an Issue**: For bugs and feature requests
5. **Email**: For private or urgent matters

#### Response Times

- **Critical Bugs**: 24-48 hours
- **General Issues**: 2-7 days
- **Feature Requests**: Variable
- **Pull Requests**: Reviewed within 1 week

### Bug Reporting

When reporting bugs, please include:
1. Clear description of the issue
2. Steps to reproduce
3. Expected vs actual behavior
4. Environment details (OS, Python version, etc.)
5. Error messages and logs
6. Screenshots if applicable

See [Contributing Guidelines](#-contributing-guidelines) for detailed template.

### Feature Requests

We welcome feature ideas! Please include:
1. Description of the feature
2. Use case and benefits
3. Proposed implementation (if applicable)
4. Any relevant examples

### Security Issues

For security vulnerabilities:
- **DO NOT** create public issues
- Email directly: sanjay.1991999@gmail.com
- Use subject: "SECURITY: MCQ Generator"
- Expect response within 48 hours

---

## 🔗 Additional Resources

### Documentation Links

#### Official Documentation
- [GitHub Repository](https://github.com/sanjayravichander/mcqgenr)
- This README (comprehensive guide)
- [Setup Guide](https://github.com/sanjayravichander/mcqgenr#-installation)
- [Usage Guide](https://github.com/sanjayravichander/mcqgenr#-usage)

#### API Documentation
- [LangChain Docs](https://python.langchain.com/docs/get_started/introduction)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)
- [Streamlit Documentation](https://docs.streamlit.io/)

### Related Projects

#### Similar Tools
- [Quiz Generator AI](https://github.com/topics/quiz-generator)
- [LangChain Examples](https://github.com/langchain-ai/langchain/tree/master/templates)
- [Educational AI Tools](https://github.com/topics/education-ai)

#### Complementary Projects
- **Question Banks**: Store and manage generated questions
- **Quiz Platforms**: Deploy and administer quizzes
- **LMS Integration**: Connect with learning management systems

### External Resources

#### Learning Materials

**LangChain Tutorials**:
- [LangChain Official Tutorials](https://python.langchain.com/docs/tutorials/)
- [LangChain YouTube Channel](https://www.youtube.com/@LangChain)

**OpenAI Resources**:
- [OpenAI Cookbook](https://github.com/openai/openai-cookbook)
- [Best Practices for Prompt Engineering](https://platform.openai.com/docs/guides/prompt-engineering)

**Streamlit Tutorials**:
- [Streamlit Getting Started](https://docs.streamlit.io/get-started)
- [30 Days of Streamlit](https://30days.streamlit.app/)

#### Community Resources

**Forums and Communities**:
- [LangChain Discord](https://discord.gg/langchain)
- [Streamlit Forum](https://discuss.streamlit.io/)
- [r/LangChain](https://www.reddit.com/r/LangChain/)
- [r/OpenAI](https://www.reddit.com/r/OpenAI/)

**AI/ML Education**:
- [Hugging Face Learn](https://huggingface.co/learn)
- [FastAI](https://www.fast.ai/)
- [DeepLearning.AI](https://www.deeplearning.ai/)

### Video Tutorials and Guides

#### Project-Specific Guides
- Video tutorials coming soon!
- Follow the repository for updates

#### General LangChain Tutorials
- [LangChain Crash Course](https://www.youtube.com/results?search_query=langchain+tutorial)
- [Building AI Apps with LangChain](https://www.youtube.com/results?search_query=langchain+streamlit)

### Research Papers and Articles

#### Relevant Research
- [Language Models are Few-Shot Learners (GPT-3 Paper)](https://arxiv.org/abs/2005.14165)
- [Chain-of-Thought Prompting](https://arxiv.org/abs/2201.11903)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

#### Educational Technology
- [AI in Education Research](https://educationaltechnologyjournal.springeropen.com/)
- [Automated Question Generation Papers](https://scholar.google.com/scholar?q=automated+question+generation)

### Tools and Utilities

#### Development Tools
- [VS Code](https://code.visualstudio.com/) - Recommended IDE
- [Jupyter Lab](https://jupyter.org/) - For notebook experimentation
- [Postman](https://www.postman.com/) - API testing (for future API version)

#### Testing and Debugging
- [Python Debugger (pdb)](https://docs.python.org/3/library/pdb.html)
- [Streamlit Debugging](https://docs.streamlit.io/develop/concepts/app-testing)

### Datasets and Examples

#### Sample Educational Content
- Use the included `data.txt` for testing
- [Project Gutenberg](https://www.gutenberg.org/) - Free books for testing
- [Wikipedia API](https://www.mediawiki.org/wiki/API:Main_page) - For generating test content

### Updates and Announcements

#### Stay Updated
- **Watch** the repository on GitHub for updates
- **Star** the project to show support
- Check the [Releases](https://github.com/sanjayravichander/mcqgenr/releases) page

#### Roadmap
- See [Changelog](#-changelog-and-versioning) for upcoming features
- Suggest features via [GitHub Issues](https://github.com/sanjayravichander/mcqgenr/issues)

---

## 🌟 Quick Links

- [Installation](#-installation)
- [Quick Start](#-usage)
- [Troubleshooting](#-troubleshooting-and-faq)
- [Contributing](#-contributing-guidelines)
- [License](#-license-and-legal)
- [Contact](#-contact-and-support)

---

## 📊 Project Stats

![GitHub Repo Stars](https://img.shields.io/github/stars/sanjayravichander/mcqgenr?style=social)
![GitHub Forks](https://img.shields.io/github/forks/sanjayravichander/mcqgenr?style=social)
![GitHub Issues](https://img.shields.io/github/issues/sanjayravichander/mcqgenr)
![GitHub Pull Requests](https://img.shields.io/github/issues-pr/sanjayravichander/mcqgenr)

---

<div align="center">

**Made with ❤️ by Sanjay Ravichander**

*"Empowering Education with AI"*

[⬆ Back to Top](#-mcq-generator)

</div>

---

**Last Updated**: October 13, 2025  
**Version**: 0.0.1  
**Maintainer**: Sanjay Ravichander (sanjay.1991999@gmail.com)
