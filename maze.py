def convert_data_to_list(file_name):

    with open(file_name, "r") as file:
        list_of_steps = []
        for line in file:
            step = file.readline()
            step = int(step.replace("\n", ""))
            list_of_steps.append(step)
        
    return list_of_steps


def count_steps(list_):
        
    steps = 0
    old_position = 0

    while old_position < len(list_):
    
        new_position = old_position + list_[old_position]
        list_[old_position] = list_[old_position] + 1
        old_position = new_position
        
        steps +=1

    print("Getting out took {} steps.".format(steps)) 

convert_data_to_list("maze.txt")