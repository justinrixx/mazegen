# mazegen
A simple maze generator in Python

# Usage
`python3 mazegen.py` will generate a maze of the default size (10x10)

`python3 mazegen.py <rows> <cols>` will generate a maze with `<rows>` rows and `<cols>` columns

The mazes are generated using backtracking and depth-first search. Learn more [here](https://en.wikipedia.org/wiki/Maze_generation_algorithm#Recursive_backtracker)

# Samples
A 10x20 maze

```
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
|  |        |     |           |                 |           |
+  +  +  +  +--+  +  +--+  +  +  +  +--+--+--+  +--+--+  +  +
|  |  |  |     |  |  |     |  |  |     |        |     |  |  |
+  +--+  +--+  +  +  +  +--+  +  +--+  +  +--+--+  +  +--+  +
|     |  |     |     |  |  |  |     |  |           |     |  |
+--+  +  +--+  +--+--+  +  +  +--+  +  +--+--+--+--+--+  +  +
|     |     |        |  |  |     |  |     |     |     |     |
+  +--+  +  +--+--+  +  +  +--+  +--+  +  +  +  +--+  +--+  +
|  |  |  |     |        |     |     |  |     |     |     |  |
+  +  +  +--+  +--+--+--+  +--+--+  +  +--+--+--+  +  +  +  +
|  |  |     |           |        |  |        |     |  |     |
+  +  +--+  +--+--+--+  +  +--+  +  +--+--+--+  +--+  +--+--+
|  |           |        |     |     |           |  |  |     |
+  +  +--+--+--+  +--+--+--+  +--+--+  +--+--+--+  +  +  +--+
|  |  |  |     |     |     |  |     |  |        |     |     |
+  +  +  +  +  +--+  +  +  +  +  +  +  +  +--+  +  +--+--+  +
|  |     |  |        |  |  |     |     |  |  |  |        |  |
+  +--+--+  +--+--+--+  +  +--+--+--+--+  +  +  +--+--+  +  +
|           |           |                    |              |
+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+

```
