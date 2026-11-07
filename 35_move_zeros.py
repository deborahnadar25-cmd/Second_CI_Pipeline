def move_zeros(numbers):
    non_zeros = [num for num in numbers if num != 0]
    zeros = [num for num in numbers if num == 0]
    return non_zeros + zeros


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print(move_zeros(numbers))