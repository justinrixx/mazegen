import random


class Ant:
    def __init__(self, maze):
        # starting location
        self.i = 0
        self.j = 0

        self.memory = []

        # am i moving forward or backward?
        self.forward = True

    def step(self, maze):
        """Moves the ant to the next cell. Could be looking for food, could be returning home"""

        # at the goal
        # if self.i == food_location.i and self.j == food_location.j:
        #     self.forward = False

        if self.forward:
            path = self.choose_path(maze)

            # cycle removal
            if path in self.memory:
                for i in range(self.memory.index(path) + 1, len(self.memory) + 1):
                    del self.memory[i]
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

    def choose_path(self, maze):
        """Choose the path to follow this step"""
        return 0, 0
