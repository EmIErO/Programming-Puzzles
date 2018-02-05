def convert_data_to_table(file_name):

    with open(file_name, "r") as file:
        lines = file.readlines()

    data_table = [line.replace("\n", "").split(" ") for line in lines]

    return data_table


def compare_phrases(row):
    for i in range(len(row) - 1):
        for j in range(i+1, len(row)):
            if row[i] == row[j]:
                return True
        


def count_valid_passphrases(table):

    all_passphrases = len(table)
    valid_passphrases = all_passphrases
    for row in table:
        if compare_phrases(row):
            valid_passphrases -= 1

    return valid_passphrases


def main():

    table = convert_data_to_table("passphrases.txt")
    valid_passphrases = count_valid_passphrases(table)
    print(valid_passphrases)


if __name__ == '__main__':
    main()
