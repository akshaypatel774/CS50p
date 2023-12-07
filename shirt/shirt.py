import sys
import os
from PIL import Image, ImageOps

IMAGE_EXTENSIONS = (".jpg", ".jpeg", ".png")

def main():
    file = get_file()
    with Image.open(file) as image:
        with Image.open("shirt.png") as overlay:
            x, y = overlay.size
            image = ImageOps.fit(image, (x, y))
            image.paste(overlay, overlay)
            image.save(sys.argv[2], format=None)


def get_file():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 3 and not (sys.argv[1].endswith(IMAGE_EXTENSIONS) and sys.argv[2].endswith(IMAGE_EXTENSIONS)):
        sys.exit("Invalid input")
    elif not sys.argv[1] in os.listdir():
        sys.exit("Input does not exist")
    elif sys.argv[1][-4:] != sys.argv[2][-4:]:
        sys.exit("Input and output have different extensions")
    else:
        return sys.argv[1]

if __name__=="__main__":
    main()