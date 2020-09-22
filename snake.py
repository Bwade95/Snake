import setters, random, pygame, sys

class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((screen_width / 2), (screen_height / 2))]
        self.direction = random.choice([up,down,left,right])
        self.color = (0,128,128)
    
    # draws snake on scene
    def draw(self,surface):
        for p in self.positions:
            r = pygame.Rect((p[0],p[1]),(grid_size,grid_size))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93,216,228), r, 1)
    
    # gets location of head of snake
    def get_head_position(self):
        return self.positions[0]
    
    # moves snake forward at set speed
    def move(self):
        cur = self.get_head_position()
        x,y = self.direction
        new = (((cur[0]+(x*grid_size))%screen_width), (cur[1]+(y*grid_size))%screen_height)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0,new)
            if len(self.positions) > self.length:
                self.positions.pop()
    
    # turns snake left or right based on facing
    def turn(self,point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point
    
    # called when snake dies
    def reset(self):
        self.length = 1
        self.positions = [((screen_width / 2), (screen_height / 2))]
        self.direction = random.choice([up,down,left,right])

    # keeps track of snake size
    def size(self):
        pass

    # keys player presses to control snake
    def keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(up)
                elif event.key == pygame.K_DOWN:
                    self.turn(down)
                elif event.key == pygame.K_LEFT:
                    self.turn(left)
                elif event.key == pygame.K_RIGHT:
                    self.turn(right)

# initiliasing setters
screen_width = setters.SCREEN_WIDTH
screen_height = setters.SCREEN_HEIGHT

grid_size = setters.GRID_SIZE
  
up = setters.UP
down = setters.DOWN
left = setters.LEFT
right = setters.RIGHT