
import re


def main():
    text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    splittedTexts = re.sub(r"[,.!?:;']", "", text).split(" ")

    sizes = []
    for text in splittedTexts:
        textSize = len(text)
        sizes.append(textSize)

    for size in sizes:
        print(str(size))


if __name__ == '__main__':
    main()
