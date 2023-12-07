def main():
    fuel = convert_int()
    print(fuel)

def get_fraction():
    while True:
        try:
            x,y = map(int, input("Fraction: ").split('/'))
            fuel = round(((x/y)*100))
        except (ValueError, ZeroDivisionError):
            continue
        else:
            return fuel


def convert_int():
    fuel = get_fraction()
    if 0 <= fuel <= 1:
        return "E"
    elif 100>= fuel >= 99:
        return "F"
    elif 2<=fuel<=98:
        return (f"{fuel}%")
    else:
        return get_fraction()

if __name__ == "__main__":
    main()