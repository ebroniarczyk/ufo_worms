import pygame

class Menu(object):

    def __init__(self, battle):
        self.show = False
        self.number_of_teams = 2
        self.number_of_worms = 3
        self.selected_text = 0
        self.myfont = pygame.font.SysFont('Courier', 25)
        self.battle = battle
        self.English_chosen = True
        # self.music_file = pygame.mixer.music.load("music.mp3")
        # self.music_playing = True
        

    def draw(self, screen):
        """
        Draws 'settings page'.
        """
        if self.show:
            standard_color = (100,100,100)
            selected_color = (100, 0, 0)
            colors = [standard_color] * 2
            colors[self.selected_text] = selected_color

            if self.English_chosen:
                intro = self.myfont.render('Press Up/Down Arrows and +/- to adapt the settings.', False, (170,170,100))
                total_worms = self.myfont.render('Number of worms: '+ str(self.number_of_worms), False, colors[0])
                total_teams = self.myfont.render('Number of teams: '+ str(self.number_of_teams), False, colors[1])
                start_game = self.myfont.render('Press ENTER to start the game.', False, (170,170,100))
            else:
                intro = self.myfont.render("Użyj strzałek góra/dół oraz +/-, aby dostosować ustawienia.", False, (170,170,100))
                total_worms = self.myfont.render('Ilość kosmitów w drużynie: '+ str(self.number_of_worms), False, colors[0])
                total_teams = self.myfont.render('Ilość drużyn: '+ str(self.number_of_teams), False, colors[1])
                start_game = self.myfont.render('Wybierz ENTER, aby zacząć grę.', False, (170,170,100))

            screen.blit(intro, (50,50))
            screen.blit(total_worms, (50,120))
            screen.blit(total_teams, (50,170))
            screen.blit(start_game, (50, 500))

    def action(self, key, key_event_type):
        """
        Adjusts settings.
        """
        if (self.show):
            if (pygame.K_UP == key and pygame.KEYDOWN == key_event_type):
                self.selected_text = (self.selected_text + 1) % 2
            elif (pygame.K_DOWN == key and pygame.KEYDOWN == key_event_type):
                self.selected_text = (self.selected_text - 1) % 2
            elif (pygame.K_KP_PLUS == key or pygame.K_PLUS == key) and pygame.KEYDOWN == key_event_type:
                if (self.selected_text == 0 and self.number_of_worms < 5):
                    self.number_of_worms += 1
                elif (self.selected_text == 1 and self.number_of_teams < 4):
                    self.number_of_teams += 1
            elif (pygame.K_KP_MINUS == key or pygame.K_MINUS == key) and pygame.KEYDOWN == key_event_type:
                if (self.selected_text == 0 and self.number_of_worms > 1):
                    self.number_of_worms -= 1
                elif (self.selected_text == 1 and self.number_of_teams > 2):
                    self.number_of_teams -= 1
            elif (pygame.K_RETURN == key):
                self.show = False
                self.battle.start_battle(self.number_of_teams, self.number_of_worms)

    def showtime(self):
        """
        Sets `show` as true.
        """
        self.show = True
