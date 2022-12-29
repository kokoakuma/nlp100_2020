
import re


def main():
    text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    size_one_set = {1, 5, 6, 7, 8, 9, 15, 16, 19}
    splitted_texts = re.sub(r"[,.!?:;']", "", text).split(" ")

    text_dict = {}
    for index, text in enumerate(splitted_texts):
        target_number = index + 1
        if target_number in size_one_set:
            sliced = text[:1]
            text_dict[sliced] = target_number
        else:
            sliced = text[:2]
            text_dict[sliced] = target_number

    print(text_dict)


if __name__ == '__main__':
    main()
