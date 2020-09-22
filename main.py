import pygame

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480

GRID_SIZE = 30
GRID_WIDTH = SCREEN_WIDTH / GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT / GRID_SIZE

UP = (0,-1)
DOWN = (0,1)
LEFT = (0,-1)
RIGHT = (0,1)

def main():
    pygame.init()

    logo = pygame.image.load("durp.jpg")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Snake")

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__=="__main__":
    main()