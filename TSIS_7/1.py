import pygame
import datetime

pygame.init()
clock = pygame.time.Clock()

screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Clock")

fon = pygame.image.load("backgr.png")
fon = pygame.transform.scale(fon, (screen_width, screen_height))

minute_hand = pygame.image.load("min.png")
minute_hand = pygame.transform.scale(minute_hand, (300, 200))

second_hand = pygame.image.load("sec.png")
second_hand = pygame.transform.scale(second_hand, (300, 200))

def update_hands(current_time):
    minute_angle = (current_time.minute / 60) * 360
    rotated_minute_hand = pygame.transform.rotate(minute_hand, -minute_angle)
    
    second_angle = (current_time.second / 60) * 360
    rotated_second_hand = pygame.transform.rotate(second_hand, -second_angle)
    
    return rotated_minute_hand, rotated_second_hand

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    current_time = datetime.datetime.now().time()
    
    rotated_minute_hand, rotated_second_hand = update_hands(current_time)
    
    screen.blit(fon, (0, 0))
    
    screen.blit(rotated_minute_hand, (screen_width/2 - rotated_minute_hand.get_width()/2, screen_height/2 - rotated_minute_hand.get_height()/2))
    
    screen.blit(rotated_second_hand, (screen_width/2 - rotated_second_hand.get_width()/2, screen_height/2 - rotated_second_hand.get_height()/2))
    
    pygame.display.update()
    
    clock.tick(60)