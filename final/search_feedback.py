def search_feedback(feedback_list, name):
    for feedback in feedback_list:
        if feedback["name"].lower() == name.lower():
            return feedback
    return None
