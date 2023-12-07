import random


def main():
    level = get_level()
    generate_integer(level)

def get_level():
    while True:
        try:
            level = input("Level: ")
            if level in ("1","2","3"):
                return level
        except ValueError:
            continue

def generate_integer(level):
    score = 0
    for _ in range(10):
        if level == "1":
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        elif level == "2":
            x = random.randint(10, 99)
            y = random.randint(10, 99)
        else:
            x = random.randint(100, 999)
            y = random.randint(100, 999)

        for _ in range(3):
            try:
                answer = int(input(f"{x} + {y} = : "))
                if (x+y) == answer:
                    print("Right")
                    score += 1
                    break
                else:
                    print("EEE")
                    continue
            except (ValueError, TypeError):
                continue

        print(f"{x} + {y} = {x+y}")

    print(f"Score: {score}")

if __name__ == "__main__":
    main()