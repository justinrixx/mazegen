import mazegen
import ant
import sys

num_rows = 10
num_cols = 10
num_cycles = 7
num_ants = 6


def main(argv):
    maze = mazegen.gen_maze(num_rows, num_cols, num_cycles)
    edges = gen_edges(num_rows, num_cols)

    # make a bunch of ants
    ants = []
    for i in range(0, num_ants):
        a = ant.Ant(maze, edges)
        ants.append(a)

    while True:
        for a in ants:
            a.step()
        mazegen.print_maze(maze)


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


if __name__ == "__main__":
    main(sys.argv)
