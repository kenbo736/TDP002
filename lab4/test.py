from operator import itemgetter
import glob

################################################################################
def create_wall(x, y):
    wall = ["wall", x, y]
    return wall

def create_storage(x, y):
    storage = ["storage", x, y]
    return storage

def create_box(x, y):
    box = ["box", x, y]
    return box

def create_player(x, y):
    player = ["player", x, y]
    return player

def soko_win(soko_walls, soko_boxes, soko_storage, soko_player):
    #checks if box in soko_boxes in on same place as soko_storage
    for box in soko_boxes:
        if not create_storage(box[1], box[2]) in soko_storage:
            return False
    return True

def player_can_move(direction, soko_walls, soko_boxes, soko_storage, soko_player):
    #sets a new postion of the player
    new_pos = ["player", soko_player[0][1] + direction[0], soko_player[0][2] + direction[1]]

    wall = create_wall(new_pos[1], new_pos[2])
    box = create_box(new_pos[1], new_pos[2])


    if wall in soko_walls:
        return False

    #if box exist in soko_boxes
    elif box in soko_boxes:
        second_pos = [new_pos[1] + direction[0], new_pos[2] + direction[1]]
        second_wall = create_wall(second_pos[0], second_pos[1])
        second_box = create_box(second_pos[0], second_pos[1])

        if second_box in soko_boxes or second_wall in soko_walls:
            return False

            #if something is in the way for the box can the player nor the box move
        else:
            #move box
            soko_boxes.remove(box)
            soko_boxes.append(second_box)
            #move player
            soko_player.pop(0)
            soko_player.append(new_pos)

    else:
        soko_player.pop(0)
        soko_player.append(new_pos)
        return True

    return new_pos

###############################################################################

def sokoban_display(walls, box, storage, player):
    #sorts the array and key let you decide which element to sort after
    sortedByX = sorted(walls, key = itemgetter(1))
    sortedByY = sorted(walls, key = itemgetter(2))

    #because an array starts from 0, you need to add +1 to make it correct
    w = sortedByX[-1][1]+1
    h = sortedByY[-1][2]+1

    #a list comprehension that creates an multideminsional array
    worldMap = [[0 for x in range(w)] for y in range(h)]

    #takes out the x and y values from the wall list and put it in the multidim array and sets the value as an wall
    for x1 in range(0, len(walls)):
        valueX, valueY = walls[x1][2], walls[x1][1]
        worldMap[valueX][valueY] = "#"

    for x2 in range(0, len(box)):
        valueXb, valueYb = box[x2][2], box[x2][1]
        worldMap[valueXb][valueYb] = "o"

    for x3 in range(0, len(storage)):
        valueXs, valueYs = storage[x3][2], storage[x3][1]
        worldMap[valueXs][valueYs] = "."
        for x4 in range(0, len(box)):
            #check if box in the same position as storage
            if box[x4][2] == storage[x3][2]:
                if box[x4][1] == storage[x3][1]:
                    #print("test test")
                    worldMap[valueXs][valueYs] = "*"
    soko_win(walls, box, storage, player)

    print(len(storage))
    print(len(box))

    #sets the icon of the player and postition
    pX, pY = player[0][2], player[0][1]
    worldMap[pX][pY] = "@"

    for check0 in range(0, len(worldMap)):
        for check1 in range(0, len(worldMap[check0])):
            #checks if == 0 then sets it as an whitespace
            if worldMap[check0][check1] == 0:
                worldMap[check0][check1] = " "

    # a tempt to visual the worldmap
    for check in range(0, h):
        #print(worldMap[check])
        visualMap = "".join(worldMap[check])
        print(visualMap)
    return visualMap

def sokoban_load(file_name, soko_walls, soko_boxes, soko_storage, soko_player):
    y = 0
    for line in open(file_name):
        x = 0
        for char in line:
            if char == '#':
                soko_walls.append(create_wall(x, y))
            #lägg till spelaren
            if char == '@':
                soko_player.append(create_player(x, y))
            # lägg om låda
            if char == 'o':
                soko_boxes.append(create_box(x, y))
            # lägg in lagerplats
            if char == '.':
                soko_storage.append(create_storage(x, y))

            x = x + 1
        y = y + 1
    return soko_player

def sokoban():
    soko_walls = []
    soko_boxes = []
    soko_storage = []
    soko_player = []
    run = True
    pick_way = {"a" : (-1, 0), "d" : (1, 0), "w" : (0, -1), "s" : (0, 1)}
    print("Welcome to Sokoban, please choose a level:")
    listWithMaps = glob.glob("/home/kenbo736/Courses/TDP002/u4/maps/*.sokoban")
    newList = []
    for p in range(0, len(listWithMaps)):
        newList.append(listWithMaps[p][33:])
        print(str(p+1) + ". " + str(listWithMaps[p][38:-8]))
    levelNumber = int(input("Choose: "))
    nameOfMap = newList[levelNumber-1]
    sokoban_load(nameOfMap, soko_walls, soko_boxes, soko_storage, soko_player)
    sokoban_display(soko_walls, soko_boxes, soko_storage, soko_player)
    while run:
        direction = input("Choose direction(a, s, d, w): ")
        if direction == "quit":
            run = False

        if direction in pick_way:
            player_can_move(pick_way[direction], soko_walls, soko_boxes, soko_storage, soko_player)
            print(soko_player)
            sokoban_display(soko_walls, soko_boxes, soko_storage, soko_player)

        if soko_win(soko_walls, soko_boxes, soko_storage, soko_player):
            run = False
            print("Congratulations! you completed level " + "'" + str(nameOfMap[5:-8]) + "'")

#saved_map()
#sokoban_load("maps/easy.sokoban")
#all_lists()
sokoban()
#sokoban_display(soko_walls, soko_boxes, soko_storage, soko_player)
