# Program converts txt file with data to a table (list of lists).
# It calculates the difference between the largest value and the smallest value for each row; 
# then it calculates the sum of all of these differences.

def convert_data_to_table(file_name):
"""
Converts txt file with data to a table (list of lists) of int.
"""
    with open(file_name, "r") as file:
        lines = file.readlines()
        table_of_data = [line.replace("\n", "").split("\t") for line in lines]

    for row in table_of_data:
        for i in range(len(row)):
            row[i] = int(row[i])

    return table_of_data


def calculate_range(table):
"""
Calculates the difference between the largest value and the smallest value for each row.
"""
    list_of_ranges = [max(row) - min(row) for row in table]

    return list_of_ranges


def main():
    
    table = convert_data_to_table("corruption_checksum.txt")
    list_of_ranges = calculate_range(table)
    checksum = sum(list_of_ranges)
    print(checksum)
    

if __name__ == '__main__':
    main()

