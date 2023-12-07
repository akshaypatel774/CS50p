import sys
import os
import csv
from tabulate import tabulate

# print(tabulate(table, headers, tablefmt="grid"))
def main():
    file = get_file()
    with open(file, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        headers = next(reader)
        print(tabulate(reader, headers, tablefmt="grid"))


def get_file():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 2 and not sys.argv[1].endswith(".csv"):
        sys.exit("Not a csv file")
    elif not sys.argv[1] in os.listdir():
        sys.exit("File does not exist")
    else:
        return sys.argv[1]

main()