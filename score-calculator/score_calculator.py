def calculate_average_score(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    scores = [int(line.strip().split(",")[2]) for line in lines]
    return sum(scores) / len(scores) if scores else 0
