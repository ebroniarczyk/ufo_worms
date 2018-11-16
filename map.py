import pygame
import numpy as np
import random

class Map(object):

    def __init(self):
        self.matrix = np.array(
            [   
                [1 if (e > 9 and e <15) or e>45 else 0  for e in range(60)],
                [1 if e <20 or e>50 else 0 for e in range(60) ],
                [1 if e <30 or e>45 else 0 for e in range(60)],
                [1]*60
                [1]*60
            ]
        )
        self.block = pygame.transform.scale(pygame.image.load("planet.png"), (20,20))

