
m = [5, 1, 10, 0, 1, 7, 13, 14, 3, 12, 8, 10, 7, 12, 0, 6]
set_of_blocks = [1, 1, 14, 13, 12, 11, 10, 9, 8, 7, 7, 5, 5, 3, 3, 0]


def count_steps(set_of_blocks):
    all_redistributions = []
    steps = 0
    copy_of_set = set_of_blocks[:]
    all_redistributions.append(copy_of_set)

    while set_of_blocks:
        
        
        if lenght >= blocks_to_distribiute:
            banks_to_end = lenght - 1 - mb_index
            
            if banks_to_end >= blocks_to_distribiute:
                end_of_iteration = mb_index + blocks_to_distribiute + 1
                for i in range(mb_index + 1, end_of_iteration):
                    l[i] = l[i] + 1
            
            else:
                part_one = lenght - 1 - mb_index
                part_two = blocks_to_distribiute - part_one
                for i in range(mb_index + 1, len(l)):
                    l[i] = l[i] + 1
                for i in range(part_two):
                    l[i] = l[i] + 1
                    
        if l in all:
            steps += 1
            print("yay!")
            print(steps)
            print(l)
            break
        else:
            t = l[:]
            all_redistributions.append(t)
            steps += 1

def distribute_blocks(set_of_blocks, blocks_to_distribiute):
    
    lenght_of_set = len(set_of_blocks)

    blocks_to_distribiute = max(set_of_blocks)
    blocks_to_distribiute_index = set_of_blocks.index(blocks_to_distribiute)

    set_of_blocks[blocks_to_distribiute_index] = 0

    first_part_of_blocks, last_part_of_blocks, number_of_cycles = divide_blocks_to_distribiute(lenght_of_set, 
                                                                                                blocks_to_distribiute_index, 
                                                                                                blocks_to_distribiute)
    
    if last_part_of_blocks == 0 and number_of_cycles == 0:
        end_of_iteration = blocks_to_distribiute_index + blocks_to_distribiute + 1

        for i in range(blocks_to_distribiute_index + 1, end_of_iteration):
            set_of_blocks[i] = set_of_blocks[i] + 1
    
    elif: last_part_of_blocks != 0:
        
        for i in range(blocks_to_distribiute_index + 1, lenght_of_set):
            set_of_blocks[i] = set_of_blocks[i] + 1
        for i in range(last_part_of_blocks):
            set_of_blocks[i] = set_of_blocks[i] + 1

        if number_of_cycles != 0:
            for i in range

def divide_blocks_to_distribiute(lenght_of_set, blocks_to_distribiute_index, blocks_to_distribiute):
   
    spots_till_end_of_list = lenght_of_set - blocks_to_distribiute_index - 1

    if spots_till_end_of_list >= blocks_to_distribiute:
        first_part_of_blocks = blocks_to_distribiute
        last_part_of_blocks = 0
        number__of_cycles = 0

    else:
        first_part_of_blocks = spots_till_end_of_list
        remaining_spots = blocks_to_distribiute - first_part_of_blocks
        last_part_of_blocks = lenght_of_set % remaining_spots
        
        if remaining_spots > lenght_of_set:
            number_of_cycles = (remaining_spots - last_part_of_blocks) / lenght_of_set
        else: 
            number_of_cycles = 0

    return first_part_of_blocks, last_part_of_blocks, number__of_cycles      

