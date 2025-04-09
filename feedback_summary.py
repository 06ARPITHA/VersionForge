def summarize_feedback(feedback_scores):
    if not feedback_scores:
        return {
            "average": 0,
            "highest": None,
            "lowest": None,
            "total_feedback": 0
        }

    average_score = sum(feedback_scores) / len(feedback_scores)
    highest_score = max(feedback_scores)
    lowest_score = min(feedback_scores)
    total_feedback = len(feedback_scores)

    return {
        "average": round(average_score, 2),
        "highest": highest_score,
        "lowest": lowest_score,
        "total_feedback": total_feedback
    }

# Example run
if __name__ == "__main__":
    sample = [4, 5, 3, 4, 2, 5]
    summary = summarize_feedback(sample)
    print("Feedback Summary:")
    for k, v in summary.items():
        print(f"{k.capitalize()}: {v}")
