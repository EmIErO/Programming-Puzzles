# Program converts txt file with data to a table (list of lists).
# Then it finds the only two numbers in each row of the table where one evenly divides the other  
# and adds up each row's result

import corruption_checksum


def calculate_quotient(row):
"""
Finds the only two numbers in a row where one evenly divides the other.
"""
    quotient = 0

    for i in range(len(row)):
            for j in range(len(row)):
                if i != j and row[i] % row[j] == 0: # doesn't allow dividing a number by itself, finds if different numbers divide evenly
                    quotient += row[i] / row[j]
                
    return quotient


def prepare_list_of_quotients(table):
    """
    Prepares list of quotients for every row in the given table.
    """

    list_of_quotients = [calculate_quotient(row) for row in table]

    return list_of_quotients

    
def main():

    table = corruption_checksum.convert_data_to_table("corruption_checksum.txt")
    list_of_quotients = prepare_list_of_quotients(table)
    checksum = sum(list_of_quotients) # calculates sum of all quotients
    print(checksum)
    

if __name__ == '__main__':
    main()