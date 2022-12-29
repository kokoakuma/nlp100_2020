def n_gram(target, n) -> list:
    return [target[index:index + n] for index in range(len(target) - n + 1)]


def main():
    text1 = "paraparaparadise"
    text2 = "paragraph"
    bi_gram_x = set(n_gram(text1, 1))
    bi_gram_y = set(n_gram(text2, 1))

    union_x_y = bi_gram_x | bi_gram_y
    intersection_x_y = bi_gram_x & bi_gram_y
    diff_a_not_b = bi_gram_x - bi_gram_y
    diff_b_not_a = bi_gram_y - bi_gram_x

    print(f"bi_gram_x: {bi_gram_x}")
    print(f"bi_gram_y: {bi_gram_y}")
    print(f"union_x_y: {union_x_y}")
    print(f"intersection_x_y: {intersection_x_y}")
    print(f"diff_a_not_b: {diff_a_not_b}")
    print(f"diff_b_not_a: {diff_b_not_a}")


if __name__ == '__main__':
    main()
