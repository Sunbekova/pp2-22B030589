import pygame

pygame.init()

clock = pygame.time.Clock()
fps = 60

WIDTH = 800
HEIGHT = 600

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PAINT V3")

#TEXTS:
menu_font = pygame.font.SysFont("Arial.ttx", 25)

clear_text = menu_font.render("CLEAR", True, (0, 0, 0))
clear_rect = pygame.Rect(WIDTH-90, 50, 60, 20)

save_text = menu_font.render("SAVE", True, 'black')
save_rect = pygame.Rect(WIDTH-150, 50, 46, 20)

rect_text = menu_font.render("RECT", True, 'black')
rect_rect = pygame.Rect(250, 10, 50, 50)

triangle_text = menu_font.render("3AN", True, 'black')
triangle_rect = pygame.Rect(310, 10, 50, 50)


eraser = pygame.image.load('eraser.png')
resized_eraser = pygame.transform.scale(eraser, (25, 25))
eraser_rect = pygame.Rect(WIDTH-175, 10, 25, 25)

active_color = 'white'
active_size = 0
painting = [] #PAINTINGS GET HERE



def draw_menu(size, color):
    #MY MENU SURFACE:
    pygame.draw.rect(SCREEN, 'gray', (0, 0, WIDTH, 80))
    pygame.draw.line(SCREEN, 'black', (0, 80), (WIDTH, 80), 3)

    #BRASH SIZES AND PUT IT TO MENU
    xl_brush = pygame.draw.rect(SCREEN, 'black', (10, 10, 50, 50))
    pygame.draw.circle(SCREEN, 'white', (35, 35), 20)

    l_brush = pygame.draw.rect(SCREEN, 'black', (70, 10, 50, 50))
    pygame.draw.circle(SCREEN, 'white', (95, 35), 15)

    m_brush = pygame.draw.rect(SCREEN, 'black', (130, 10, 50, 50))
    pygame.draw.circle(SCREEN, 'white', (155, 35), 10)

    s_brush = pygame.draw.rect(SCREEN, 'black', (190, 10, 50, 50))
    pygame.draw.circle(SCREEN, 'white', (215, 35), 5)

    #FOR TAKE BRASHES IN DRAW FUNC
    brush_list = [xl_brush, l_brush, m_brush, s_brush]

    #FOR SELECTING SIZE
    if size == 20:
        pygame.draw.rect(SCREEN, (0, 255, 255), (10, 10, 50, 50), 3)
    if size == 15:
        pygame.draw.rect(SCREEN, (0, 255, 255), (70, 10, 50, 50), 3)
    if size == 10:
        pygame.draw.rect(SCREEN, (0, 255, 255), (130, 10, 50, 50), 3)
    if size == 5:
        pygame.draw.rect(SCREEN, (0, 255, 255), (190, 10, 50, 50), 3)




    #COLORS IN MENU:
    blue = pygame.draw.rect(SCREEN, 'blue', (WIDTH-35, 10, 25, 25))
    red = pygame.draw.rect(SCREEN, 'red', (WIDTH-63, 10, 25, 25))
    green = pygame.draw.rect(SCREEN, 'green', (WIDTH-91, 10, 25, 25))
    yellow = pygame.draw.rect(SCREEN, (255, 255, 0), (WIDTH-119, 10, 25, 25))
    black = pygame.draw.rect(SCREEN, 'black', (WIDTH-147, 10, 25, 25))
    white = pygame.draw.rect(SCREEN, 'white', (WIDTH-175, 10, 25, 25))
    
    #for clear
    gray = pygame.draw.rect(SCREEN, 'gray', clear_rect)
    #for save
    gray_2 = pygame.draw.rect(SCREEN, (127, 127, 127), save_rect)
    #for rect
    gray_3 = pygame.draw.rect(SCREEN, (128, 128, 128), rect_rect)
    #fortriangle rect
    gray_4 = pygame.draw.rect(SCREEN, (128.1, 128.1, 128.1), triangle_rect)

    #TO INIT COLORS IN MENU
    color_rect = [blue, red, green, yellow, black, white, gray, gray_2, gray_3]
    
    #FOR TAKING COLOR IN DRAW DEF
    rgb_list = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), (0, 0, 0), (255, 255, 255), (255/2, 255/2, 255/2), (127, 127, 127), (128, 128, 128), (128.1, 128.1, 128.1)]


    #FOR SELECTING COLOR
    if color == (0, 0, 255):
        pygame.draw.rect(SCREEN, (0, 255, 255), (WIDTH-35, 10, 25, 25), 3)
    if color == (255, 0, 0):
        pygame.draw.rect(SCREEN, (0, 255, 255), (WIDTH-63, 10, 25, 25), 3)
    if color == (0, 255, 0):
        pygame.draw.rect(SCREEN, (0, 255, 255), (WIDTH-91, 10, 25, 25), 3)
    if color == (255, 255, 0):
        pygame.draw.rect(SCREEN, (0, 255, 255), (WIDTH-119, 10, 25, 25), 3)
    if color == (0, 0, 0):
        pygame.draw.rect(SCREEN, (0, 255, 255), (WIDTH-147, 10, 25, 25), 3)
    if color == (255, 255, 255):
        pygame.draw.rect(SCREEN, (0, 255, 255), (WIDTH-178, 8, 30, 30), 3)
    
    #TO REPRESENT BUTTON'S FUNCTIONALITY
    if color == (255/2, 255/2, 255/2):
        #pygame.draw.rect(SCREEN, 'white', (0, 80, WIDTH, HEIGHT))
        global painting
        painting = []
    if color == (127, 127, 127):
        pygame.image.save(SCREEN, "drawing.png")
    if color == (128, 128, 128):
        pygame.draw.rect(SCREEN, (0, 255, 255), rect_rect, 3)
    if color == (128.1, 128.1, 128.1):
        pygame.draw.rect(SCREEN, (0, 255, 255), triangle_rect, 3)



    
    #FOR ERASER
    SCREEN.blit(resized_eraser, eraser_rect)

    #FOR CLEAR BUTTON
    SCREEN.blit(clear_text, clear_rect)

    #FOR SAVE BUTTON
    SCREEN.blit(save_text, save_rect)

    #FOR RRECT BUTTON
    SCREEN.blit(rect_text, rect_rect)

    #FOR TRIANGLE BUTTON
    SCREEN.blit(triangle_text, triangle_rect)


    return brush_list, color_rect, rgb_list



def draw_painting(paints):
    for i in range(len(paints)):
        pygame.draw.circle(SCREEN, paints[i][0], paints[i][1], paints[i][2])





runing = True
while runing:
    SCREEN.fill('white')

    mouse = pygame.mouse.get_pos() #POSITION OF MOUSE
    left_click = pygame.mouse.get_pressed()[0] #PRESSING LEFT CLICK

   

    if left_click and mouse[1]>80:
        painting.append((active_color, mouse, active_size))

    
    draw_painting(painting)


    if mouse[1] > 80:
        if active_color == (128, 128, 128):
            rect_draw = pygame.draw.rect(SCREEN, active_color, (mouse, mouse), active_size)
        
        elif active_color == (128.1, 128.1, 128.1):
            triangle_draw = pygame.draw.polygon(SCREEN, active_color, ((mouse), (mouse), (mouse)), active_size)

        else:
            pygame.draw.circle(SCREEN, active_color, mouse, active_size)


    brushes, colors, rgbs = draw_menu(active_size, active_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(brushes)):
                if brushes[i].collidepoint(event.pos):
                    active_size = 20 - (i*5)

            
            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    active_color = rgbs[i]



    pygame.display.flip()
    clock.tick(fps)

pygame.quit()