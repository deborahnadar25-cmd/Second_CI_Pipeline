def count_words(sentence):
    words = sentence.split()
    return len(words)


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    print(count_words(sentence))