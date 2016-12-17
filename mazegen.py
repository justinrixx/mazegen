import sys
import cell


def main(argv):

    rows = 30
    cols = 30

    if len(argv) > 2:
        rows = int(argv[1])
        cols = int(argv[2])

    maze = gen_maze(rows, cols)
    # print(maze)
    print_maze(maze)


def gen_maze(rows, cols):
    """Generate a random maze of the proper size"""
    maze = make_blank_maze(rows, cols)

    start = maze[0][0]

    gen_maze_recursive(start, maze)

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
                s += '-'
            else:
                s += ' '
        s += '+\n'

        # | |  |   | |
        for c in row:
            if c.left:
                s += '| '
            else:
                s += '  '
        s += '|\n'

    # add a row at the bottom
    for i in range(0, len(maze[0])):
        s += '+-'
    s += '+\n'

    print(s)


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
