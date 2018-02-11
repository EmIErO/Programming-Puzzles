# Program is given a list of numbers that are steps to be performed.
# The rule for step is: -x moves x steps to the previous instruction, and y skips y steps to the next one. 
# After each step, the offset of that instruction increases by 1.
# Program counts how many steps need to be performed to get outside of the list.

    def convert_data_to_list(file_name):
    """
    Converts txt file with numbers to a list of int.
    Returns a list (steps).
    """
    with open(file_name, "r") as file:

        list_of_steps = file.readlines()

        steps = [step.replace("\n", "").split(",") for step in list_of_steps] # creates list inside list
        steps = steps[0] # unpacks list    
        steps = [int(number) for number in steps]
        
    return steps


def count_steps(list_):
    """
    Counts steps needed to get outside of the list.
    Changes numbers in list accordingly to performed steps.
    Prints to console final number of steps.
    """       
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