# Maze Solver

This project implements maze-solving algorithms using both Breadth-First Search (BFS) and Depth-First Search (DFS) in Python. It can read maze configurations from text files, solve the mazes, and output the solutions both as text and as image files.

## Project Overview

The Maze Solver consists of the following main components:

1. `maze.py`: The main Python script that contains the maze-solving logic.
2. Maze text files (e.g., `maze.txt`, `maze2.txt`, `maze3.txt`): Input files that define the maze layouts.

## Features

- Reads maze configurations from text files
- Solves mazes using either Breadth-First Search (BFS) or Depth-First Search (DFS) algorithms
- Visualizes the maze and its solution in the console
- Generates image files of the maze, showing the solution path and explored areas

## Requirements

- Python 3.x
- Pillow library (for image generation)

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Install the required Pillow library:

```
pip install Pillow
```

## Usage

Run the script from the command line, providing the maze file as an argument:

```
python maze.py maze3.txt
```

Replace `maze3.txt` with the name of your maze file.

## Maze File Format

The maze is represented in a text file using the following characters:
- `#`: Wall
- `A`: Starting point
- `B`: Goal
- ` ` (space): Open path

Example:
```
##    #
## ## #
#B #  #
# ## ##
     ##
A######
```

## Code Explanation

### Main Classes

1. `Node`: Represents a state in the maze with its parent and the action taken to reach it.
2. `StackFrontier`: Implements the frontier for Depth-First Search (DFS).
3. `QueueFrontier`: Implements the frontier for Breadth-First Search (BFS).
4. `Maze`: The main class that handles maze operations, including reading the maze, solving it, and generating output.

### Key Methods

- `Maze.__init__`: Reads the maze file and initializes the maze structure.
- `Maze.solve`: Implements the search algorithm (BFS or DFS) to find the solution.
- `Maze.neighbors`: Finds valid neighboring cells for a given state.
- `Maze.output_image`: Generates an image representation of the maze and its solution.

### Solving Algorithms

The maze can be solved using either BFS or DFS:

1. Breadth-First Search (BFS):
   - Uses a queue to explore nodes in order of their distance from the start.
   - Guarantees the shortest path solution.
   - Implemented using the `QueueFrontier` class.

2. Depth-First Search (DFS):
   - Uses a stack to explore as far as possible along each branch before backtracking.
   - May not find the shortest path, but can be more memory-efficient.
   - Implemented using the `StackFrontier` class.

The choice between BFS and DFS is determined by which frontier class is used in the `Maze.solve` method.

## Output

The script provides two types of output:
1. Console output: Shows the maze layout and solution path using ASCII characters.
2. Image output: Generates a PNG file (`maze3.png`) visualizing the maze, solution path, and explored areas.

## Customization

You can create your own maze files following the format described above. Ensure that there is exactly one start point (A) and one goal point (B) in the maze.

To switch between BFS and DFS, modify the `frontier` initialization in the `Maze.solve` method:
- For BFS: `frontier = QueueFrontier()`
- For DFS: `frontier = StackFrontier()`

## Troubleshooting

If you encounter any issues:
- Ensure all required libraries are installed.
- Check that the maze file is in the correct format and in the same directory as the script.
- Verify that there is a valid path from the start to the goal in your maze.

## Contributing

Feel free to fork this project and submit pull requests with improvements or additional features.
