import curses
from curses import wrapper
import queue
import time

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]


def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, j*2 , "X", RED)

            else:
                stdscr.addstr(i, j*2 , value, BLUE)

def findStart(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j


def findPath(maze, stdscr):
    start = "O"
    end = "X"
    startPos = findStart(maze, start)

    q = queue.Queue()
    q.put((startPos, [startPos]))

    visited = set()

    while not q.empty():
        currentPos, path = q.get()
        row, col = currentPos

        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.2)
        stdscr.refresh

        if maze [row][col] == end:
            return path
        
        neighbors = findNeighbors(maze, row, col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue

            r, c = neighbors
            if maze[r][c] == "#":
                continue

            newPath = path + [neighbor]
            q.put((neighbor, newPath))
            visited.add(neighbor)
        
def findNeighbors (maze, row, col):
    neighbors = []

    if row > 0: #UP
        neighbors.append((row - 1, col))
    if row + 1 < len(maze): #DOWN
        neighbors.append((row + 1, col))
    if col > 0: #LEFT
        neighbors.append((row, col - 1))
    if col + 1 < len(maze[0]): #RIGHT
        neighbors.append((row, col + 1))

        return neighbors

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    findPath(maze, stdscr)
    stdscr.getch()

wrapper(main)
