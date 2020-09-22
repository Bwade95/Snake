import setters, random, pygame

class Food:
    def __init__(self):
        self.position = (0,0)
        self.color = (255,255,255)

    def draw(self,surface):
        r = pygame.Rect((self.position[0], self.position[1]), (grid_size,grid_size))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93,216,228), r, 1)

    def randomise_position(self):
        self.position = (random.randint(0, grid_width-1) * grid_size, random.randint(0,grid_height-1) * grid_size)

    def energy(self):
        pass        

# initiliasing setters
screen_width = setters.SCREEN_WIDTH
screen_height = setters.SCREEN_HEIGHT

grid_size = setters.GRID_SIZE
grid_width = setters.GRID_WIDTH
grid_height = setters.GRID_HEIGHT
  
up = setters.UP
down = setters.DOWN
left = setters.LEFT
right = setters.RIGHT