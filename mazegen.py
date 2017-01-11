import random
import sys
import cell


def main(argv):

    rows = 30
    cols = 30
    num_cycles = 0

    if len(argv) > 2:
        rows = int(argv[1])
        cols = int(argv[2])

    if len(argv) > 3:
        num_cycles = argv[3]

    maze = gen_maze(rows, cols, num_cycles)
    # print(maze)
    print_maze(maze)


def gen_maze(rows, cols, num_cycles):
    """Generate a random maze of the proper size"""
    maze = make_blank_maze(rows, cols)

    start = maze[0][0]

    gen_maze_recursive(start, maze)

    add_cycles(maze, int(num_cycles))

    return maze


def gen_maze_recursive(current, maze):
    current.visited = True

    neighbor = current.get_neighbor(maze)
    while neighbor is not None:
        # remove the wall
        remove_wall(current, maze[neighbor[0]][neighbor[1]])

        gen_maze_recursive(maze[neighbor[0]][neighbor[1]], maze)

        # make progress
        neighbor = current.get_neighbor(maze)


def print_maze(maze):
    s = ""

    for row in maze:

        # +-+-+-+ +-+ +-+
        for c in row:
            s += '+'
            if c.up:
                s += '--'
            else:
                s += '  '
        s += '+\n'

        # | |  |   | |
        for c in row:
            if c.left:
                s += '|  '
            else:
                s += '   '
        s += '|\n'

    # add a row at the bottom
    for i in range(0, len(maze[0])):
        s += '+--'
    s += '+\n'

    print(s)


def add_cycles(maze, num_cycles):
    """Add cycles to a maze that has been generated"""

    num_cycles_added = 0

    while num_cycles_added < num_cycles:
        # pick a random cell and get a neighbor
        row = random.randint(0, len(maze) - 1)
        choice = random.choice(maze[row])
        coords = choice.get_visited_neighbor(maze)
        neighbor = maze[coords[0]][coords[1]]

        if neighbor is not None and has_wall(choice, neighbor):
            remove_wall(choice, neighbor)
            num_cycles_added += 1


def remove_wall(current, neighbor):
    """Removes a wall between two cells"""

    # make sure this is a valid neighbor
    assert (current.row == neighbor.row and abs(current.col - neighbor.col) == 1) or \
           (current.col == neighbor.col and abs(current.row - neighbor.row) == 1)

    # top
    if current.row - 1 == neighbor.row and current.col == neighbor.col:
        current.up = False
        neighbor.down = False
    # right
    elif current.row == neighbor.row and current.col + 1 == neighbor.col:
        current.right = False
        neighbor.left = False
    # bottom
    elif current.row + 1 == neighbor.row and current.col == neighbor.col:
        current.down = False
        neighbor.up = False
    # left
    elif current.row == neighbor.row and current.col - 1 == neighbor.col:
        current.left = False
        neighbor.right = False

def has_wall(current, neighbor):
    """Determine if a wall exists between two cells"""

    # make sure this is a valid neighbor
    assert (current.row == neighbor.row and abs(current.col - neighbor.col) == 1) or \
           (current.col == neighbor.col and abs(current.row - neighbor.row) == 1)

    # top
    if current.row - 1 == neighbor.row and current.col == neighbor.col:
        return current.up and neighbor.down
    # right
    elif current.row == neighbor.row and current.col + 1 == neighbor.col:
        return current.right and neighbor.left
    # bottom
    elif current.row + 1 == neighbor.row and current.col == neighbor.col:
        return current.down and neighbor.up
    # left
    elif current.row == neighbor.row and current.col - 1 == neighbor.col:
        return current.left and neighbor.right

def make_blank_maze(rows, cols):
    """Construct a blank maze of the proper size"""
    maze = []

    for i in range(0, rows):
        row = []
        for j in range(0, cols):
            row.append(cell.Cell(i, j))

        maze.append(row)

    return maze


if __name__ == "__main__":
    main(sys.argv)
