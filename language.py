import pygame

class Language(object):

    def __init__(self, pl):
        self.show = True
        self.myfont = pygame.font.SysFont('Courier', 31)
        self.color = (200, 230, 150)
        self.polish_rules = pl

    def draw(self, screen):
        """
        Draws 'language page'.
        """
        if self.show:
            en1 = self.myfont.render("Let's start with choosing the LANGUAGE!", False, self.color)
            en2 = self.myfont.render("Press 'E' if it's English.", False, self.color)
            pl1 = self.myfont.render("Zacznijmy od wyboru języka!", False, self.color)
            pl2 = self.myfont.render("Wybierz 'P', jeśli jest nim polski.", False, self.color)

            screen.blit(en1, (50,50))
            screen.blit(en2, (50,100))
            screen.blit(pl1, (50,300))
            screen.blit(pl2, (50,350))

    def action(self, key, key_event_type):
        """
        Chooses language.
        """
        if (self.show):
            if (pygame.K_p == key):
                self.show = False
                self.polish_rules.showtime()
                self.polish_rules.English_chosen = False
            elif (pygame.K_e == key):
                self.show = False
                self.polish_rules.show = True

