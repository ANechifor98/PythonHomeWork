import sys

def main():
    lines = sys.stdin.readlines()

    par = [int(n) for n in lines[0].split()]
    hole_index = [int(n) for n in lines[1].split()]

    players = {}
    disqualifiedPlayers = []

    for line in lines[2:]:

        line = line.split()
        name = " ".join(line[:-19])
        handicap = int(line[-19])

        strokes = []
        for stroke in line[-18:]:
            try:
                strokes.append(int(stroke))
            except:
                if stroke == "X":
                    strokes.append(0)
                else:
                    disqualifiedPlayers.append(name)
                    break

        handicaps = [0] * 18

        for i in range(handicap):
            handicaps[i % 18] += 1
        hole_score = []

        for i, stroke in enumerate(strokes):
            if 0 < stroke:
                tot_score = stroke - handicaps[hole_index[i]-1]
                points = par[i] - tot_score + 2
                hole_score.append(points if points > 0 else 0)
            else:
                hole_score.append(0)

        tot_points = sum(hole_score)

        if name not in disqualifiedPlayers:
            players[name] = tot_points

    outputs = list(players.keys()) + disqualifiedPlayers
    spaces = len(max(outputs, key=len))

    for name in sorted(players, key=lambda x: players[x])[::-1]:
        print("{:>{}} : {:>2}".format(name, spaces, players[name]))

    for name in disqualifiedPlayers:
        print("{:>{}} : Disqualified".format(name, spaces))

if __name__ == '__main__':
    main()  
