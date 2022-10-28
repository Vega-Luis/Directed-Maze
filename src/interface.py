import sys
from pygame import *
import pygame
from pygame.locals import *
from inputText import InputText 
import time
import constants as consts
import controllerProlog

"""
* Class constructor
* Set up a maze game by requesting the path of the maze file
* @param {String} Path: The path of the maze file
"""
class Player:
    """
    * 
    *
    * @param {String} 
    """

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

    """
    * 
    *
    * @param {String} 
    """
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

    """
    * 
    *
    * @param {String} 
    """  
    def move(self, dx, dy, xDisplacement, yDisplacement, controller):
        if (self.validarMovimiento(dx, dy, xDisplacement, yDisplacement, controller)):
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
            self.movements+=1
            self.rect = pygame.Rect(self.rect.x+dx,self.rect.y+dy, 40,40)
        else:
            print("Cannot move")

    """
    * 
    *
    * @param {String} 
    """            
    def validarMovimiento(self, dx, dy, xDisplacement, yDisplacement, controller):
        posActual = maze[self.row][self.column]
        valid = controller.checkMove(self.row, self.column, self.row + xDisplacement,
                        self.column + yDisplacement, posActual)
        return valid
 
    """
    * 
    *
    * @param {String} 
    """
    def getValue(self,list):
        array = []
        for element in list:
            row = element[0]*40+15
            column = element[1]*40+15
            array+= [[column,row]]
        return array

    """
    * 
    *
    * @param {String} 
    """
"""
    * 
    *
    * @param {String} 
    """
class Wall(object):
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 40, 40)
"""
    * 
    *
    * @param {String} 
    """
class Way(object):
    def __init__(self, pos,wayType):
        self.img = pygame.image.load('resource/vacio.png')
        self.rect = self.img.get_rect()
        ways.append(self)
        self.draw(pos,wayType)
    
    def draw(self,pos,wayType):
        if (wayType == 'ad'):
            self.img = pygame.image.load('resource/flecha-derecha.png')
            self.img.convert()
            self.rect = self.img.get_rect()
            self.rect.center = pos[0]+20,pos[1]+20
            self.rect.width = 40
            self.rect.height = 40

        elif (wayType == 'ar'):

            self.img = pygame.image.load('resource/flecha-arriba.png')
            self.img.convert()
            self.rect = self.img.get_rect()
            self.rect.center = pos[0]+20,pos[1]+20
            self.rect.width = 40
            self.rect.height = 40

        elif (wayType == 'ab'):
            self.img = pygame.image.load('resource/flecha-abajo.png')
            self.img.convert()
            self.rect = self.img.get_rect()
            self.rect.center = pos[0]+20,pos[1]+20
            self.rect.width = 40
            self.rect.height = 40

        elif (wayType == 'inter'):
            self.img = pygame.image.load('resource/cuatro-flechas.png')
            self.img.convert()
            self.rect = self.img.get_rect()
            self.rect.center = pos[0]+20,pos[1]+20
            self.rect.width = 40
            self.rect.height = 40
        
        elif (wayType == 'at'):
            self.img = pygame.image.load('resource/flechas-circulares.png')
            self.img.convert()
            self.rect = self.img.get_rect()
            self.rect.center = pos[0]+20,pos[1]+20
            self.rect.width = 40
            self.rect.height = 40

        else:
            self.img = pygame.image.load('resource/flecha-de-juego.png')
            self.img.convert()
            self.rect = self.img.get_rect()
            self.rect.center = pos[0]+20,pos[1]+20
            self.rect.width = 40
            self.rect.height = 40

"""
    * 
    *
    * @param {String} 
    """
class Boton:
    def __init__(self,screen):
        self.screen = screen
        self.rect = self.screen.get_rect()
        self.width = self.height = 500, 500

path = ""              
walls = []
ways = []
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


"""
    * 
    *
    * @param {String} 
    """
class App:
    """
    * 
    *
    * @param {String} 
    """
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
        self.suggetion_list= []
        self.seeSolition_list= []
        self.draw()
        self.plController = ''
        #maze = self.controllerProlog.getMaze()
        
    def mainMenu(self):
        while True:
            screenWidth, screenHeight = pygame.display.get_surface().get_size()
            App.screen.fill((174, 219, 52))

            font = pygame.font.SysFont(None, 40)
            textobj = font.render("Directed Maze", 1, (0,0,0))
            textrect = textobj.get_rect()
            textrect.center = (screenWidth // 2, screenHeight // 2 - 150)
            self.screen.blit(textobj, textrect)
            #Buttons
            buttonPlay = pygame.Rect(screenWidth // 2 - 100, screenHeight // 2 - 50 , 200, 50)
            buttonExit = pygame.Rect(screenWidth // 2 - 100, screenHeight // 2 + 25, 200, 50)
            # Draw buttons
            pygame.draw.rect(App.screen, (252, 118, 52), buttonPlay)
            pygame.draw.rect(App.screen, (252, 118, 52), buttonExit)


            # Texts
            textPlay = font.render("New Game", 0, (27, 72, 107))
            textPlayCenter = textPlay.get_rect()
            textPlayCenter.center = (buttonPlay.centerx, buttonPlay.centery)

            textExit = font.render("Exit", 1, (27, 72, 107))
            textExitCenter = textExit.get_rect()
            textExitCenter.center = (buttonExit.centerx, buttonExit.centery)

            self.screen.blit(textPlay, textPlayCenter)
            self.screen.blit(textExit, textExitCenter)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if buttonExit.collidepoint(mouse.get_pos()):
                            pygame.quit()
                            sys.exit()
                        if buttonPlay.collidepoint(mouse.get_pos()):
                            inputText = InputText()
                            inputText.run()
                            self.plController = controllerProlog.PrologController(inputText.text)
                            self.run()
            pygame.display.flip()

    """
    * 
    *
    * @param {String} 
    """
    def draw(self):
        x = y = 15
        for row in maze:
            for col in row:
                if col == "x":
                    Wall((y,x))
                elif col == "f":
                    self.end_rect = pygame.Rect(y,x, 40, 40)
                else:
                    Way((y,x),col)
                y += 40
            x += 40
            y = 15

    """
    * 
    *
    * @param {String} 
    """
    def reboot(self):
        self.player.rect = pygame.Rect(15, 95, 40,40)
        self.player.type = "Abandono"
        self.player.row = 2
        self.player.column = 0

    """
    * 
    *
    * @param {String} 
    """
    def verify(self):
        flag = self.plController.check(self.player.row,self.player.column)
        if (flag):
            print("Yes") 
        else:
            print("No")

    """
    * 
    *
    * @param {String} 
    """
    def suggetion(self):
        self.suggetion_list = []
        suggetions_list = self.plController.suggestion(self.player.row,self.player.column)
        if (self.player.suggestions > 0):
            array = self.player.getValue(suggetions_list)
            for element in array:
                rect = pygame.Rect(element[0],element[1],40,40)
                self.suggetion_list.append(rect)
            self.player.suggestions -= 1
        else:
            pass
            #sonido o ventana
        
    """
    * 
    *
    * @param {String} 
    """
    def seeSolution(self):
        seeSolutions_list = self.plController.seeSolution()
        array = self.player.getValue(seeSolutions_list)
        for element in array:
            rect = pygame.Rect(element[0],element[1],40,40)
            self.seeSolition_list.append(rect)
        self.player.type="Autosolución" 

    """
    * 
    *
    * @param {String} 
    """
    def statistics(self):
        print("Nickname: ",self.player.name)
        print("Movements: ",self.player.movements)
        print("Suggestions: ",self.player.suggestions)
        print("Solution type: ",self.player.type)
    

    """
    * 
    *
    * @param {String} 
    """
    def run(self):
        flag_Suggetion = False
        flag_seeSolition = False
        running = True

        myFort = font.SysFont("Calibri",25)
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                
                elif event.type == pygame.KEYDOWN:
                    if (event.key == K_RIGHT):
                        self.player.move(40, 0, 0, 1, self.plController)
                    elif (event.key == K_LEFT):
                        self.player.move(-40, 0, 0, -1, self.plController)
                    elif (event.key == K_UP):
                        self.player.move(0, -40, -1, 0, self.plController)
                    elif (event.key == K_DOWN):
                        self.player.move(0, 40, 1, 0, self.plController)
                    if event.key == K_ESCAPE:
                        running = False
                                    
                elif (event.type == MOUSEBUTTONDOWN and event.button == 1):
                    if (self.button_reboot.collidepoint(mouse.get_pos())):
                        self.reboot()
                        flag_seeSolition = False
                    elif (self.button_suggetion.collidepoint(mouse.get_pos())):
                        self.suggetion()
                        flag_Suggetion = True
                        
                    elif (self.button_seeSolition.collidepoint(mouse.get_pos())):
                        self.seeSolution()
                        flag_seeSolition = True

                    elif (self.button_verify.collidepoint(mouse.get_pos())):
                        self.verify()
            if self.player.rect.colliderect(self.end_rect):
                    self.player.type = "Exitosa" 
                    self.statistics()

            App.screen.fill((0, 0, 50))
            
            
            for wall in walls:
                pygame.draw.rect(App.screen , (255, 255, 255), wall.rect)
            
            if (flag_seeSolition):
                for way in ways:
                    App.screen.blit(way.img, way.rect)
                for element in self.seeSolition_list:
                    pygame.draw.rect(App.screen , (0, 128, 0), element)
            else:
                for way in ways:
                    App.screen.blit(way.img, way.rect)
                    
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

            if (flag_Suggetion):
                for element in self.suggetion_list:
                    pygame.draw.rect(App.screen , (0, 128, 0), element,4)
                pygame.display.update()
                time.sleep(1)
                flag_Suggetion = False
        pygame.display.update()

"""
    * 
    *
    * @param {String} 
    """
if __name__ == '__main__':
    App().mainMenu()

