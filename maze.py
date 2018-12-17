import pygame
import random
from cell import Cell

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class Maze:
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.display = self.create_display()
        self.cells = self.generate_cells()
        self.start = None
        self.goal = None
        self.choose_start_and_end_cells()
        self.draw_cell(self.cells)
        pygame.display.update()
    def create_display(self):
        display = pygame.display.set_mode((self.width * self.cell_size, self.height * self.cell_size))
        display.fill((255, 255, 255))
        return display
    def generate_cells(self):
        cells = []
        index = 0
        for x in range(0, self.width):
            for y in range(0, self.height):
                wall = True if (random.randint(0, 10) <= 2) else False
                cell = Cell(x * self.cell_size, y * self.cell_size, index, wall)
                cells.append(cell)
                index += 1
        return cells
    def choose_start_and_end_cells(self):
        self.start = None
        while (self.start == None or self.start.IsWall or self.start.IsEnd):
            self.start = self.cells[random.randint(0, (self.width * self.height))]
        self.start.IsStart = True
        self.start.IsEnd = False
        self.start.IsWall = False

        self.goal = None
        while (self.goal == None or self.goal.IsWall or self.goal.IsEnd):
            self.goal = self.cells[random.randint(0, (self.width * self.height))]
        self.goal.IsStart = False
        self.goal.IsEnd = True
        self.goal.IsWall = False
    def draw_cell(self, cells):
        for i in range(0, len(cells)):
            cell = cells[i]
            color = None
            if (cell.IsWall):
                color = BLACK
            elif (cell.IsStart):
                color = GREEN
            elif (cell.IsEnd):
                color = RED
            elif (cell.IsPath):
                color = BLUE
            else:
                continue
            pygame.draw.rect(self.display, color, [cell.x, cell.y, self.cell_size, self.cell_size])
    def find_cell_by_position(self, x, y):
        for i in range(0, len(self.cells)):
            cell = self.cells[i]
            if (cell.x == x and cell.y == y):
                return self.cells[i]
    def same(self, cell_a, cell_b):
        if (cell_a.x == cell_b.x and cell_a.y == cell_b.y):
            return True
        return False