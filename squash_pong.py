"""
A sqash version of the classic pong game

@author: Mathew Charath
"""

import pygame

pygame.init()

WIDTH = 1500
HEIGHT = 900
BORDER = 20
VELOCITY = 1

bgColor = pygame.Color("black")
borderColor = pygame.Color("yellow")
paddleColor = pygame.Color("blue")
ballColor = pygame.Color("red")

gameOver = False

class Ball:

    RADIUS = 25

    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def show(self, color):
        global SCREEN
        pygame.draw.circle(SCREEN, color, (self.x, self.y), self.RADIUS)

    def updatePosition(self):
        global ballColor, bgColor

        nextXpos = self.x + self.vx
        nextYpos = self.y + self.vy

        if nextXpos < BORDER + self.RADIUS:
            self.vx = -self.vx
        elif nextYpos < BORDER + self.RADIUS or nextYpos > HEIGHT - (BORDER + self.RADIUS):
            self.vy = -self.vy
        elif nextXpos + self.RADIUS > WIDTH - (2 * pongPaddle.WIDTH) and abs(nextYpos-pongPaddle.y) < pongPaddle.HEIGHT:
            self.vx = -self.vx
        elif nextXpos + self.RADIUS > WIDTH - BORDER:
            global gameOver
            gameOver = True
        else:
            self.show(bgColor)
            self.x = self.x + self.vx
            self.y = self.y + self.vy
            self.show(ballColor)

class Paddle:
    
    WIDTH = 20
    HEIGHT = 150

    def __init__(self, y):
        self.y = y
    
    def show(self, color):
        global SCREEN
        pygame.draw.rect(SCREEN, color, pygame.Rect(WIDTH-(2*self.WIDTH), self.y, self.WIDTH, self.HEIGHT))

    def updatePosition(self):
        global bgColor, paddleColor
        self.show(bgColor)
        self.y = pygame.mouse.get_pos()[1]
        self.show(paddleColor)
    

# defining a ball for the game session
# (HEIGHT//2) returns an integer rather than a float. This is done because pygame.draw.circle() does not accept floating point values
pongBall = Ball(WIDTH - (4 * Ball.RADIUS), HEIGHT//2, -VELOCITY, -VELOCITY)
pongPaddle = Paddle(HEIGHT//4)


SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.draw.rect(SCREEN, borderColor, pygame.Rect(0, 0, WIDTH - (2 * Paddle.WIDTH), BORDER))
pygame.draw.rect(SCREEN, borderColor, pygame.Rect(0, 0, BORDER, WIDTH))
pygame.draw.rect(SCREEN, borderColor, pygame.Rect(0, HEIGHT-BORDER, WIDTH - (2 * Paddle.WIDTH), BORDER))
pygame.draw.rect(SCREEN, ballColor, pygame.Rect(WIDTH-BORDER, 0, BORDER, HEIGHT))

pongBall.show(ballColor)
pongPaddle.show(paddleColor)


while not gameOver:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break
    
    pygame.display.flip()

    pongPaddle.updatePosition()
    pongBall.updatePosition()

print("game over")
pygame.quit()
