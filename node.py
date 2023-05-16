import pygame

class node:
    def __init__(self, x, y, prev, gCost, hCost):
        self.x = x
        self.y = y
        self.prev = prev
        self.gCost = gCost
        self.hCost = hCost
        self.fCost = gCost + hCost

    