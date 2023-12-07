def main():
    plate = input("enter the plat name and number: ")
    if is_valid(plate):
        print("valid")

    else:
        print("invalid")


def is_valid(s):

    if (len(s) > 0 and s[0].isdigit()) or (len(s) > 1 and s[1].isdigit()):
        return False

    elif len(s) > 6 or len(s) <= 2:
        return False

    for char in s:
        if char in (""".,!?;:'"()[]{}<>-—–/ """):
            return False

    for i in range(len(s) - 1):
        if s[i].isdigit() and s[i] == '0' and s[i-1].isalpha():
            return False
        elif s[i].isdigit():
            for j in range(i + 1, len(s)):
                if s[j].isalpha():
                    return False
    else:
        return True


if __name__ == "__main__":
    main()