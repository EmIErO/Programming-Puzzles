# Program reviews a sequence of digits (a txt file) 
# and find the sum of all digits that match the next digit in the list. 
# The list is circular, so the digit after the last digit is the first digit in the list


def convert_captcha_to_list(file_name):
    """Converts string of digits from a txt file into a list of digits (int)."""

    with open(file_name, "r") as file:
        captcha = file.readline()

    captcha = captcha.replace("\n","")
    list_of_digits = list(captcha)
    list_of_digits = [int(digit) for digit in list_of_digits]

    return list_of_digits


def add_matching_digits(list_of_digits):
    """Calculates the sum of all digits that match the next digit in the list. 
    The digit after the last digit is checked with the first digit in the list."""

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