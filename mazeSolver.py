import argparse

# Initialize the parser
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Command line maze solver"
    )

# Read the inputs from the input.js file
inputFile = open("input.txt", "r")
probArr = []
for line in inputFile.readlines():
    probArr.append([int(i) for i in line.rstrip().split(" ")])

# Maze size
N = len(probArr)

# Add parameters
parser.add_argument('-i', '--input', help="Input file name",
                    default="input.txt")
parser.add_argument(
    '-o', '--output', help="Output file name", default="output.txt")
parser.add_argument('-d1', '--destination1',
                    help="Custom destination 1 for maze", default=N)
parser.add_argument('-d2', '--destination2',
                    help="Custom destination 2 for maze", default=N)

args = parser.parse_args()

d1 = int(args.destination1)
d2 = int(args.destination2)


# Check if matrix is square matrix
def checkValidMatrix():
    for i in probArr:
        if len(i) != N:
            print("Invalid maze. Please enter a square shaped maze")
            return False
        return True

# # A function to print and write to output.txt
#  solution matrix solMat


def printSolution(solMat):

    f = open("output.txt", "w")
    print("Path exists")
    for i in solMat:
        for j in i:
            f.writelines(str(j) + " ")
            print(str(j) + " ", end="")
        print("")
        f.write("\n")

# # A function to check if x, y is valid
# # index for N * N Maze


def indexInRange(maze, x, y):
    if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1:
        return True

    return False

# Parent function to recursive function to solve the maze


def solveMaze(maze):

    if not checkValidMatrix():
        return

    if d1 > N or d2 > N:
        print("Index out of range, try with smaller indexes")
        return

    # Creating a N * N 2-D list with 0s
    solMat = [[0 for j in range(N)] for i in range(N)]
    if solveMazeRec(maze, 0, 0, solMat) == False:
        print("Solution doesn't exist")
        return False

    printSolution(solMat)
    return True

# Recursively solving the matrix


def solveMazeRec(maze, x, y, solMat):
    if x == d1 - 1 and y == d2 - 1:
        solMat[x][y] = 1
        return True

    if indexInRange(maze, x, y) == True:

        solMat[x][y] = 1
        if solveMazeRec(maze, x + 1, y, solMat) == True:
            return True

        if solveMazeRec(maze, x, y + 1, solMat) == True:
            return True

        solMat[x][y] = 0
        return False


solveMaze(probArr)
