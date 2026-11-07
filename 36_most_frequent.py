def most_frequent(numbers):
    if not numbers:
        return None

    return max(set(numbers), key=numbers.count)


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print(most_frequent(numbers))