def main():
    word = input("Input: ")
    word = shorten(word)
    print(word)

def shorten(word):
    for char in word:
        if char.lower() in "aeiou":
            word = word.replace(char, "")
    return word

if __name__ == "__main__":
    main()