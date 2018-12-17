import sys
import pygame
from pygame.locals import QUIT
from maze import Maze
from solver import Solver

# Generate "maze"
maze = Maze(100, 50, 10)
solver = Solver(maze)

# User input loop for exiting
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
