import random


class Cell:
    """A single cell in a maze"""

    def __init__(self, row, col):
        self.visited = False
        self.left = True
        self.right = True
        self.up = True
        self.down = True
        self.row = row
        self.col = col

    def get_all_neighbors(self, maze):
        """Get a list of all the neighbors to this cell"""
        neighbors = []

        # top
        if self.row - 1 > -1:
            neighbors.append((self.row - 1, self.col))

        # right
        if self.col + 1 < len(maze[0]):
            neighbors.append((self.row, self.col + 1))

        # bottom
        if self.row + 1 < len(maze):
            neighbors.append((self.row + 1, self.col))

        # left
        if self.col - 1 > -1:
            neighbors.append((self.row, self.col - 1))

        return neighbors

    def get_all_unvisited_neighbors(self, maze):
        """Get a list of all the neighbors to this cell"""
        neighbors = []

        # top
        if self.row - 1 > -1 and not maze[self.row - 1][self.col].visited:
            neighbors.append((self.row - 1, self.col))

        # right
        if self.col + 1 < len(maze[0]) and not maze[self.row][self.col + 1].visited:
            neighbors.append((self.row, self.col + 1))

        # bottom
        if self.row + 1 < len(maze) and not maze[self.row + 1][self.col].visited:
            neighbors.append((self.row + 1, self.col))

        # left
        if self.col - 1 > -1 and not maze[self.row][self.col - 1].visited:
            neighbors.append((self.row, self.col - 1))

        return neighbors

    def get_neighbor(self, maze):
        """Pick a random neighbor to return"""

        neighbors = self.get_all_unvisited_neighbors(maze)

        if not neighbors:
            return None
        else:
            return random.choice(neighbors)

    def get_visited_neighbor(self, maze):
        """Pick a random neighbor to return. Doesn't matter if it's been visited before."""

        neighbors = []

        # top
        if self.row - 1 > -1:
            neighbors.append((self.row - 1, self.col))

        # right
        if self.col + 1 < len(maze[0]):
            neighbors.append((self.row, self.col + 1))

        # bottom
        if self.row + 1 < len(maze):
            neighbors.append((self.row + 1, self.col))

        # left
        if self.col - 1 > -1:
            neighbors.append((self.row, self.col - 1))

        if not neighbors:
            return None
        else:
            return random.choice(neighbors)
