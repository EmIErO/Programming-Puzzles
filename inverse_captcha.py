def convert_captcha_to_list(file_name):

    with open(file_name, "r") as file:
        captcha = file.readline()

    captcha = captcha.replace("\n","")
    list_of_digits = list(captcha)
    list_of_digits = [int(digit) for digit in list_of_digits]

    return list_of_digits


def add_matching_digits(list_of_digits):

    sum_of_matching_digits = 0

    for i in range(len(list_of_digits)-1):
        if list_of_digits[i] == list_of_digits[i + 1]:
            sum_of_matching_digits += list_of_digits[i]

    first_digit_index = 0
    last_digit_index = -1
    if list_of_digits[first_digit_index] == list_of_digits[last_digit_index]:
        sum_of_matching_digits += list_of_digits[first_digit_index]

    return sum_of_matching_digits


def main():

    list_of_digits = convert_captcha_to_list("my_capcha.txt")
    sum_of_matching_digits = add_matching_digits(list_of_digits)
    print(sum_of_matching_digits)


if __name__ == '__main__':
    main()