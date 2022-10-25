import sys
import pygame
from pygame.locals import *

class Player:
    def __init__(self):
        self.name = "nickNmae"
        self.movements = 0
        self.suggestions = 10
        self.type = ""
        self.rect = pygame.Rect(0, 80, 40,40)
        self.row = 0
        self.column = 0 
        self.previous=""
        self.getPosition()

    def getPosition(self):
        x = y = 0
        for row in maze:
            y = 0
            for col in row:
                if (col == 'i'):
                    self.row = x
                    self.column = y
                y+=1
            x+=1
            
    def move(self, dx, dy):
        if (self.validarMovimiento(dx, dy)):
            if (dx > 0): 
                self.previous="RIGHT"
                self.column+=1
            if (dx < 0): 
                self.previous="LEFT"
                self.column-=1
            if (dy > 0): 
                self.previous="DOWN"
                self.row+=1
            if (dy < 0):
                self.previous="UP"
                self.row-=1
            self.rect = pygame.Rect(self.rect.x+dx,self.rect.y+dy, 40,40)
        else:
            print("Cannot move")
                
    def validarMovimiento(self, dx, dy):
        posActual = maze[self.row][self.column] 
        if(posActual!='i'):
            if (posActual == 'at'):
                print(self.previous)
                if (dx > 0 and self.previous=="LEFT"): 
                    return True
                if (dx < 0 and self.previous=="RIGHT"): 
                    return True
                if (dy > 0 and self.previous=="UP"): 
                    return True
                if (dy < 0 and self.previous=="DOWN"):
                    return True
                return False
            else:
                posActual = maze[self.row][self.column] 
                if (dx > 0): 
                    posNext = maze[self.row][self.column+1] 
                    return ((posActual == 'ad' or posActual == 'inter') and posNext !='x')
                if (dx < 0): 
                    posNext = maze[self.row][self.column-1]
                    return (posActual == 'inter' and posNext !='x')
                if (dy > 0): 
                    posNext = maze[self.row+1][self.column]
                    return ((posActual == 'ab' or posActual == 'inter') and posNext !='x')
                if (dy < 0):
                    posNext = maze[self.row-1][self.column]
                    return ((posActual == 'ar' or posActual == 'inter') and posNext!='x')
        else:
            if (dx>0):
                return True
            return False
            
class Wall(object):
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 40, 40)
        
walls = []
maze = [['x','x','x','x','x','x','x','x','x','x','x'],
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
        ['x','x','x','x','x','x','x','x','x','x','x']]

class App:

    def __init__(self):
        pygame.init()
        flags = RESIZABLE
        App.screen = pygame.display.set_mode((650, 500), flags)
        App.running = True
        
        self.player = Player()
        self.end_rect=""
        self.draw()

    def draw(self):
        x = y = 0
        for row in maze:
            for col in row:
                if col == "x":
                    Wall((x, y))
                if col == "f":
                    self.end_rect = pygame.Rect(x, y, 40, 40)
                
                x += 40
            y += 40
            x = 0

    def run(self):
        while App.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    App.running = False
                elif event.type == pygame.KEYDOWN:
                    if (event.key == K_RIGHT):
                        self.player.move(40, 0)
                    elif (event.key == K_LEFT):
                        self.player.move(-40, 0)
                    elif (event.key == K_UP):
                        self.player.move(0, -40)
                    elif (event.key == K_DOWN):
                        self.player.move(0, 40)
            if self.player.rect.colliderect(self.end_rect):
                pygame.quit()
                sys.exit()

            App.screen.fill((0, 0, 50))
            for wall in walls:
                pygame.draw.rect(App.screen , (255, 255, 255), wall.rect)
            pygame.draw.rect(App.screen , (255, 0, 0), self.end_rect)
            pygame.draw.rect(App.screen , (255, 200, 0),self.player.rect)
            pygame.display.flip()

        pygame.quit()


if __name__ == '__main__':
    App().run()
