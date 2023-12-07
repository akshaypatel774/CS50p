import emoji

def main():
    try:
        emojis = input("Input: ")

    except (ValueError, TypeError):
        pass

    else:
        print(emoji.emojize(f"{emojis}"))

if __name__ == "__main__":
    main()