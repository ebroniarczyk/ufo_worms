import pygame
from weapon import Weapon
from worm import Worm

class Team(object):

    def __init__(self, game, battle, worms_positions, color, ground):
        self.game = game
        self.worms = []
        self.selected_worm = 0
        self.selected_weapon = 0
        self.battle = battle
        for e in worms_positions:
            self.worms.append(Worm(game, battle, e, color, ground))
        self.weapons = [Weapon(self, self.battle, game)] * 4

    def draw(self, screen):
        """
        Draws aliens for each team.
        """
        for worm in self.worms:
            worm.draw(screen)
        self.weapons[self.selected_weapon].draw(screen)

    def get_selected_worm(self):
        """
        Returns alien selected in particular round.
        """
        return(self.worms[self.selected_worm])
        
    def action(self, key, key_event_type):
        """
        Changes selected alien by pressing Tab key.
        """
        self.worms[self.selected_worm].action(key, key_event_type)
        self.weapons[self.selected_weapon].action(key, key_event_type)
        if key == pygame.K_TAB and key_event_type == pygame.KEYDOWN:
            self.change_worm()

    def change_worm(self):
        """
        Automatically changes selected alien during preparation and makes it current owner of a weapon.
        """
        if self.battle.preparation:
            self.selected_worm = (self.selected_worm + 1) % len(self.worms)
        for weapon in self.weapons:
            weapon.set_current_owner()

    def update(self):
        """
        Calls `update` functions from Worm and Weapon classes.
        """
        for worm in self.worms:
            worm.update()
        self.weapons[self.selected_weapon].update()