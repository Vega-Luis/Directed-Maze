from pygame import *
import pygame
from pygame.locals import *

"""
* Class InputText
* This class is used to get the address of a file
"""
class InputText:

    def __init__(self):
        self.input_box = ""
        self.button = ""
        self.font = ""
        self.color_inactive = "" 
        self.color_active = ""
        self.color = ""        
        self.active = ""
        self.text = ''
    """
    * Function: Run 
    * Use to initialize the class and get de file path
    * @return {String}: return the file path
    """    
    def run(self):
        pygame.init()
        pygame.scrap.init()
        flags = RESIZABLE
        InputText.screen = pygame.display.set_mode((600, 180))
        InputText.running = True

        self.input_box = pygame.Rect(50, 60, 400, 40)
        self.button = Rect(250,120,90,30)
        self.color_inactive = pygame.Color('black')
        self.color_active = pygame.Color('white')
        self.color = self.color_inactive
        self.active = False
        self.text = ''
        while InputText.running:
            for event in pygame.event.get():
                if (event.type == QUIT):
                    InputText.running = False
                
                elif (event.type == pygame.MOUSEBUTTONDOWN):
                    if (self.input_box.collidepoint(event.pos)):
                        self.active = not self.active
                    else:
                        self.active = False
                    self.color = self.color_active if self.active else self.color_inactive
                    
                    if (self.button.collidepoint(mouse.get_pos())):
                        if (self.text!=''):
                            return self.text

                elif (event.type == pygame.KEYDOWN):
                    if (self.active):
                        if (event.key == pygame.K_RETURN):
                            if (self.text!=''):
                                return self.text
                        elif event.key == pygame.K_v and event.mod & pygame.KMOD_CTRL:
                            self.text = pygame.scrap.get("text/plain;charset=utf-8").decode()

                        elif (event.key == pygame.K_BACKSPACE):
                            self.text = self.text[:-1]
                        
                        else:
                            self.text += event.unicode
                        
            font = pygame.font.Font(None, 32)
            fontText = pygame.font.Font(None, 20)
            InputText.screen.fill(pygame.Color('gray'))
            txt_surface = fontText.render(self.text, True, (0,0,0))
            width = max(500, txt_surface.get_width()+10)
            self.input_box.w = width
            InputText.screen.blit(txt_surface, (self.input_box.x+5, self.input_box.y+5))
            pygame.draw.rect(InputText.screen, self.color, self.input_box, 2)

            text_button = font.render("Accept",True,(0,0,0))
            titulo = font.render("Enter file path",True,(0,0,0))

            InputText.screen.blit(text_button,(self.button.x+(self.button.width-text_button.get_width())/2,
                        self.button.y+(self.button.height-text_button.get_height())/2))

            InputText.screen.blit(titulo,(self.button.x+(self.button.width-titulo.get_width())/2,
                        10+(self.button.height-titulo.get_height())/2))

            pygame.display.flip()

        pygame.quit()

