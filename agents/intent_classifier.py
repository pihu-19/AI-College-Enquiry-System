
def intent_classifier(question):

    question = question.lower().strip()

    admission_keywords = [
        "admission", "apply", "application", "join", "enroll",
        "registration", "eligibility", "eligible",
        "document", "documents",
        "course", "courses",
        "branch", "branches",
        "department", "departments",
        "seat", "seats",
        "placement", "placements",
        "company", "companies",
        "package",
        "backlog", "backlogs"
    ]

    fees_keywords = [
        "fee", "fees", "payment", "pay", "cost",
        "price", "charge", "tuition", "amount"
    ]

    exam_keywords = [
        "exam", "exams", "semester", "test",
        "paper", "result", "results",
        "marks", "schedule", "timetable", "time table"
    ]

    scholarship_keywords = [
        "scholarship", "scholarships",
        "grant", "financial help",
        "government scheme"
    ]

    if any(keyword in question for keyword in admission_keywords):
        return "admission"

    elif any(keyword in question for keyword in fees_keywords):
        return "fees"

    elif any(keyword in question for keyword in exam_keywords):
        return "exam"

    elif any(keyword in question for keyword in scholarship_keywords):
        return "scholarship"

    return "unknown"