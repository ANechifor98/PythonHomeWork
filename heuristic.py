def h(start, goal):
    assert "".join(sorted(start)) == " 12345678" and "".join(sorted(goal)) == " 12345678"
    
    # Work out the manhattab h distance of each tile from its eventual goal
    
    matrix_of_start = [start[i:i+3] for i in range(0, len(start), 3)][::-1]
    matrix_of_goal = [goal[i:i+3] for i in range(0, len(goal), 3)][::-1]

    #create dictionaries of start and goal coordinates
    d_start = {}
    d_goal = {}
    for i in matrix_of_start:
        for c in i:
            d_start[c] = (matrix_of_start.index(i),i.index(c))

    for i in matrix_of_goal:
        for c in i:
            d_goal[c] = (matrix_of_goal.index(i),i.index(c))

    #k is number(or blank) tile, v is tuple of the coordinates of the tile
    manhattan_distance = 0
    for k, v in d_start.items():
        #set coordinates of tiles
        x1 = v[0]
        y1 = v[1]
        x2 = d_goal[k][0]
        y2 = d_goal[k][1]
        if not (k == ' '):
            manhattan_distance += abs(x1-x2) + abs(y1-y2)
    return manhattan_distance
