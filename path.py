import pygame
import heapq
import math
from node import node

class path:
    def __init__(self, screen):
        self.drawn = False
        self.path = []
        self.completed = []
        self.pathLength = 0
        self.screen = screen

    def notDrawn(self):
        if (pygame.key.get_pressed()[pygame.K_p] and self.pathLength > 0):
            self.toComplete = self.path
            return False
        else:
            return True
        
    def scanDraw(self):
        px, py = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if (px, py) in self.path:
                pass
            else:
                self.path.append((px, py))
                self.pathLength += 1
            
    def drawPath(self):
        for tuple in self.path:
            if tuple in self.completed:
                pygame.draw.ellipse(self.screen, (255,165,0), (tuple[0], tuple[1], 10, 10))
            else:
                pygame.draw.ellipse(self.screen, (255,255,255), (tuple[0], tuple[1], 10, 10))

    def dist(self, orig, next):
        return math.sqrt(math.pow(orig[0] - next[0], 2) + math.pow(orig[1] - next[1], 2))

    def aStar(self, start, end):
        open = [] # min heap
        closed = [] # set

        startNode = node(start[0], start[1], None, 0, self.dist(start, end))
        open.append((startNode.fCost, startNode))
        while (len(open) > 0):
            heapq.heapify(open)
            current = heapq.heappop(open)
            closed.append(current)
            current = current[1]

            if current.x == end[0] and current.y == end[1]:
                while current.x != start[0] or current.y != start[1]:
                    self.path.insert(self.pathLength, (current.x, current.y))
                    current = current.prev
                return
            
            