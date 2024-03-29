import sys
from pygame import *
import pygame
from pygame.locals import *
from inputText import InputText 
from pyswip import *
from constants import *
import time
import controllerProlog
from stat_record import Stat
from stats_window import StatsWindow

"""
* Class Player
* This class is used to simulate the maze player
"""
class Player:
    def __init__(self):
        self.name = "nickNmae"
        self.movements = 0
        self.suggestions = 10
        self.type = ""
        self.rect = ""
        self.row = 0
        self.column = 0 
        self.previous=""

    """
     * This function sets the player icon in the begining of the maze
     * @param {Integer} Row: current position row 
    """  
    def setPlayerOriginPoint(self, row):
        yDisplacement = row * 40 + 15
        self.rect = pygame.Rect(15, yDisplacement, 40, 40)

    """
     * This function the player logic position to the begining of the maze
     * @param {Integer} Row: current position row 
    """
    def setOriginPoint(self, originPoint):
        self.row = originPoint[0] 
        self.column = originPoint[1] 

    """
    * This function moves the position of the player
    * @param {Integer} dx: current position row 
    * @param {Integer} dy: current position column
    """  
    def move(self, dx, dy):
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

 
    """
    * This function gets the position of the player in the maze and returns an array with the value of the straight position
    * @param {Array} list: current position of the player
    * @return {Array}: returns an array with the value of the straight position
    """  
    def getValue(self,list):
        array = []
        for element in list:
            row = element[0]*40+15
            column = element[1]*40+15
            array+= [[column,row]]
        return array

        
"""
* This class simulates a maze wall.
"""
class Wall(object):
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 40, 40)

"""
* This class simulates the path of the maze.
"""
class Way(object):
    def __init__(self, pos,wayType):
        self.img = pygame.image.load('resource/vacio.png')
        self.rect = self.img.get_rect()
        ways.append(self)
        self.draw(pos,wayType)
    
    """
    * This function gets the position of the player in the maze and returns an array with the value of the straight position
    * @param {Array} pos: current position of the way
    * @param {String} wayType: the type of way to draw
    """ 
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
            self.img = pygame.image.load('resource/flecha-izquierda.png')
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
*This class simulates a button
"""
class Boton:
    def __init__(self,screen):
        self.screen = screen
        self.rect = self.screen.get_rect()
        self.width = self.height = 500, 500

path = ""   # the path of the maze           
walls = [] # maze wall list
ways = []  # maze way list


"""
* This class simulates a maze with condition to moves
"""
class App:
    def __init__(self):
        pygame.init()
        flags = RESIZABLE
        App.screen = pygame.display.set_mode((650, 500))
        self.player = Player()
        self.end_rect=""
        self.button_reboot = Rect(520,50,90,30)
        self.button_verify = Rect(520,100,80,30)
        self.button_suggetion = Rect(500,150,120,30)
        self.button_seeSolition = Rect(490,200,140,30)
        self.suggetion_list= []
        self.seeSolition_list= []
        self.plController = ''
        self.statistics = []
        self.clock = pygame.time.Clock()
        self.time = ""
        self.startTime = 0
       
    """
    * Menu of the maze game
    """
    def mainMenu(self):
        App.screen = pygame.display.set_mode((650, 500))
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
            buttonStats = pygame.Rect(screenWidth // 2 - 100, screenHeight // 2 + 25, 200, 50)
            buttonExit = pygame.Rect(screenWidth // 2 - 100, screenHeight // 2 + 100, 200, 50)
            # Draw buttons
            pygame.draw.rect(App.screen, (252, 118, 52), buttonPlay)
            pygame.draw.rect(App.screen, (252, 118, 52), buttonStats)
            pygame.draw.rect(App.screen, (252, 118, 52), buttonExit)


            # Texts
            textPlay = font.render("New Game", 0, (27, 72, 107))
            textPlayCenter = textPlay.get_rect()
            textPlayCenter.center = (buttonPlay.centerx, buttonPlay.centery)

            textStats = font.render("Stats", 1, (27, 72, 107))
            textStatsCenter = textStats.get_rect()
            textStatsCenter.center = (buttonStats.centerx, buttonStats.centery)

            textExit = font.render("Exit", 1, (27, 72, 107))
            textExitCenter = textExit.get_rect()
            textExitCenter.center = (buttonExit.centerx, buttonExit.centery)

            self.screen.blit(textPlay, textPlayCenter)
            self.screen.blit(textStats, textStatsCenter)
            self.screen.blit(textExit, textExitCenter)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if buttonStats.collidepoint(mouse.get_pos()):
                            self.printStatistics()
                        if buttonExit.collidepoint(mouse.get_pos()):
                            pygame.quit()
                            sys.exit()
                        if buttonPlay.collidepoint(mouse.get_pos()):
                            inputText = InputText()
                            inputText.run()
                            self.plController = controllerProlog.PrologController(inputText.text)
                            originPoint = self.plController.getOriginPoint()
                            self.player.setOriginPoint(originPoint)
                            self.player.setPlayerOriginPoint(originPoint[0])
                            self.player.movements = 0
                            self.draw(self.plController.maze)
                            self.run()

            pygame.display.flip()

    """
    * This function check the moze for the palyer 
    * @param {Array} rowDisplacement: current row position of the player
    * @param {Array} columnDisplacement: current column position of the player
    * @return True si es un movimento valido de lo contraio
    """  
    def checkMove(self, rowDisplacement, columnDisplacement):
        actualRow = self.player.row
        actualColumn = self.player.column
        actualPos = self.plController.maze[actualRow][actualColumn]
        isValid = self.plController.checkMove(actualRow, actualColumn,
                        actualRow + rowDisplacement, actualColumn + columnDisplacement, actualPos)
        return isValid
  
    """
    * This function draw the maze
    * @param {Array} maze: maze game
    """  
    def draw(self, maze):
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
    * This function puts de current position of the playe in a original row and
    """
    def reboot(self):
        self.player.type = "Quit"
        self.addStat()
        self.player.type = ""
        originPoint = self.plController.getOriginPoint()
        self.player.setOriginPoint(originPoint)
        self.player.setPlayerOriginPoint(originPoint[0])
        self.player.suggestions = 10
        self.player.movements = 0
        self.startTime = pygame.time.get_ticks()
    
    """
    * This verify a the position of de player
    """
    def verify(self):
        flag = self.plController.check(self.player.row,self.player.column)
        if (flag):
            self.goodFeedback() 
        else:
            self.badFeedback()
    
    """
    *This function gives clues to the player in the maze
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
            
    """
    * This function give the solution of the maze
    """
    def seeSolution(self):
        seeSolutions_list = self.plController.seeSolution()
        array = self.player.getValue(seeSolutions_list)
        for element in array:
            rect = pygame.Rect(element[0],element[1],40,40)
            self.seeSolition_list.append(rect)
        self.player.type="Auto solution"


    def addStat(self):
        newStat = Stat(self.player.name, self.player.movements,
                        10 - self.player.suggestions, self.player.type, self.time)
        self.statistics += [newStat]

    """
    *This function shows the statistics of the players
    """
    def printStatistics(self):
        str = ""
        for record in self.statistics:
           str += record.toString()
        StatsWindow(str).run()

    """
    *This function create the clock of the maze
    """
    def chronometer(self):
        finishTime = pygame.time.get_ticks()
        elapsed = finishTime - self.startTime
        ms = elapsed % 1000
        s = int(elapsed/1000 % 60)
        m = int(elapsed/60000 % 24)
        self.time = str(m) + ":" + str(s) + ":" + str(ms)
    
    """
    * This function draw the clock of the maze
    """
    def drawChronometer(self):
        font = pygame.font.SysFont(None, 30)
        textobj = font.render(self.time, 1, (255, 255, 255))
        textrect = textobj.get_rect()
        textrect.center = (550, 300)
        self.screen.blit(textobj, textrect)

    """
    * This function runs the program
    """
    def run(self):
        screen = pygame.display.set_mode((650, 500))
        flag_Suggetion = False
        flag_seeSolition = False
        running = True
        myFort = font.SysFont("Calibri",25)
        self.startTime = pygame.time.get_ticks()
        while running:
            self.chronometer()
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                
                elif event.type == pygame.KEYDOWN:
                    if (event.key == K_RIGHT):
                        if self.checkMove(0, 1):
                            self.player.move(40, 0)
                        else:
                            self.badFeedback()
                    elif (event.key == K_LEFT):
                        if self.checkMove(0, -1):
                            self.player.move(-40, 0)
                        else:
                            self.badFeedback()
                    elif (event.key == K_UP):
                        if self.checkMove(-1, 0):
                            self.player.move(0, -40)
                        else:
                            self.badFeedback()
                    elif (event.key == K_DOWN):
                        if self.checkMove(1, 0):
                            self.player.move(0, 40)
                        else:
                            self.badFeedback()
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
                    if flag_seeSolition == False:
                        self.player.type = "Exitosa"
                    self.addStat()
                    running = False

            App.screen.fill((0, 0, 50))
            
            
            for wall in walls:
                pygame.draw.rect(App.screen , (255, 255, 255), wall.rect)
            
            if (flag_seeSolition):
                for way in ways:
                    App.screen.blit(way.img, way.rect)
                for element in self.seeSolition_list:
                    pygame.draw.rect(App.screen , (0, 128, 0), element,4)
            else:
                for way in ways:
                    App.screen.blit(way.img, way.rect)
                    
            pygame.draw.rect(App.screen , (255, 0, 0), self.end_rect)
            pygame.draw.rect(App.screen , (255, 200, 0),self.player.rect)

            texto1 = myFort.render("Verify",True,(255,255,255))
            texto2 = myFort.render("Suggetion",True,(255,255,255))
            texto3 = myFort.render("See Solution",True,(255,255,255))
            texto4 = myFort.render("Restart",True,(255,255,255))

            self.screen.blit(texto1,(self.button_verify.x+(self.button_verify.width-texto1.get_width())/2,
                        self.button_verify.y+(self.button_verify.height-texto1.get_height())/2))

            self.screen.blit(texto2,(self.button_suggetion.x+(self.button_suggetion.width-texto2.get_width())/2,
                        self.button_suggetion.y+(self.button_suggetion.height-texto2.get_height())/2))
            
            self.screen.blit(texto3,(self.button_seeSolition.x+(self.button_seeSolition.width-texto3.get_width())/2,
                        self.button_seeSolition.y+(self.button_seeSolition.height-texto3.get_height())/2))

            self.screen.blit(texto4,(self.button_reboot.x+(self.button_reboot.width-texto4.get_width())/2,
                        self.button_reboot.y+(self.button_reboot.height-texto4.get_height())/2))
            
            self.drawChronometer()
            pygame.display.flip()
            self.clock.tick(30)
            if (flag_Suggetion):
                for element in self.suggetion_list:
                    pygame.draw.rect(App.screen , (0, 128, 0), element,4)
                pygame.display.update()
                time.sleep(0.25)
                flag_Suggetion = False
        pygame.display.update()
    
    def badFeedback(self):
        pygame.draw.rect(self.screen, (255, 0, 0), self.player.rect)
        pygame.display.update()
        time.sleep(0.12)

    def goodFeedback(self):
        pygame.draw.rect(self.screen, (0, 170, 228), self.player.rect)
        pygame.display.update()
        time.sleep(0.12)

"""
*Game initialization
"""
if __name__ == '__main__':
    App().mainMenu()

