def main():
    characters = input("Input: ")
    for char in characters:
        if char in "AaEeIiOoUu":
            characters = characters.replace(char, "")
    print(characters)


if __name__ == "__main__":
    main()