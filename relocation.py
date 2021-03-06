# Program performs a reallocation routine as long as it finds a blocks-in-banks configuration that has been seen before.
# The reallocation routine operates in cycles. In each cycle, it finds the memory bank with the most blocks 
# (ties won by the lowest-numbered memory bank) and redistributes those blocks among the banks. 
# To do this, it removes all of the blocks from the selected bank, then moves to the next (by index) memory bank and inserts one of the blocks. 
# It continues doing this until it runs out of blocks.
# Number of mamory banks and blocks in every bank is given by the user. Program prints to console a configuration that is repeated. 


def count_steps(set_of_blocks):
    """
    Creates a list of all seen redistributions. Counts number of steps needed to be performend until a configuration
    that has been seen before appeares.
    Prints that configuration and number of steps.
    """
    all_redistributions = []
    steps = 0
    
    while set_of_blocks not in all_redistributions:

        copy_of_set = set_of_blocks[:]
        all_redistributions.append(copy_of_set)  
        set_of_blocks = distribute_blocks(set_of_blocks)
                    
        if set_of_blocks in all_redistributions:
            steps += 1
            print("This configuration appears for the second time:\n")
            print(set_of_blocks)
            print("\nIt took {} steps.".format(steps))   
        else: 
            steps += 1


def distribute_blocks(set_of_blocks):
    """
    Distributes number of blocks among memory banks.
    Returns set of blocks after redistribiution.
    """
    lenght_of_set = len(set_of_blocks)

    blocks_to_distribiute = max(set_of_blocks)
    blocks_to_distribiute_index = set_of_blocks.index(blocks_to_distribiute)

    set_of_blocks[blocks_to_distribiute_index] = 0 # removes blocks from a memory bank

    first_part_of_blocks, last_part_of_blocks, number_of_cycles = divide_blocks_to_distribiute(lenght_of_set, 
                                                                                                blocks_to_distribiute_index, 
                                                                                                blocks_to_distribiute)

    # Case: number of blocks to distribute is smaller than or equal to memory banks left till the end of set.
    if last_part_of_blocks == 0 and number_of_cycles == 0:
        end_of_iteration = blocks_to_distribiute_index + blocks_to_distribiute + 1

        for i in range(blocks_to_distribiute_index + 1, end_of_iteration):
            set_of_blocks[i] = set_of_blocks[i] + 1
    
    # Case: number of blocks to distribute is larger than memory banks left till the end of set.
    elif last_part_of_blocks != 0 or number_of_cycles != 0:
        
        for i in range(blocks_to_distribiute_index + 1, lenght_of_set):
            set_of_blocks[i] = set_of_blocks[i] + 1
        for i in range(last_part_of_blocks):
            set_of_blocks[i] = set_of_blocks[i] + 1

        if number_of_cycles != 0:
            while number_of_cycles > 0:    
                for i in range(lenght_of_set):
                    set_of_blocks[i] = set_of_blocks[i] + 1
                number_of_cycles -= 1

    return set_of_blocks


def divide_blocks_to_distribiute(lenght_of_set, blocks_to_distribiute_index, blocks_to_distribiute):
    """
    Divides blocks into parts.
    Returns parts of blocks.
    """  
    spots_till_end_of_list = lenght_of_set - blocks_to_distribiute_index - 1

    # Case: number of blocks to distribute is smaller than or equal to memory banks left till the end of set.
    if spots_till_end_of_list >= blocks_to_distribiute:
        first_part_of_blocks = blocks_to_distribiute
        last_part_of_blocks = 0
        number_of_cycles = 0

    # Case: number of blocks to distribute is larger than memory banks left till the end of set.
    else:
        first_part_of_blocks = spots_till_end_of_list
        remaining_blocks = blocks_to_distribiute - first_part_of_blocks
        last_part_of_blocks = remaining_blocks % lenght_of_set 
        
        if remaining_blocks >= lenght_of_set:
            number_of_cycles = (remaining_blocks - last_part_of_blocks) / lenght_of_set
        else: 
            number_of_cycles = 0

    return first_part_of_blocks, last_part_of_blocks, number_of_cycles      


def get_users_input():
    """
    Gets user's input: nuber of memory banks and number of blocks in every bank.
    """
    print("This is a relocation process.\n" 
            + "There are some memory banks:\n" 
            + "each memory bank can hold any number of blocks.\n" 
            + "The goal of the reallocation routine is to balance the blocks between the memory banks.\n\n")

    lenght_of_list = input("How many memory banks do you want to create?\n") 

    try:
        lenght_of_list = int(lenght_of_list)

        set_of_blocks = []

        for i in range(lenght_of_list):
            amount_of_blocks = int(input("How many blocks are in bank no. {}? \n".format(i + 1)))
            set_of_blocks.append(amount_of_blocks)

        return set_of_blocks

    except ValueError:
        print("Sorry, wrong number.")


def main():

    set_of_blocks = get_users_input()
    if set_of_blocks != None:
        count_steps(set_of_blocks)


if __name__ == '__main__':
    main()