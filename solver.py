import pygame
from cell import Cell
from maze import Maze

class Solver:
    def __init__(self, maze):
        self.maze = maze
        self.final_path = self.a_star(self.maze.start, self.maze.goal)
        for cell in self.final_path:
            cell.IsPath = True
        self.maze.draw_cell(self.final_path)
        pygame.display.update()
    # need start index and goal index
    def a_star(self, start, goal):
        closedSet = []
        openSet = [start]
        cameFrom = {}
        gScore = {}
        for i in range(0, len(self.maze.cells)):
            gScore[i] = float('inf')
        gScore[start.Index] = 0
        fScore = {}
        for i in range(0, len(self.maze.cells)):
            fScore[i] = float('inf')
        fScore[start.Index] = self.heuristic_cost_estimate(start, goal)

        while len(openSet) > 0:
            current = self.find_lowest_fscore(openSet, fScore)
            if (self.maze.same(current, goal)):
                return self.reconstruct_path(cameFrom, current)
            
            openSet.remove(current)
            closedSet.append(current)

            neighbors = self.find_neighbors(current.Index)
            for neighbor in neighbors:

                InSet = False
                for n in closedSet:
                    if (self.maze.same(neighbor, n)):
                        InSet = True
                        break
                
                if InSet:
                    continue

                tenative_gScore = self.dist_between(gScore, current, neighbor)

                InSet = False
                for n in openSet:
                    if (self.maze.same(neighbor, n)):
                        InSet = True
                        break
                
                if not InSet:
                    openSet.append(neighbor)
                elif (tenative_gScore >= gScore[neighbor.Index]):
                    continue
                
                print (current)
                cameFrom[neighbor.Index] = current
                for i in cameFrom:
                    print ('Cell:', cameFrom[i].x, cameFrom[i].y)
                gScore[neighbor.Index] = tenative_gScore
                fScore[neighbor.Index] = gScore[neighbor.Index] + self.heuristic_cost_estimate(neighbor, goal)
    def heuristic_cost_estimate(self, start, goal):
        x = (start.x - goal.x)
        x = x * x
        y = (start.y - goal.y)
        y = y * y
        z = x + y
        return z
    def find_lowest_fscore(self, openSet, fScore):
        min = float('inf')
        minIndex = 0
        index = 0
        for cell in openSet:
            if (fScore[cell.Index] < min):
                min = fScore[cell.Index]
                minIndex = index
            index += 1
        return openSet[minIndex]
    def reconstruct_path(self, cameFrom, current):
        total_path = [current]

        while self.InList(cameFrom, current):
            current = cameFrom[current.Index]
            total_path.append(current)
        return total_path
    def find_neighbors(self, cell):
        cell = self.maze.cells[cell]
        neighbors = []
        print (cell.x, cell.y)
        if (cell.x + 1 in range(0, self.maze.width * self.maze.cell_size)):
            newCell = self.maze.find_cell_by_position(cell.x + self.maze.cell_size, cell.y)
            if (not newCell.IsWall):
                neighbors.append(newCell)
        if (cell.x - 1 in range(0, self.maze.width * self.maze.cell_size)):
            newCell = self.maze.find_cell_by_position(cell.x - self.maze.cell_size, cell.y)
            if (not newCell.IsWall):
                neighbors.append(newCell)
        if (cell.y + 1 in range(0, self.maze.height * self.maze.cell_size)):
            newCell = self.maze.find_cell_by_position(cell.x, cell.y + self.maze.cell_size)
            if (not newCell.IsWall):
                neighbors.append(newCell)
        if (cell.y - 1 in range(0, self.maze.height * self.maze.cell_size)):
            newCell = self.maze.find_cell_by_position(cell.x, cell.y - self.maze.cell_size)
            if (not newCell.IsWall):
                neighbors.append(newCell)
        return neighbors
    def dist_between(self, gScore, current, neighbor):
        return gScore[current.Index] + 1
    def InList(self, list, cell):
        for current in list:
            if (self.maze.same(self.maze.cells[current], cell)):
                return True
        return False
