import re
import sys


def main():
    ip = input("IPv4 Address: ")
    print(validate(ip))


def validate(ip):
    return (ip := re.match(r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", ip)) is not None

if __name__ == "__main__":
    main()