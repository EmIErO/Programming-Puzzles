L = [0, 3, 0, 1, -3] 

steps = 0
old_position = 0


while old_position <= len(L):
    try:
        new_position = old_position + L[old_position]
        L[old_position] = L[old_position] + 1
        old_position = new_position
        
        steps +=1
        
    except IndexError:
        break

print("Getting out took {} steps.".format(steps)) 