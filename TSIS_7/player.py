import pygame
pygame.init()


screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Music Player")

image = pygame.image.load("img1.png")

resized_image = pygame.transform.scale(image, (500, 300))

songs = ["Rick Astley - Never Gonna Give You Up.mp3", "Michael Jackson - Billie Jean.mp3", "Britney Spears - Criminal.mp3"]

pygame.mixer.init()
pygame.mixer.music.load(songs[0])

#keyboard
play_press = pygame.K_RETURN
next_press = pygame.K_RIGHT
prev_press = pygame.K_LEFT
stop_press = pygame.K_SPACE

curr_song = 0


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pressed = pygame.key.get_pressed()
    if pressed[play_press]:
        pygame.mixer.music.play()
    
    elif pressed[stop_press]:
        pygame.mixer.music.pause()

    elif pressed[next_press]:
        if curr_song < len(songs) - 1:
            curr_song +=1
            pygame.mixer.music.load(songs[curr_song])
            pygame.mixer.music.play()
        
        curr_song +=1

    elif pressed[prev_press]:
        if curr_song >=0 or curr_song>=1:
            curr_song -= 1
            pygame.mixer.music.load(songs[curr_song])
            pygame.mixer.music.play()

        curr_song = 0


    screen.blit(resized_image, (0, 0))

    pygame.display.flip()

    
