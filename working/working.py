import re
import sys


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    s = re.search(r'^(0?[1-9]|1[0-2])(:[0-5][0-9])? (AM|PM) to (0?[1-9]|1[0-2])(:[0-5][0-9])? (AM|PM)$', s, re.IGNORECASE)
    if s is None:
        raise ValueError
    else:
        start_hour = s.group(1)
        start_min = s.group(2)
        start_abbr = s.group(3)
        end_hour = s.group(4)
        end_min = s.group(5)
        end_abbr = s.group(6)
        if start_min is None:
            start_min = "00"
        else:
            start_min = start_min.replace(':', '')
        if end_min is None:
            end_min = "00"
        else:
            end_min = end_min.replace(':', '')
        if start_abbr == 'PM' and start_hour != '12':
            start_hour = int(start_hour)+12
        else:
            start_hour = int(start_hour)
        if end_abbr == 'PM' and end_hour != '12':
            end_hour = int(end_hour)+12
        else:
            end_hour = int(end_hour)
        if start_hour == 12 and start_abbr == 'AM':
            start_hour = 0
        return f"{start_hour:02}:{start_min:02} to {end_hour:02}:{end_min:02}"


if __name__ == "__main__":
    main()