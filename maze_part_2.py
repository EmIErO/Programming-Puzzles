# Program is given a list of numbers that are steps to be performed.
# The rule for step is: -x moves x steps to the previous instruction, and y skips y steps to the next one. 
# After each step, the offset of that instruction: if it was three or more,decreases it by 1; otherwise, increases by 1.
# Program counts how many steps need to be performed to get outside of the list.

import maze


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

        if list_[old_position] >= 3:
            list_[old_position] = list_[old_position] - 1
        else:
            list_[old_position] = list_[old_position] + 1
        
        old_position = new_position
        
        steps +=1

    print("Getting out took {} steps.".format(steps)) 


def main():
    list_of_steps = maze.convert_data_to_list("maze.txt")
    count_steps(list_of_steps)


if __name__ == '__main__':
    main()