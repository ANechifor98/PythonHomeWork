def h(start, goal):
    # ensure that start and goal are valid positions
    assert "".join(sorted(start)) == " 12345678" and "".join(sorted(goal)) == " 12345678"
    
    # Work out how many tiles are out of place
    num_tiles_out_of_place = 0
    blank_making_one_num_out_of_place = 0
    i = 0
    while i < len(start):
        print(start[i], goal[i], start[i] != goal[i], start[i] != ' ' and goal[i] != ' ')
        if start[i] != goal[i]:
            if (start[i] != ' ' or goal[i] != ' '):
                blank_making_one_num_out_of_place += 1
                num_tiles_out_of_place += 1
        i += 1
    
    return num_tiles_out_of_place

if __name__ == "__main__":
    start = "87654321 "
    goal = " 12345678"
    print(h(start, goal))
