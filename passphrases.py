# Program checks if passphrase that consists of a series of words (lowercase letters) 
# separated by spaces contains no duplicate words.
# Phassphrases to check are given as a txt file.

def convert_data_to_table(file_name):
    """
    Converts data from txt file to list of lists.
    Returns list of lists with data.
    """
    with open(file_name, "r") as file:
        lines = file.readlines()

    data_table = [line.replace("\n", "").split(" ") for line in lines]

    return data_table


def compare_phrases(row):
    """
    Compares phrases from a list (row), if duplicate phrases are found, returns True.
    """
    for i in range(len(row) - 1):
        for j in range(i+1, len(row)):
            if row[i] == row[j]:
                return True
        


def count_valid_passphrases(table):
    """
    Counts passphrases without duplicates.
    Returns number of valid passphrases.
    """

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
