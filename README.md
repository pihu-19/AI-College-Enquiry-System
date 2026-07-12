# 🎓 AI College Enquiry System

## Project Overview

The AI College Enquiry System is a simple Multi-Agent application developed using Python and Streamlit. It helps students get information related to college admission, fees, examinations, and scholarships through different AI agents.

The project uses intent classification to identify the user's query and routes it to the appropriate agent.

---

## Features

- Multi-Agent Architecture
- Intent Classification
- Streamlit User Interface
- College Knowledge Base
- Admission Information
- Fee Information
- Exam Information
- Scholarship Information

---

## Technologies Used

- Python
- Streamlit
- LangGraph (Project Structure)
- AI Agents
- Knowledge Base

---

## Project Structure

```
AI-College-Enquiry-System/
│
├── app.py
│
├── agents/
│   ├── admission_agent.py
│   ├── exam_agent.py
│   ├── fees_agent.py
│   ├── scholarship_agent.py
│   └── intent_classifier.py
│
├── graph/
│   └── graph_builder.py
│
├── knowledge/
│   └── college_data.py
│
├── assets/
│   └── college.jpg
│
└── README.md
```

---

## Workflow

```
User Question
      │
      ▼
Intent Classifier
      │
      ▼
Select Appropriate Agent
      │
      ├── Admission Agent
      ├── Fees Agent
      ├── Exam Agent
      └── Scholarship Agent
      │
      ▼
Knowledge Base
      │
      ▼
Response to User
```

---

## AI Agents

### Admission Agent
- Admission process
- Eligibility
- Required documents

### Fees Agent
- Course fees
- Payment information

### Exam Agent
- Semester examination information

### Scholarship Agent
- Scholarship details

---

## How to Run

### Install Streamlit

```bash
pip install streamlit
```

### Run the Application

```bash
python -m streamlit run app.py
```

The application will open in your web browser.

---

## Sample Questions

- What is the admission process?
- What documents are required?
- What are the fees?
- Tell me about exams.
- Is scholarship available?

---

## Future Improvements

- Course information
- Placement information
- Seat availability
- Better intent classification
- Database integration
- Large Language Model (LLM) support

---

## Developer

**PIHU**

AI Internship Project
