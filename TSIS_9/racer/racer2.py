import random
import pygame
import time

pygame.init()

WIDTH, HEIGHT = 400, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("RACER V2")


#IMAGES

backgr = pygame.image.load("backgrn.png")
resized_bg = pygame.transform.scale(backgr, (WIDTH, HEIGHT))

road = pygame.image.load("road.png")
resized_road = pygame.transform.scale(road, (WIDTH-120, HEIGHT))

coin_1 = pygame.image.load("coin.png")
coin_2 = pygame.image.load("coin2.png")
coin_im3 = pygame.image.load("coin3.png")
coin_3 = pygame.transform.scale(coin_im3, (45, 45))


#COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#SOUNDS:
pygame.mixer.music.load('racer_fon.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)

#VARIABLES:
score = 0
speed = 1
move_left = False
move_right = False
num = random.randint(1, 3)

#TEXTS:
score_font = pygame.font.SysFont("Arial", 30)
game_over = pygame.font.SysFont("bold", 80)
game_over_text = game_over.render('Game Over', True, 'black')



class Road():
    def __init__(self):
        self.image = pygame.image.load("road.png")
        self.image = pygame.transform.scale(self.image, (WIDTH-120, HEIGHT))
        self.x = 64
        self.y1 = 0
        self.y2 = 600
        self.move = True


    def update(self, speed):
        if self.move:
            self.y1 += speed
            self.y2 += speed

            if self.y1>=HEIGHT:
                self.y1 = -HEIGHT
            if self.y2>=HEIGHT:
                self.y2 = -HEIGHT


    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y1))
        SCREEN.blit(self.image, (self.x, self.y2))


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, type):
        super().__init__()
        self.image = pygame.image.load("player.png")
        self.image = pygame.transform.scale(self.image, (48, 86))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



    def update(self, left, right):
        left = pygame.key.get_pressed()
        if left[pygame.K_LEFT]:
            self.rect.x -=3
            if self.rect.x <= 75:
                self.rect.x = 75
        
        right = pygame.key.get_pressed()
        if right[pygame.K_RIGHT]:
            self.rect.x +=3
            if self.rect.right >= 320:
                self.rect.right = 320
        


    def draw(self, SCREEN):
        SCREEN.blit(self.image, self.rect)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 1.5
        self.image = pygame.image.load('enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (
            random.randint(65, WIDTH-65), self.rect.height
        )

    def draw(self, SCREEN):
        SCREEN.blit(self.image, self.rect)

    def update(self):
        global score

        self.rect.y += self.speed
        if self.rect.y > HEIGHT:
            self.rect.y = 0
            self.rect.x = random.randint(65, (WIDTH-65)- self.rect.width)
        if score//100 == 1:
            self.speed = 3



class Coin1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        

        self.image = coin_1
        self.rect = self.image.get_rect()
        self.rect.center = (
            random.randint(65, WIDTH-65), self.rect.height//2
        )

    def update(self, speed):

        self.rect.y += speed
        if self.rect.y > HEIGHT:
            self.rect.y = 0
            self.rect.x = random.randint(65, (WIDTH-60) - self.rect.width)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, self.rect)


class Coin2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        

        self.image = coin_2
        self.rect = self.image.get_rect()
        self.rect.center = (
            random.randint(65, WIDTH-65), self.rect.height//2
        )

    def update(self, speed):

        self.rect.y += speed
        if self.rect.y > HEIGHT+800:
            self.rect.y = 0
            self.rect.x = random.randint(65, (WIDTH-60) - self.rect.width)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, self.rect)


class Coin3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        

        self.image = coin_3
        self.rect = self.image.get_rect()
        self.rect.center = (
            random.randint(65, WIDTH-65), self.rect.height//2
        )

    def update(self, speed):

        self.rect.y += speed
        if self.rect.y > HEIGHT+1000:
            self.rect.y = 0
            self.rect.x = random.randint(65, (WIDTH-60) - self.rect.width)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, self.rect)

#OBJECTS:
road = Road()
player = Player(145, HEIGHT-120, 0)
coin_1 = Coin1()
coin_2 = Coin2()
coin_3 = Coin3()
enemy = Enemy()
enemies = pygame.sprite.Group()
enemies.add(enemy)

coins1 = pygame.sprite.Group()
coins1.add(coin_1)
coins2 = pygame.sprite.Group()
coins2.add(coin_2)
coins3 = pygame.sprite.Group()
coins3.add(coin_3)




running = True

while running:

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            

        if event.type == pygame.KEYDOWN:
            x, y = 0, 0
            if x <= WIDTH//2:
                move_left = True
            else:
                move_right = True
       

                

    SCREEN.blit(resized_bg, (0, 0))
    road.update(speed)
    road.draw(SCREEN)

    player.update(move_left, move_right)
    player.draw(SCREEN)

    enemy.update()
    enemy.draw(SCREEN)

    coin_1.update(speed)
    coin_1.draw(SCREEN)

    coin_2.update(speed)
    coin_2.draw(SCREEN)

    coin_3.update(speed)
    coin_3.draw(SCREEN)


    if pygame.sprite.spritecollideany(player, coins1):
        score += 0.08
        pygame.mixer.Sound('coin.wav').play()
        pygame.mixer.music.set_volume(0.6)
    elif pygame.sprite.spritecollideany(player, coins2):
        score += 0.16
        pygame.mixer.Sound('coin.wav').play()
        pygame.mixer.music.set_volume(0.6)
    elif pygame.sprite.spritecollideany(player, coins3):
        score += 0.24
        pygame.mixer.Sound('coin.wav').play()
        pygame.mixer.music.set_volume(0.6)
      
            

    SCORE = score_font.render(f" Your Score: {str(int(score))}", True, (0, 0, 0))
    SCREEN.blit(SCORE, (0, 0))

    if pygame.sprite.spritecollideany(player, enemies):
        pygame.mixer.music.stop()
        pygame.mixer.Sound('crash.wav').play()
        pygame.mixer.music.set_volume(0.6)
        SCREEN.blit(game_over_text, (60, 250))

        pygame.display.flip() #without this display won't update and won't show game_over
        time.sleep(2)
        running = False 


   
    pygame.display.update()
    pygame.display.flip()

pygame.quit()

