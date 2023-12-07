import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    matched = re.findall(r'\bum\b', s, re.IGNORECASE)
    return len(matched)


if __name__ == "__main__":
    main()