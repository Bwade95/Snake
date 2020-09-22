import pygame

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480

GRID_SIZE = 30
GRID_WIDTH = int(SCREEN_WIDTH / GRID_SIZE)
GRID_HEIGHT = int(SCREEN_HEIGHT / GRID_SIZE)

UP = (0,-1)
DOWN = (0,1)
LEFT = (0,-1)
RIGHT = (0,1)

FPS = 24

def draw_grid(surface):
    for y in range(0,int(GRID_HEIGHT)):
        for x in range(0,int(GRID_WIDTH)):
            if (x+y) % 2 == 0:
                r = pygame.Rect((x*GRID_SIZE,y*GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(surface, (105,31,105), r)
            else:
                rr = pygame.Rect((x*GRID_SIZE,y*GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(surface, (77,41,77), rr)

def main():
    pygame.init()

    clock = pygame.time.Clock()
    

    logo = pygame.image.load("durp.jpg")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Snake")

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), pygame.RESIZABLE)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    draw_grid(surface)

    running = True

    while running:
        clock.tick(FPS)
        screen.blit(surface,(0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__=="__main__":
    main()