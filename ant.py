import numpy as np


class Ant:
    def __init__(self, maze, edges):
        # starting location
        self.i = 0
        self.j = 0

        self.memory = [(0, 0)]

        # am i moving forward or backward?
        self.forward = True

        self.maze = maze
        self.edges = edges

    def step(self, positions):
        """Moves the ant to the next cell. Could be looking for food, could be returning home"""

        # at the goal
        if self.i == len(self.maze) - 1 and self.j == len(self.maze[0]) - 1:
            self.forward = False

            # lay down pheromone
            fitness = 1 / len(self.memory)
            for i in range(1, len(self.memory)):
                coords = get_edge(self.memory[i - 1][0], self.memory[i - 1][1],
                                      self.memory[i][0], self.memory[i][1])

                self.edges[coords[0]][coords[1]] += fitness

        if self.forward:
            path = self.choose_path()

            # cycle removal
            if path in self.memory:
                location = self.memory.index(path)
                for i in range(location + 1, len(self.memory)):
                    del self.memory[location + 1]

                self.i, self.j = path
            # move on
            else:
                self.memory.append(path)
                self.i, self.j = path

        else:
            path = self.memory.pop()
            self.i, self.j = path

            # go forward again if it's time
            if len(self.memory) == 0:
                self.forward = True

        positions[self.i][self.j] = True

    def choose_path(self):
        """Choose the path to follow this step"""
        neighbors = self.maze[self.i][self.j].get_all_neighbors(self.maze)

        choices = {}
        total = 0.0
        for n in neighbors:
            edge = get_edge(self.i, self.j, n[0], n[1])
            choices[n] = self.edges[edge[0]][edge[1]]

            total += self.edges[edge[0]][edge[1]]

        items = []
        probs = []
        for k, v in choices.items():
            items.append(k)
            probs.append(v / total)

        return items[np.random.choice(range(0, len(items)), p=probs)]


def get_edge(r1, c1, r2, c2):
    """Get the indices of an edge based on the starting and ending positions"""
    # figure out the direction
    if r1 == r2 and c1 == c2 + 1:
        # left
        return r1 * 2, c1 - 1
    elif r1 == r2 and c1 + 1 == c2:
        # right
        return r1 * 2, c1
    elif r1 == r2 + 1 and c1 == c2:
        # up
        return r1 * 2 - 1, c1
    elif r1 + 1 == r2 and c1 == c2:
        # down
        return r1 * 2 + 1, c1
    else:
        assert False
