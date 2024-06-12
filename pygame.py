import pygame
import random

height = 500
width = 500

xc = 20
yc = 200

xb = 100
yb = 100

i = 0

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))

def ball(xc, yc):
    ball1 = pygame.draw.circle(screen, (255, 0, 0), (xc, yc), 10)
    
def box():
    box1 = pygame.draw.line(screen, (0, 255, 0), (xb, yb), (xb, yb+ 10), 20)
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    if xc == xb and yc == yb:
        xb = random.randrange(100, 470, 8)
        yb = random.randrange(100, 470, 8)
        
    if xc < xb:
        xc +=2
        
    if xc > xb:
        xc -= 2
        
    if yc > yb:
        yc -= 2
        
    if yc < yb:
        yc += 2
        
    screen.fill((0, 100, 150))
    ball(xc, yc)
    box()
    clock.tick(60)
    pygame.display.update()
exit()
    
