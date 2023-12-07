import re

def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    if s := re.search(r'<iframe[^>]*src="https?://(?:www\.)?youtube\.com/embed/([^"/]+)"', s):
        return "https://youtu.be/" + s.group(1)
    else:
        return None


if __name__ == "__main__":
    main()