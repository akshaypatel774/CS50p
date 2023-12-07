import sys
import os
import csv

def main():
    file = get_file()
    with open(file, "r") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        after = []
        for row in reader:
            last, first = row["name"].split(",")
            after.append({'first': first.strip(), 'last': last, 'house': row["house"]})

    with open(sys.argv[2], "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["first","last","house"])
        writer.writeheader()
        for row in after:
            writer.writerow(row)


def get_file():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 3 and not sys.argv[1].endswith(".csv"):
        sys.exit("Not a csv file")
    elif not sys.argv[1] in os.listdir():
        sys.exit(f"Could not read {sys.argv[1]}")
    else:
        return sys.argv[1]

if __name__=="__main__":
    main()