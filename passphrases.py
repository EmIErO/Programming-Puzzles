def convert_data_to_table(file_name):

    with open(file_name, "r") as file:
        lines = file.readlines()

    data_table = [line.replace("\n", "").split(" ") for line in lines]
    print(data_table)

    return data_table

convert_data_to_table("passphrases.txt")