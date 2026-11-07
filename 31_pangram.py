def is_pangram(sentence):
    letters = set()

    for char in sentence.lower():
        if char.isalpha():
            letters.add(char)

    return len(letters) == 26


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    print(is_pangram(sentence))


# Python code