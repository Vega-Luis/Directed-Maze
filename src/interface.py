import sys
from pygame import *
import pygame
from pygame.locals import *

class Player:
    def __init__(self):
        self.name = "nickNmae"
        self.movements = 0
        self.suggestions = 10
        self.type = ""
        self.rect = pygame.Rect(15, 95, 40,40)
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

class Boton:
    def __init__(self,screen):
        self.screen = screen
        self.rect = self.screen.get_rect()
        self.width = self.height = 500, 500
              
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
        self.button_reboot = Rect(520,50,90,30)
        self.button_verify = Rect(520,100,80,30)
        self.button_suggetion = Rect(500,150,120,30)
        self.button_seeSolition = Rect(490,200,140,30)
        self.draw()


    def draw(self):
        x = y = 15
        for row in maze:
            for col in row:
                if col == "x":
                    Wall((x, y))
                if col == "f":
                    self.end_rect = pygame.Rect(x, y, 40, 40)
                
                x += 40
            y += 40
            x = 15

    def run(self):
        myFort = font.SysFont("Calibri",25)
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
                
                elif (event.type == MOUSEBUTTONDOWN and event.button == 1):
                    if (self.button_verify.collidepoint(mouse.get_pos())):
                        print("Uno")
                    elif (self.button_suggetion.collidepoint(mouse.get_pos())):
                        print("Dos")
                    elif (self.button_seeSolition.collidepoint(mouse.get_pos())):
                        print("Tres")
                    elif (self.button_reboot.collidepoint(mouse.get_pos())):
                        print("Tres")

            if self.player.rect.colliderect(self.end_rect):
                    pygame.quit()
                    sys.exit()

            if (self.button_verify.collidepoint(mouse.get_pos())):
                draw.rect(self.screen,(237,128,19),self.button_verify,0)
            else: # if not(self.button_verify.collidepoint(mouse.get_pos())):
                draw.rect(self.screen,(70,184,34),self.button_verify,0)

            if (self.button_suggetion.collidepoint(mouse.get_pos())):
                draw.rect(self.screen,(237,128,19),self.button_suggetion,0)
            else: #if not(self.button_suggetion.collidepoint(mouse.get_pos())):
                draw.rect(self.screen,(70,184,34),self.button_suggetion,0)
            
            if (self.button_seeSolition.collidepoint(mouse.get_pos())):
                draw.rect(self.screen,(237,128,19),self.button_seeSolition,0)
            else: # if not(self.button_seeSolition.collidepoint(mouse.get_pos())):
                draw.rect(self.screen,(70,184,34),self.button_seeSolition,0)

            if (self.button_reboot.collidepoint(mouse.get_pos())):
                draw.rect(self.screen,(237,128,19),self.button_reboot,0)
            else: #if not(self.button_reboot.collidepoint(mouse.get_pos())):
                draw.rect(self.screen,(70,184,34),self.button_reboot,0)

            App.screen.fill((0, 0, 50))
            for wall in walls:
                pygame.draw.rect(App.screen , (255, 255, 255), wall.rect)
            pygame.draw.rect(App.screen , (255, 0, 0), self.end_rect)
            pygame.draw.rect(App.screen , (255, 200, 0),self.player.rect)
            texto1 = myFort.render("Verify",True,(255,255,255))
            texto2 = myFort.render("Suggetion",True,(255,255,255))
            texto3 = myFort.render("See Solition",True,(255,255,255))
            texto4 = myFort.render("Reniciar",True,(255,255,255))

            self.screen.blit(texto1,(self.button_verify.x+(self.button_verify.width-texto1.get_width())/2,
                        self.button_verify.y+(self.button_verify.height-texto1.get_height())/2))

            self.screen.blit(texto2,(self.button_suggetion.x+(self.button_suggetion.width-texto2.get_width())/2,
                        self.button_suggetion.y+(self.button_suggetion.height-texto2.get_height())/2))
            
            self.screen.blit(texto3,(self.button_seeSolition.x+(self.button_seeSolition.width-texto3.get_width())/2,
                        self.button_seeSolition.y+(self.button_seeSolition.height-texto3.get_height())/2))

            self.screen.blit(texto4,(self.button_reboot.x+(self.button_reboot.width-texto4.get_width())/2,
                        self.button_reboot.y+(self.button_reboot.height-texto4.get_height())/2))
            pygame.display.flip()
            
        pygame.quit()


if __name__ == '__main__':
    App().run()
