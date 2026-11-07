def find_largest(numbers):
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest


def main():
    values = [-8, -3, -12, -5]
    result = find_largest(values)
    print(f"Largest number: {result}")


if __name__ == "__main__":
    main()
