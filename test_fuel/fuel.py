def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    fuel = gauge(percentage)
    print(fuel)


def convert(fraction):
    try:
        x,y = map(int, fraction.split('/'))
        print(round(((x/y)*100)))
        return round(((x/y)*100))
    except (ValueError, ZeroDivisionError):
        pass

def gauge(percentage):
    try:
        if percentage <= 1:
            return "E"
        elif percentage >= 99:
            return "F"
        else:
            return (f"{percentage}%")
    except TypeError:
        pass

if __name__ == "__main__":
    main()