def collect_feedback(student_name, subject, score):
    entry = f"{student_name},{subject},{score}\n"
    with open("feedback_data.csv", "a") as file:
        file.write(entry)
