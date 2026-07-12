
from agents.intent_classifier import intent_classifier
from agents.admission_agent import admission_agent
from agents.fees_agent import fees_agent
from agents.exam_agent import exam_agent
from agents.scholarship_agent import scholarship_agent


def process_question(question):

    state = {"question": question}

    intent = intent_classifier(question)

    if intent == "admission":
        return admission_agent(state)["response"]

    elif intent == "fees":
        return fees_agent(state)["response"]

    elif intent == "exam":
        return exam_agent(state)["response"]

    elif intent == "scholarship":
        return scholarship_agent(state)["response"]

    else:
        return (
            "I can help you with:\n\n"
            "• Admission\n"
            "• Eligibility\n"
            "• Required Documents\n"
            "• Courses\n"
            "• Departments\n"
            "• Seat Availability\n"
            "• Placements\n"
            "• Backlogs\n"
            "• Fees\n"
            "• Exams\n"
            "• Scholarships\n\n"
            "Please ask a college-related question."
        )