import controllerProlog
import pygame

class Player:
    def __init__(self):
        self.name = "nickNmae"
        self.movements = 0
        self.suggestions = 10
        self.type = ""
        self.rect = pygame.Rect(0, 80, 40,40)

    def move():
        pass

class Wall(object):
    
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 40, 40)
 
pygame.init()
pygame.display.set_caption("Maze")
screen = pygame.display.set_mode((650, 500))
walls = []
player = Player()
maze = [
            ['x','x','x','x','x','x','x','x','x','x','x'],
            ['x','ar','x','x','ad','ad','ad','inter','ad','inter','x'],
            ['i','inter','ad','ad','inter','x','x','ab','x','ab','x'],
            ['x','ab','x','x','x','inter','at','inter','x','ab','x'],
            ['x','ab','x','x','x','ab','x','ab','x','x','x'],
            ['x','ab','x','x','inter','inter','x','ab','x','inter','f'],
            ['x','ab','x','x','ab','x','x','inter','inter','inter','x'],
            ['x','ab','x','x','ab','x','x','x','ar','x','x'],
            ['x','ab','x','at','inter','inter','ad','ad','inter','at','x'],
            ['x','ab','x','ar','x','ab','x','x','ab','ar','x'],
            ['x','inter','ad','inter','x','inter','ad','x','ab','inter','x'],
            ['x','x','x','x','x','x','x','x','x','x','x'],
        ]
 
x = y = 0
for row in maze:
    for col in row:
        if col == "x":
            Wall((x, y))
        if col == "f":
            end_rect = pygame.Rect(x, y, 40, 40)
        
        x += 40
    y += 40
    x = 0
 
running = True
while running:
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False
    key = pygame.key.get_pressed()
    screen.fill((0, 0, 50))
    for wall in walls:
        pygame.draw.rect(screen, (255, 255, 255), wall.rect)
    pygame.draw.rect(screen, (255, 0, 0), end_rect)
    pygame.draw.rect(screen, (255, 200, 0),player.rect)
    pygame.display.flip()
pygame.quit()
