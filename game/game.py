import random

def main():
    s=get_level()
    guessing(s)

def get_level():
    level = 0
    while level < 1:
        try:
            level = int(input("Level: "))
            return random.randint(1,level)
        except (ValueError, TypeError):
            continue

def guessing(level):
    guess=None
    while guess!=level:
        try:
            guess = int(input("Guess: "))
        except (ValueError, TypeError):
            continue

        if guess<level:
            print("Too small!")
        elif guess>level:
            print("Too large!")

        print("Just right!")

if __name__=="__main__":
    main()