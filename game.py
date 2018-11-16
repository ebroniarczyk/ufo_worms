import pygame
import os
from worm import Worm
from weapon import Weapon
from menu import Menu
from battle import Battle
from language import Language
from pl_rules import RulesPL
from ground import Ground
from end import End

class Game(object):
    
    def __init__(self):
        
        pygame.init()
        
        self.images = []
        for i in range(1,5):
            self.images.append([pygame.image.load(str(i) + '.1.png'),
                                pygame.image.load(str(i) + '.2.png'),
                                pygame.image.load(str(i) + '.3.png'),
                                pygame.image.load(str(i) + '.4.png'),
                                pygame.image.load(str(i) + '.5.png')])
        
        self.gravity = 1000

        self.ground = Ground()
        self.battle = Battle(self, self.ground)
        self.menu = Menu(self.battle)
        self.pl_rules = RulesPL(self.menu)
        self.language = Language(self.pl_rules)
        self.end = End(self.menu, self.battle)
        pygame.font.init()
        self.screen = pygame.display.set_mode((1200, 700))
        pygame.display.set_caption('Worms')

        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    os._exit(1)
                if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                    self.battle.action(event.key, event.type)
                    self.menu.action(event.key, event.type)
                    self.pl_rules.action(event.key, event.type)
                    self.language.action(event.key, event.type)
                    
            keys = pygame.key.get_pressed()
            for i in range(len(keys)):
                if keys[i] == True:
                    self.battle.action(i, None)

            self.battle.update()
            self.screen.fill((0,0,0))
            # if self.battle.show:
            #     self.screen.blit(self.battle.background, (0,0)) 
            self.language.draw(self.screen)
            self.pl_rules.draw(self.screen)
            self.menu.draw(self.screen)
            self.battle.draw(self.screen)
            self.end.draw(self.screen)

            pygame.display.flip()
    
if __name__ == "__main__":
    Game()