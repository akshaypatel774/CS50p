import sys
import os

def main():
    file = get_file()
    count=0
    with open(file, 'r') as lines:
        for line in lines:
            if line.strip().startswith("\n") or line.strip().startswith("#") or line.isspace():
                pass
            else:
                count+=1
    print(count)

def get_file():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 2 and not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    elif not sys.argv[1] in os.listdir():
        sys.exit("File does not exist")
    else:
        return sys.argv[1]

main()