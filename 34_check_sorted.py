def is_sorted(numbers):
    return numbers == sorted(numbers)


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print(is_sorted(numbers))