import pygame
import math

class robot:
    def __init__(self, x, y, dir, speed):
        self.x = x
        self.y = y
        self.dir = dir
        self.speed = speed
        self.turnSpeed = 0.05

    def draw(self, screen):
        pygame.draw.rect(screen, "white", (self.x, self.y, 30, 30))
        pygame.draw.line(screen, "red", (self.x + 15, self.y + 15), (self.x + 15 + (math.cos(self.dir) * 30), self.y + 15 - (math.sin(self.dir) * 30)), 2)

    def pos(self):
        return (self.x, self.y)

    def moveControl(self, screen):
        if (pygame.key.get_pressed()[pygame.K_w]):
            self.x += math.cos(self.dir) * self.speed
            self.y -= math.sin(self.dir) * self.speed
        if (pygame.key.get_pressed()[pygame.K_s]):
            self.x -= math.cos(self.dir) * self.speed
            self.y += math.sin(self.dir) * self.speed
        if (pygame.key.get_pressed()[pygame.K_d]):
            if (self.dir - self.turnSpeed < 0):
                self.dir = (2 * math.pi) + (self.dir - self.turnSpeed)
            else:
                self.dir -= self.turnSpeed
        if (pygame.key.get_pressed()[pygame.K_a]):
            if (self.dir + self.turnSpeed > (2 * math.pi)):
                self.dir = (self.dir + self.turnSpeed) - (2 * math.pi)
            else:
                self.dir += self.turnSpeed
        self.draw(screen)

    def turn(self, amt):
        if (amt < 0):
            amt = abs(amt)
            if (self.dir - amt < 0):
                self.dir = (2 * math.pi) + (self.dir - amt)
            else:
                self.dir -= amt
        elif (amt > 0):
            if (self.dir + amt > (2 * math.pi)):
                self.dir = (self.dir + amt) - (2 * math.pi)
            else:
                self.dir += amt
        else:
            pass

    def move(self, amt):
        self.x += math.cos(self.dir) * amt
        self.y -= math.sin(self.dir) * amt

    def dist(self, orig, next):
        return math.sqrt(math.pow(orig[0] - next[0], 2) + math.pow(orig[1] - next[1], 2))
    
    def findAng(self, point):
        dY = abs(point[1] - self.y)
        dX = abs(point[0] - self.x)

        if (dX != 0 and dY != 0):
            desAng = math.atan(dY / dX)
            if (point[1] > self.y and point[0] > self.x):
                desAng = (2 * math.pi) - desAng
            elif (point[1] < self.y and point[0] > self.x):
                desAng = desAng
            elif (point[1] > self.y and point[0] < self.x):
                desAng = math.pi + desAng
            elif (point[1] < self.y and point[0] < self.x):
                desAng = math.pi - desAng
        else:
            if (dX == 0):
                if (point[1] > self.y):
                    desAng = (3/2) * math.pi
                else:
                    desAng = (1/2) * math.pi
            elif (dY == 0):
                if (point[0] > self.x):
                    desAng = 0
                else:
                    desAng = math.pi

        return desAng

    def moveToPoint(self, screen, point):
        if (abs(self.y - point[1]) <= 10 and abs(self.x - point[0]) <= 10):
            self.draw(screen)
            return False

        dist = self.dist((self.x, self.y), point)

        desAng = self.findAng(point)
        dAng = desAng - self.dir
        if (dAng > math.pi):
            dAng -= math.pi
            dAng *= -1
        elif (dAng < -1 * math.pi):
            dAng += math.pi
            dAng *= -1

        if dist > 10:
            self.move(self.speed)
        else:
            self.move((self.speed / 10) * (dist / 50))
        if (dAng != 0):
            self.turn((self.turnSpeed / 2) * (dAng / abs(dAng)))

        self.draw(screen)
        pygame.draw.circle(screen, "green", point, 3)
        return True