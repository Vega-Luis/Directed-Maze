from pygame import *
import pygame

class StatsWindow:
    """
     * @param statsText string formated statistics records
    """
    def __init__(self, statsText):
        self.statsText = statsText
        self.FONT_SIZE = 20
        self.FONT_COLOR = (0, 0, 0)
        self.yDisplacement = 10
        self.BACKGROUND_COLOR = (255, 255, 255)
        self.FONT_TYPE = None
        self.isRunning = True
        StatsWindow.screen = pygame.display.set_mode((650, 500), RESIZABLE)
    
    """
     * Runs the statistics window
    """
    def run(self):
        pygame.init()
        while self.isRunning:

            screenWidth, screenHeight = pygame.display.get_surface().get_size()
            self.screen.fill(self.BACKGROUND_COLOR)
            lines = self.statsText.splitlines()
            for i, l in enumerate(lines):
                font = pygame.font.SysFont(self.FONT_TYPE, self.FONT_SIZE)
                text = font.render(l, 0, self.FONT_COLOR)
                textCenter = text.get_rect()
                textCenter.center = (screenWidth // 2, self.yDisplacement +
                                self.FONT_SIZE* i)
                self.screen.blit(text, textCenter)

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.isRunning = False
                if event.type == pygame.MOUSEWHEEL:
                    self.yDisplacement = self.yDisplacement + (20 * event.y)
            pygame.display.flip()