import pygame, sys, setters
from snake import Snake
from food import Food

screen_width = setters.SCREEN_WIDTH
screen_height = setters.SCREEN_HEIGHT

grid_size = setters.GRID_SIZE
grid_height = setters.GRID_HEIGHT
grid_width = setters.GRID_WIDTH

fps = setters.FPS

def draw_grid(surface):
    for y in range(0,int(grid_height)):
        for x in range(0,int(grid_width)):
            if (x+y) % 2 == 0:
                r = pygame.Rect((x*grid_size,y*grid_size), (grid_size, grid_size))
                pygame.draw.rect(surface, (105,31,105), r)
            else:
                rr = pygame.Rect((x*grid_size,y*grid_size), (grid_size, grid_size))
                pygame.draw.rect(surface, (77,41,77), rr)

def main():
    pygame.init()

    clock = pygame.time.Clock()
    

    logo = pygame.image.load("durp.jpg")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Snake")

    screen = pygame.display.set_mode((screen_width,screen_height), pygame.RESIZABLE)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    draw_grid(surface)

    snake = Snake()
    food = Food()

    myfont = pygame.font.SysFont("monospace", 16)

    running = True

    score = 0

    while running:
        print(snake.positions)
        clock.tick(fps)
        snake.keys()
        draw_grid(surface)
        snake.move()
        if snake.get_head_position() == food.position:
            snake.length += 1
            score += 1
            food.randomize_position()
        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface,(0,0))
        text = myfont.render("Score {0}".format(score), 1, (0,0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__=="__main__":
    main()