def convert_data_to_list(file_name):

    with open(file_name, "r") as file:

        list_of_steps = file.readlines()

        steps = [step.replace("\n", "").split(",") for step in list_of_steps] # creates list inside list
        steps = steps[0] # unpacks list    
        steps = [int(number) for number in steps]
        
    return steps


def count_steps(list_):
        
    steps = 0
    old_position = 0

    while old_position < len(list_):
    
        new_position = old_position + list_[old_position]
        list_[old_position] = list_[old_position] + 1
        old_position = new_position
        
        steps +=1

    print("Getting out took {} steps.".format(steps)) 


def main():
    list_of_steps = convert_data_to_list("maze.txt")
    count_steps(list_of_steps)


if __name__ == '__main__':
    main()