def calculate_average(scores):
    if not scores:
        return 0

    total = sum(scores)
    average = total / len(scores)
    return average


def main():
    scores = [78, 85, 92, 66]
    result = calculate_average(scores)
    print(f"Average score: {result:.2f}")


if __name__ == "__main__":
    main()
