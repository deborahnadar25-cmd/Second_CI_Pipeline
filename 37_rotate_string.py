def rotate_string(string, position):
    if not string:
        return string

    position = position % len(string)
    return string[-position:] + string[:-position] if position else string


if __name__ == "__main__":
    string = input("Enter a string: ")
    position = int(input("Enter rotation position: "))
    print(rotate_string(string, position))