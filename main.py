import pygame
import time

pygame.init()

CANVA_WIDTH = 400
CANVA_HEIGHT = 400
CELL_SIDE = 40
ERASER_SIZE = 20

BLUE = (0,0,225)
WHITE = (255,255,255)
PINK = (225,182,193)

screen = pygame.display.set_mode((CANVA_WIDTH,CANVA_HEIGHT))
pygame.display.set_caption("Enter effect in pygame")

grid = []
for row in range(0,CANVA_HEIGHT,CELL_SIDE):
    for col in range(0,CANVA_WIDTH,CELL_SIDE):
        rect = pygame.Rect(col,row,CELL_SIDE,CELL_SIDE)
        grid.append(rect)

eraser =  pygame.Rect(200,200,ERASER_SIZE,ERASER_SIZE)

running = True
while running:
    screen.fill(WHITE)
    
    for  rect in grid:
        pygame.draw.rect(screen, BLUE, rect)

        mouse_x , mouse_y = pygame.mouse.get_pos()
        eraser.topleft = (mouse_x, mouse_y)

        new_grid = []
        for rect in grid:
            if not eraser.colliderect(rect):
                new_grid.append(rect)
        grid = new_grid 

        pygame.draw.rect(screen, PINK, eraser)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        time.sleep(0.05)

pygame.quit()        

