def convert_data_to_table(file_name):

    with open(file_name, "r") as file:
        lines = file.readlines()
        table_of_data = [line.replace("\n", "").split("\t") for line in lines]

    return table_of_data

table = convert_data_to_table("corruption_checksum.txt")
print(table)