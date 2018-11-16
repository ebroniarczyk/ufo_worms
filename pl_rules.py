import pygame

class RulesPL(object):

    def __init__(self, menu):
        self.show = False
        self.myfont = pygame.font.SysFont('Courier', 15)
        self.menu = menu
        self.color = (200, 230, 150)
        self.English_chosen = True

    def draw(self, screen):
        """
        Draws rules of the game.
        """
        if self.show:
            if self.English_chosen == False:
                Dict = {
                    "line1" : self.myfont.render("Witajcie! Czas poznać zasady gry :)", False, self.color),
                    "line2" : self.myfont.render("Jest to zabawa dla 2-4 osób. Każdy gracz ma swoją drużynę kosmitów.", False, self.color),
                    'line3' : self.myfont.render("Celem gry jest zniszczenie drużyny przeciwników.", False, self.color),
                    'line4' : self.myfont.render("W prawym górnym rogu odliczany jest czas.", False, self.color),
                    'line5' : self.myfont.render("Każdy gracz ma 10s na wybór kosmity (za pomocą przycisku 'Tab').", False, self.color),
                    'line6' : self.myfont.render("Jeśli gracz wykona dowolny ruch - czas na przygotowanie się kończy i zaczyna się odliczanie czasu rundy.", False, self.color),
                    'line7' : self.myfont.render("Można się poruszać za pomocą strzałek w lewo i prawo, zaś strzałki w górę i w dół zmieniają kierunek strzału.", False, self.color),
                    'line8' : self.myfont.render("W celu skorzystania z broni, należy wcisnąć spację. Im dłużej trzymana - tym większa siła wystrzału.", False, self.color),
                    'line9' : self.myfont.render("Naciśnięcie klawisza Enter spowoduje skok.", False, self.color),
                    'line10' : self.myfont.render("Przysisk 'M' wyłącza/włącza dźwięk.", False, self.color),
                    'line11' : self.myfont.render("Jeśli wszystko jasne - wybierz Enter.", False, self.color)
                }
            else:
                Dict = {
                    'line1' : self.myfont.render("Hi! It's time to understand the rules.", False, self.color),
                    'line2' : self.myfont.render("It's game for 2-4 people. Each playes has their own team of aliens.", False, self.color),
                    'line3' : self.myfont.render("The aim of this game is destruction of opponent's team.", False, self.color),
                    'line4' : self.myfont.render("In the upper right corner there is a timer.", False, self.color),
                    'line5' : self.myfont.render("Each player has 10s for choosing an alien to play (using 'Tab').", False, self.color),
                    'line6' : self.myfont.render("If player makes a move, preparation time ends and round time starts.", False, self.color),
                    'line7' : self.myfont.render("You can use arrows to move right or left, wheras up/down arrows change shooting direction.", False, self.color),
                    'line8' : self.myfont.render("To use the weapon, press Spcabar. The longer you press it, the farther alien shoots.", False, self.color),
                    'line9' : self.myfont.render("Pressing Enter makes the alien jump.", False, self.color),
                    'line10' : self.myfont.render("'M' key turns off/on the sound", False, self.color),
                    'line11' : self.myfont.render("If everything is clear - press Enter.", False, self.color)
                }

            for i in range(1,12):
                screen.blit(Dict["line"+str(i)], (50,50+20*(i-1)))

    def action(self, key, key_event_type):
        """
        Goes to 'settings page'.
        """
        if (self.show):
            if (pygame.K_KP_ENTER == key or pygame.K_RETURN == key) and key_event_type == pygame.KEYUP:
                self.show = False
                self.menu.English_chosen = self.English_chosen
                self.menu.showtime()

    def showtime(self):
        """
        Sets `show` as true.
        """
        self.show = True
