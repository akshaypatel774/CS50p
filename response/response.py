from validator_collection import checkers

def main():
    print(is_valid(input("What's your email address? ")))


def is_valid(s):
    if checkers.is_email(s, allow_empty = False) == True:
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()