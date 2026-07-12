
def admission_agent(state):

    question = state["question"].lower()

    if "course" in question or "courses" in question or "branch" in question or "department" in question:
        return {
            "response": "The college offers Diploma courses in Computer Science Engineering, Electronics Engineering, Mechanical Engineering and Civil Engineering."
        }

    elif "placement" in question or "company" in question or "package" in question:
        return {
            "response": "The college provides placement assistance. Companies from IT and core engineering sectors visit the campus."
        }

    elif "seat" in question:
        return {
            "response": "Seat availability depends on the admission year and department. Please contact the admission office for the latest seat details."
        }

    elif "backlog" in question:
        return {
            "response": "Students with backlogs need to clear them according to college rules. Placement eligibility depends on company criteria."
        }

    elif "document" in question:
        return {
            "response": "Required documents include marksheet, Aadhaar Card, photographs, Transfer Certificate and other required certificates."
        }

    elif "eligibility" in question:
        return {
            "response": "Eligibility depends on the course requirements and institute admission rules."
        }

    elif "admission" in question or "apply" in question:
        return {
            "response": "Admission process includes checking eligibility, submitting documents and completing the application procedure."
        }

    else:
        return {
            "response": "Please ask about admission, courses, placements, seats, backlogs, eligibility or documents."
        }