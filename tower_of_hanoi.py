
def printTowers(towers):
    counter = 0
    for tower in towers:
        counter += 1
        print("tower", counter, ":", "".join(str(tower)))
    print("\n")

#move the top(last) item from towers[target] to towers[dest]
#Example: towers_move_top(towers, 1, 2) will move 1st tower's top to 2nd tower's top.
def towers_move_top(towers, target, dest):
    towers[dest].append(towers[target].pop())
    printTowers(towers)

def tower_of_hanoi(n):
    if n < 1: return
    towers = [[], [], []]
    orderQueue = []
    for i in range(n,0,-1):
        towers[0].append(i)
    print("-------------------\nStart of the tower")
    printTowers(towers)
    print("-------------------")
    while len(towers[0]) > 0:
        new_val = towers[0][-1]
        if len(towers[1]) == 0: 
            towers_move_top(towers, 0, 1)
        else: 
            towers_move_top(towers, 0, 2)
        orderQueue.append(new_val)
        while len(towers[1]) != len(orderQueue) and len(towers[2]) != len(orderQueue):
            cur_node = orderQueue[0]
            if len(towers[1]) > 0 and cur_node == towers[1][-1]:
                if len(towers[2]) > 0 and (cur_node & 1) != (towers[2][-1] & 1) and cur_node < towers[2][-1]:
                    towers_move_top(towers, 1, 2)
                elif len(towers[0]) > 0 and (cur_node & 1) != (towers[0][-1] & 1) and cur_node < towers[0][-1]: 
                    towers_move_top(towers, 1, 0)
                elif len(towers[2]) == 0:
                    towers_move_top(towers, 1, 2)
                elif len(towers[0]) == 0:
                    towers_move_top(towers, 1, 0)
            elif len(towers[2]) > 0 and cur_node == towers[2][-1]:
                if len(towers[1]) > 0 and (cur_node & 1) != (towers[1][-1] & 1) and cur_node < towers[1][-1]: 
                    towers_move_top(towers, 2, 1)
                elif len(towers[0]) > 0 and (cur_node & 1) != (towers[0][-1] & 1) and cur_node < towers[0][-1]: 
                    towers_move_top(towers, 2, 0)
                elif len(towers[1]) == 0:
                    towers_move_top(towers, 2, 1)
                elif len(towers[0]) == 0:
                    towers_move_top(towers, 2, 0)
            elif len(towers[0]) > 0 and cur_node == towers[0][-1]:
                if len(towers[1]) > 0 and (cur_node & 1) != (towers[1][-1] & 1) and cur_node < towers[1][-1]: 
                    towers_move_top(towers, 0, 1)
                elif len(towers[2]) > 0 and (cur_node & 1) != (towers[2][-1] & 1) and cur_node < towers[2][-1]: 
                    towers_move_top(towers, 0, 2)
                elif len(towers[1]) == 0:
                    towers_move_top(towers, 0, 1)
                elif len(towers[2]) == 0:
                    towers_move_top(towers, 0, 2)
            orderQueue.append(orderQueue.pop(0))
    print("-------------------\nEnd of the tower")
    printTowers(towers)
    print("-------------------")
    return

tower_of_hanoi(10)