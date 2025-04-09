import os
from feedback_entry import collect_feedback

def test_collect_feedback():
    test_file = "feedback_data.csv"
    if os.path.exists(test_file):
        os.remove(test_file)

    collect_feedback("Alice", "Math", 90)

    with open(test_file, "r") as f:
        data = f.read()

    assert "Alice,Math,90\n" in data
