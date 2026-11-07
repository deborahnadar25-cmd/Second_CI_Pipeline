def first_non_repeating_char(string):
    for char in string:
        if string.count(char) == 1:
            return char
    return None


if __name__ == "__main__":
    string = input("Enter a string: ")
    print(first_non_repeating_char(string))