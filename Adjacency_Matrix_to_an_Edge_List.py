def make_edge_list(adjacency):
    """ this function create an edge list representation of a graph using the supplied adjacency matrix
    """
    # Maybe start with an empty edge_list
    edge_list = []
    i = 0
    while i < len(adjacency):
        letterlist = []
        j = 0
        while j < len(adjacency[i]):
            num = j
            letter = chr(ord("A") + num)
            if adjacency[i][j] == 1:
                letterlist.append(letter)
            j += 1
        edge_list.append(letterlist)
        i += 1
    return edge_list

if __name__ == "__main__":
    adjacency = [
[0, 1, 1],
[1, 0, 0],
[1, 0, 0],
]
    print(make_edge_list(adjacency))
