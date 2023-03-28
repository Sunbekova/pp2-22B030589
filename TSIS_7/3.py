
import pygame
pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Draw circle')
x, y = 100, 100
step = 20

clock = pygame.time.Clock()

running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius=25, width = 0)

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y>40: 
        y -= step
    if pressed[pygame.K_DOWN] and y<460:
        y += step
    if pressed[pygame.K_LEFT] and x>40:
        x -= step
    if pressed[pygame.K_RIGHT] and x<460:
        x += step
        

    pygame.display.flip()
    clock.tick(20)
