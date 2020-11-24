import pygame,sys


screen = pygame.display.set_mode((800,500),pygame.DOUBLEBUF,32)
image = pygame.image.load("assets/background/double_spring.png").convert()
image = pygame.transform.scale(image,(1600,500))
image2 = image.copy()
rect = image.get_rect()
bx1 = 0
    

print(rect)
while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((222,222,0))

    
    screen.blit(image,(bx1,0))
    if(bx1 <= -800):
        bx1 = 0
    bx1 -= 1

    pygame.display.update()

