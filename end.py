import pygame

class End(object):

    def __init__(self, menu, battle):
        self.show = False
        self.myfont = pygame.font.SysFont('Courier', 31)
        self.color = (200, 230, 150)
        self.menu = menu
        self.battle = battle

    def draw(self, screen):
        """
        Draws 'end game page'.
        """
        if self.battle.end_show:
            if self.menu.English_chosen:
                win = self.myfont.render("You won!", False, self.color)
            else:
                win = self.myfont.render("Wygrałeś!", False, self.color)
        
            screen.blit(win, (520,300))
            