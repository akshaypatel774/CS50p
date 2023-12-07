import sys
from pyfiglet import Figlet
from random import randint

figlet = Figlet()
font_list = figlet.getFonts()

def main():
    get_args()
    text = input("Input: ")
    print(figlet.renderText(text))

def get_args():
    if len(sys.argv) == 1:
        font = font_list[randint(0, len(font_list))]
        figlet.setFont(font=font)
    elif len(sys.argv) == 3 and sys.argv[1] in ['-f', '--font']:
        figlet.setFont(font=sys.argv[2])
    else:
        sys.exit("Invalid usage")

if __name__ == "__main__":
    main()