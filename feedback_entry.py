def collect_feedback(student_name, course, rating, comments=""):
    """Collect student feedback"""
    return {
        "student_name": student_name,
        "course": course,
        "rating": rating,
        "comments": comments
    }
