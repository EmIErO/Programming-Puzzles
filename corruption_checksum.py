def convert_data_to_table(file_name):

    with open(file_name, "r") as file:
        lines = file.readlines()
        table_of_data = [line.replace("\n", "").split("\t") for line in lines]

    for row in table_of_data:
        for i in range(len(row)):
            row[i] = int(row[i])

    return table_of_data


def calculate_range(table):

    list_of_ranges = [max(row) - min(row) for row in table]

    return list_of_ranges


