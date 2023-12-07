def two_letter(s):
    return s[:2].isalpha()

def check_length(s):
    return 2 <= len(s) <= 6

def punctuations(s):
    return not any(char in s for char in """.,!?;:'"()[]{}<>-—–/ """)

def proper_numbers(s):
    for i in range(len(s) - 1):
        if s[i].isdigit():
            if s[i] == '0':
                return False
            else:
                for j in range(i + 1, len(s)):
                    if s[j].isalpha():
                        return False
    return True

def is_valid(s):
    return (two_letter(s) and check_length(s) and punctuations(s) and proper_numbers(s))

def main():
    plate = input("enter the plat name and number: ")

    if is_valid(plate):
        print("valid")

    else:
        print("invalid")
main()