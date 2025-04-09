# report_generator.py

def export_feedback_summary(feedback_list, filename="feedback_summary.txt"):
    with open(filename, "w") as file:
        file.write("Student Feedback Summary\n")
        file.write("=" * 30 + "\n\n")
        for feedback in feedback_list:
            file.write(f"Name: {feedback['name']}\n")
            file.write(f"Score: {feedback['score']}\n")
            file.write(f"Comments: {feedback['comments']}\n")
            file.write("-" * 30 + "\n")
    print(f"Feedback summary exported to {filename}")
