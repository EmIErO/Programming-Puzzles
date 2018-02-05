def convert_data_to_list(file_name):

    with open(file_name, "r") as file:
        list_of_steps = []
    
        for line in file:
            #print(line)
            step = file.readline()
            print(step)
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
        print(steps)

    print("Getting out took {} steps.".format(steps)) 


def main():
    list_of_steps = convert_data_to_list("maze.txt")
    print(list_of_steps)
    count_steps(list_of_steps)


if __name__ == '__main__':
    main()