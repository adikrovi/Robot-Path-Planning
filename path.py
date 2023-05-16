import pygame

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
