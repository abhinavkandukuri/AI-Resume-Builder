# AI Resume Builder Agent

An AI-powered Resume Builder Web App developed using Python, Streamlit, and Gemini API.

---

# Features

* AI Resume Generation
* ATS-Friendly Resume Output
* Streamlit Web Interface
* Gemini API Integration
* PDF Resume Download
* Prompt Engineering Workflow
* Beginner-Friendly Agentic AI Project

---

# Tech Stack

## Frontend

* Streamlit

## Backend

* Python

## AI Model

* Gemini API

## Libraries Used

* google-generativeai
* streamlit
* python-dotenv
* fpdf

---

# Project Structure

```text
AI-Resume-Builder/
│
├── venv/
├── main.py
├── app.py
├── resume_agent.py
├── prompt_templates.py
├── .env
└── resume.pdf
```

---

# Step-by-Step Setup

## STEP 1 — Install Python

Download Python:
[https://www.python.org/downloads/](https://www.python.org/downloads/)

Recommended Version:

* Python 3.12.x

During installation:

✅ Enable:

```text
Add Python to PATH
```

---

## STEP 2 — Verify Python Installation

Open terminal and run:

```bash
python --version
```

Check pip:

```bash
pip --version
```

---

## STEP 3 — Install VS Code

Download:
[https://code.visualstudio.com/](https://code.visualstudio.com/)

Install VS Code normally.

---

## STEP 4 — Install VS Code Extensions

Install:

* Python
* Pylance

---

## STEP 5 — Create Project Folder

Create folder:

```text
AI-Resume-Builder
```

Open it inside VS Code.

---

## STEP 6 — Open Terminal

Inside VS Code:

```text
Terminal → New Terminal
```

---

## STEP 7 — Create Virtual Environment

Command:

```bash
python -m venv venv
```

---

## STEP 8 — Activate Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

Expected:

```text
(venv)
```

---

## STEP 9 — Install Required Packages

Install packages:

```bash
pip install google-generativeai
```

```bash
pip install streamlit
```

```bash
pip install python-dotenv
```

```bash
pip install fpdf
```

OR install everything together:

```bash
pip install google-generativeai streamlit python-dotenv fpdf
```

---

## STEP 10 — Create Required Files

Create:

```text
main.py
resume_agent.py
prompt_templates.py
app.py
.env
```

---

## STEP 11 — Get Gemini API Key

Website:
[https://aistudio.google.com/](https://aistudio.google.com/)

Steps:

1. Login
2. Click “Get API Key”
3. Click “Create API Key”
4. Copy the generated API key

---

## STEP 12 — Store API Key

Inside `.env`

```env
GEMINI_API_KEY=your_api_key
```

---

# Running the Project

## Run Terminal Version

```bash
python main.py
```

---

## Run Streamlit Web App

```bash
python -m streamlit run app.py
```

Open browser:

```text
http://localhost:8501
```

---

# Workflow Architecture

```text
User Input
↓
Prompt Template
↓
Gemini AI Model
↓
Resume Generation
↓
PDF Creation
↓
Download Resume
```

---

# Agentic AI Concepts Used

## Planning Workflow

The AI follows structured generation:

* Summary
* Skills
* Projects
* Education
* Final Resume

---

## Tool Usage

Integrated tools:

* Gemini API
* Streamlit
* FPDF

---

## Workflow Automation

Input → AI Processing → Resume Output → PDF Download

---

# Future Improvements

* ATS Score Checker
* Job Description Analyzer
* Multi-Agent Workflow
* Resume Formatter Agent
* Cover Letter Generator
* SQLite Memory
* Multi-Page Streamlit App

---

# Resume Description

Built an AI-powered Resume Builder Agent using Python, Streamlit, and Gemini API that generates ATS-friendly resumes through prompt engineering, workflow automation, and PDF export functionality.

---

# Current Project Level

This project demonstrates:

* AI workflow integration
* Prompt engineering
* Streamlit frontend development
* API integration
* PDF automation
* Beginner-level Agentic AI concepts

---

# Author

Abhinav Kandukuri
