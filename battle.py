import pygame, random, time
import numpy as np
from menu import Menu
from team import Team

class Battle(object):

    def __init__(self, game, ground):
        self.show = False
        self.teams = []
        self.selected_team = 0
        self.worms_position = []
        self.game = game
        self.round_time_left = 10
        self.preparation = True
        self.time = int(time.clock())
        self.myfont = pygame.font.SysFont('Calibri', 24)
        # self.background = pygame.transform.scale(pygame.image.load("bg.png"), (1200, 700))
        self.sound = True
        self.ground = ground
        self.end_show = False

    def start_battle(self, number_of_teams, number_of_worms):
        """
        Sets initial positions of aliens.
        """
        tw = number_of_teams * number_of_worms
        a = 0
        b = int(1200 / tw)
        for i in range(tw):
            x = random.randrange(a, a + b - 50)
            self.worms_position.append(x)
            a = a + b
        np.random.shuffle(self.worms_position)

        for i in range(number_of_teams):
            self.teams.append(Team(self.game, self, self.worms_position[(i*number_of_worms):((i+1)*number_of_worms)], i, self.ground))
        self.show = True

    def draw(self, screen):
        """
        Draws surface on which aliens can move.
        Marks selected alien by arrow above its head.
        Calls `draw` from Team class.
        Draws gunpoint.
        Draws timer (measuring time of preparaion and round).
        """
        if self.show:
            for i in range(12):
                for j in range(60):
                    if self.ground.matrix.item((i,j)) == 1:
                        screen.blit(self.ground.block, pygame.Rect(j*20, 700-20*(i+1), 20, 20))

            for team in self.teams:
                team.draw(screen)
            w = self.teams[self.selected_team].get_selected_worm()
            x, y = w.get_position()
            pygame.draw.polygon(screen, (255,255,255), ((x+32, y-15), (x+27, y-25), (x+37, y-25)))
            if w.moving == False and w.jumping == False:
                pygame.draw.circle(screen, (255, 255, 255), w.get_gunpoint_position(), 4)
            
            time_left = self.myfont.render(str(self.round_time_left), False, (200,200,200))
            window_x, window_y = pygame.display.get_surface().get_size()

            screen.blit(time_left, (window_x - 50, 50))
            

    def get_all_worms(self):
        """
        Returns all worms.
        """
        w = []
        for team in self.teams:
            for worm in team.worms:
                w.append(worm)
        return(w)

    def action(self, key, key_event_type):
        """
        Turns on/off all sounds.
        """
        if self.show:
            self.teams[self.selected_team].action(key, key_event_type)
            if key == pygame.K_m and key_event_type == pygame.KEYDOWN:
                if self.sound:
                    self.sound = False
                else:
                    self.sound = True

    def update(self):
        """
        Changes round.
        Calls `update` function from Team class.
        """
        if self.show:
            self.counter()
            for team in self.teams:
                team.update()
            if self.round_time_left <= 0:
                self.next_round()

    def get_preparation(self):
        "Returns true if it's preparation time."
        return(self.preparation)

    def next_round(self):
        """
        Sets timer depending preparation - 10s for preparation, 15s for round.
        Changes teams in the consecutive rounds.
        """
        if self.preparation:
            self.preparation = False
            self.round_time_left = 15
        else:
            self.preparation = True
            self.round_time_left = 10
            self.teams[self.selected_team].weapons[self.teams[self.selected_team].selected_weapon].shooting = False
            self.teams[self.selected_team].weapons[self.teams[self.selected_team].selected_weapon].force = 0
            self.selected_team = (self.selected_team + 1) % len(self.teams)
            self.teams[self.selected_team].change_worm()

    def get_time(self):
        """
        Returns time left to the end of preparation/round.
        """
        return self.round_time_left

    def counter(self):
        """
        Creates timer.
        """
        if self.time != int(time.clock()):
            self.time = int(time.clock())
            self.round_time_left -= 1


            
        

