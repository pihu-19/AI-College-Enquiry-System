
from knowledge.college_data import college_data


def fees_agent(state):

    return {
        "response": college_data["fees"]
    }