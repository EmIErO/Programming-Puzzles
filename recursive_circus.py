def get_data(file_name):

    with open(file_name, "r") as file:

        lines = file.readlines()

        table = [line.replace("\n", "").replace(" -> ", " ").replace(",", "").replace("(", "").replace(")", "").split(" ") for line in lines]
    
    return table


table = get_data("recursive_circus.txt")

weight_index = 1

weight_column = [row[weight_index] for row in table]
weight_column = [int(weight) for weight in weight_column]
print(weight_column)

def find_bottom_program_weight(weight_column):

    for weight in weight_column:
        print(weight_column.count(weight))
        if weight_column.count(weight) == 1:
            searched_program_weight = weight

    return searched_program_weight

searched_program_weight = find_bottom_program_weight(weight_column)
index = weight_column.index(searched_program_weight)

name_index = 0
name = table[index][name_index]

print(searched_program_weight)
print(index)
print(name)