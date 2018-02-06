def count_steps(set_of_blocks):

    all_redistributions = []
    steps = 0
    copy_of_set = set_of_blocks[:]
    all_redistributions.append(copy_of_set)

    while set_of_blocks:

        set_of_blocks = distribute_blocks(set_of_blocks)
                    
        if set_of_blocks in all_redistributions:
            steps += 1
            print("This configuration appears for the second time:\n")
            print(set_of_blocks)
            print("\nIt took {} steps.".format(steps))
            break
        else:
            copy_of_set = set_of_blocks[:]
            all_redistributions.append(copy_of_set)
            steps += 1


def distribute_blocks(set_of_blocks):
    
    lenght_of_set = len(set_of_blocks)

    blocks_to_distribiute = max(set_of_blocks)
    print(blocks_to_distribiute)
    blocks_to_distribiute_index = set_of_blocks.index(blocks_to_distribiute)

    set_of_blocks[blocks_to_distribiute_index] = 0

    first_part_of_blocks, last_part_of_blocks, number_of_cycles = divide_blocks_to_distribiute(lenght_of_set, 
                                                                                                blocks_to_distribiute_index, 
                                                                                                blocks_to_distribiute)

    if last_part_of_blocks == 0 and number_of_cycles == 0:
        end_of_iteration = blocks_to_distribiute_index + blocks_to_distribiute + 1

        for i in range(blocks_to_distribiute_index + 1, end_of_iteration):
            set_of_blocks[i] = set_of_blocks[i] + 1
    
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
   
    spots_till_end_of_list = lenght_of_set - blocks_to_distribiute_index - 1

    if spots_till_end_of_list >= blocks_to_distribiute:
        first_part_of_blocks = blocks_to_distribiute
        last_part_of_blocks = 0
        number_of_cycles = 0

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

    print("This is a relocation process.\n" 
            + "There are some memory banks:\n" 
            + "each memory bank can hold any number of blocks.\n" 
            + "The goal of the reallocation routine is to balance the blocks between the memory banks.\n\n")

    lenght_of_list = input("How many memory banks do you want to create?\n") 

    try:
        lenght_of_list = int(lenght_of_list)

    except ValueError:
        print("Sorry, wrong number.")

    set_of_blocks = []

    for i in range(lenght_of_list):
        amount_of_blocks = int(input("How many blocks are in bank no. {}? \n".format(i + 1)))
        set_of_blocks.append(amount_of_blocks)

    return set_of_blocks


def main():

    set_of_blocks = get_users_input()
    count_steps(set_of_blocks)


if __name__ == '__main__':
    main()