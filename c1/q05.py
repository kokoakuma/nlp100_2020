
# n-gramとは、連続するn個の単語や文字のまとまり
# I am an PHPerをtri-gramで表すと、I am an と am an PHPer になる

def n_gram(target, n) -> list:
    return [target[index:index + n] for index in range(len(target) - n + 1)]


def main():
    text = "I am an PHPer"
    for i in range(1, 4):
        print(n_gram(text, i))
        print(n_gram(text.split(' '), i))


if __name__ == '__main__':
    main()
