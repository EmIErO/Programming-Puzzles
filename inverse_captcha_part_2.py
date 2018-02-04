import inverse_captcha


def add_matching_digits(list_of_digits):
    """Calculates the sum of all digits that match the digit halfway around the circular list."""

    half_of_list = int(len(list_of_digits) / 2)
    sum_of_digits = 0

    for i in range(half_of_list):
        if list_of_digits[i] == list_of_digits[i + half_of_list]:
            sum_of_digits += list_of_digits[i]
            sum_of_digits += list_of_digits[i + half_of_list]

    return sum_of_digits


def main():

    list_of_digits = inverse_captcha.convert_captcha_to_list("my_capcha.txt")
    sum_of_digits = add_matching_digits(list_of_digits)
    print(sum_of_digits)


if __name__ == '__main__':
    main()