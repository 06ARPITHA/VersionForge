from score_calculator import calculate_average_score

def test_calculate_average_score():
    with open("test_data.csv", "w") as f:
        f.write("Bob,English,80\n")
        f.write("Alice,Math,90\n")

    assert calculate_average_score("test_data.csv") == 85.0
