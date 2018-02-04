import corruption_checksum

def calculate_quotient(row):

    quotient = 0

    for i in range(len(row)):
            for j in range(len(row)):
                if i != j and row[i] % row[j] == 0:
                    quotient += row[i] / row[j]
                
    return quotient


def prepare_list_of_quotients(table):

    list_of_quotients = [calculate_quotient(row) for row in table]
    print(list_of_quotients)

    return list_of_quotients

    
def main():
    table = corruption_checksum.convert_data_to_table("corruption_checksum.txt")
    list_of_quotients = prepare_list_of_quotients(table)
    checksum = sum(list_of_quotients)
    print(checksum)
    

if __name__ == '__main__':
    main()