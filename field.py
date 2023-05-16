import pygame
from robot import robot
from path import path
from node import node

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

r1 = robot(100, 100, 0, 1)
pathing = True
moving = False
drawPath = False
drawObstacle = True
aStar = False
p1 = path(screen)
i = 0
font = pygame.font.Font('freesansbold.ttf', 32)
obstacles = []

while running:
    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")
        
        if (pathing):
            if (drawObstacle):
                pygame.draw.rect(screen, (255, 255, 255), (1195, 15, 70, 70))
            pygame.draw.rect(screen, (100, 100, 100), (1200, 20, 60, 60))
            text = font.render('O', True, "black")
            textRect = text.get_rect()
            textRect.center = (1230, 50)
            screen.blit(text, textRect)
            
            if (drawPath):
                pygame.draw.rect(screen, (255, 255, 255), (1195, 85, 70, 70))
            pygame.draw.rect(screen, (255, 165, 0), (1200, 90, 60, 60))
            text = font.render('P', True, "black")
            textRect = text.get_rect()
            textRect.center = (1230, 120)
            screen.blit(text, textRect)

            if (aStar):
                pygame.draw.rect(screen, (255, 255, 255), (1195, 155, 70, 70))
            pygame.draw.rect(screen, (255, 0, 0), (1200, 160, 60, 60))
            text = font.render('A', True, "black")
            textRect = text.get_rect()
            textRect.center = (1230, 190)
            screen.blit(text, textRect)

            for tuple in obstacles:
                pygame.draw.ellipse(screen, (150,150,150), (tuple[0], tuple[1], 5, 5))
            p1.drawPath()

            if (pygame.key.get_pressed()[pygame.K_p]):
                drawPath = True
                drawObstacle = False
                aStar = False
            if (pygame.key.get_pressed()[pygame.K_o]):
                drawPath = False
                drawObstacle = True
                aStar = False
            if (pygame.key.get_pressed()[pygame.K_a]):
                drawPath = False
                drawObstacle = False
                aStar = True

            if drawObstacle:
                px, py = pygame.mouse.get_pos()
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    if (px, py) in obstacles:
                        pass
                    else:
                        obstacles.append((px, py))

            if drawPath:
                p1.scanDraw()

                if not p1.notDrawn():
                    pathing = False
                    moving = True
                    r1.x = p1.path[0][0]
                    r1.y = p1.path[0][1]

            if aStar:
                pass

        if (moving):
            for tuple in obstacles:
                pygame.draw.ellipse(screen, (150,150,150), (tuple[0], tuple[1], 5, 5))
            p1.drawPath()
            r1.moveToPoint(screen, p1.path[i])
            if i < p1.pathLength - 1 and r1.dist(r1.pos(), p1.path[i]) < 50:
                p1.completed.append(p1.path[i])
                i += 1

        pygame.display.flip()

        clock.tick(100)
    except Exception as e:
        print(e)
        pygame.quit()

pygame.quit()