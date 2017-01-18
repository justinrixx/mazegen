import mazegen
import ant
import sys
import time

num_rows = 10
num_cols = 10
num_cycles = 7
num_ants = 6


def main(argv):
    maze = mazegen.gen_maze(num_rows, num_cols, num_cycles)
    edges = gen_edges(num_rows, num_cols)
    ant_positions = []

    # make a bunch of ants
    ants = []
    for i in range(0, num_ants):
        a = ant.Ant(maze, edges)
        ants.append(a)

    while True:
        ant_positions = [[False for col in range(num_cols)] for row in range(num_rows)]
        for a in ants:
            a.step(ant_positions)
        print_maze(maze, ant_positions)
        time.sleep(.5)


def gen_edges(rows, cols):
    edges = []

    for i in range(0, (rows * 2) - 1):

        # add as many rows as there need to be
        row = []

        if i % 2 == 0:
            size = cols - 1
        else:
            size = cols

        # add each item into the new array
        for j in range(0, size):
            row.append(1.0)

        edges.append(row)

    return edges


def print_maze(maze, ants):
    s = ""

    for i in range(0, len(maze)):

        # +--+--+--+  +--+  +--+
        for j in range(0, len(maze[i])):
            s += '+'
            if maze[i][j].up:
                s += '--'
            else:
                s += '  '
        s += '+\n'

        # |  |    |    |  |
        for j in range(0, len(maze[i])):
            if maze[i][j].left:
                s += '|'
            else:
                s += ' '

            if ants[i][j]:
                s += '~~'
            else:
                s += '  '

        s += '|\n'

    # add a row at the bottom
    for i in range(0, len(maze[0])):
        s += '+--'
    s += '+\n'

    print(s)


if __name__ == "__main__":
    main(sys.argv)
