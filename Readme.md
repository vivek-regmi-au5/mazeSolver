# A command line program to solve a maze problem.

![alt maze](https://qph.fs.quoracdn.net/main-qimg-0b8475b24fb396bcaca4dbece5a5c02a.webp)

A maze is a path or collection of paths, typically from an entrance to a goal. The word is used to refer both to branching tour puzzles through which the solver must find a route, and to simpler non-branching ("unicursal") patterns that lead unambiguously through a convoluted layout to a goal. (The term "labyrinth" is generally synonymous with "maze", but can also connote specifically a unicursal pattern.) The pathways and walls in a maze are typically fixed, but puzzles in which the walls and paths can change during the game are also categorised as mazes or tour puzzles.

Here is a program to solve a maze using python language. Here we take a matrix of numbers 1 and 0 as input. 1 represents a possible path and 0 represents blocked path. I have used DFS approach to solve this maze problem.
As output, I have create a output.txt file which draws a path(if exists) from startring position to ending position with 1. If path doesn't exists, it outputs "Path doesn't exists in the terminal".

### Command to initialize program

```
python3 mazeSolver.py
```

To give inputs, you can modiify input.txt file

Output will be displayed in output.txt file

It has default arguments of input file as input.txt and output file as output.txt.
`python3 mazeSolver.py -i input.txt -o output.txt`
The command also accepts two arguments as d1 and d2 which represents the destination index of the matrix you want to find the path to. d1 and d2 represents x and y index respectively
`python3 mazeSolver.py -i input.txt -o output.txt -d1 3 -d2 3`
The default value for d1 and d2 is length of the input matrix.

It also checks for a valid matrix, if you provide an invalid matrix, it will show you an error.
If you provide an invalid matrix, for example you missed a number in the row or column, then it
will print an error message on the terminal.
