import pygame
import numpy as np
import random

class Ground(object):

    def __init__(self):
        self.matrix = np.array(
            [   
                [1]*60,
                [1]*60,
                [1]*60,
                [1]*60,
                [1 if e <30 or e>45 else 0 for e in range(60)],
                [1 if e <30 or e>45 else 0 for e in range(60)],
                [1 if e <25 or e>45 else 0 for e in range(60)],
                [1 if e <20 or e>50 else 0 for e in range(60) ],
                [1 if e <20 or e>50 else 0 for e in range(60) ],
                [1 if (e > 6 and e <17) or e>55 else 0  for e in range(60)],
                [1 if (e > 9 and e <15) or e>55 else 0  for e in range(60)],
                [1 if (e > 9 and e <15) or e>55 else 0  for e in range(60)]
            ]
        )
        self.block = pygame.transform.scale(pygame.image.load("planet.png"), (20,20))

    def check_collision(self,x, y, x_size, y_size, worm):
        """
        Checks if there is a collision between the aliens and the ground.
        """
        k = 35 - int(y//20)
        l = int(x//20)
        for i in range(k - 5, k + 5):
            for j in range (l - 5, l + 5):
                if ( i < 12 and j < 60 and i >= 0 and j >= 0 and self.matrix.item((i,j)) == 1 and
                    (self.coordinates_in_range(x, y + y_size, i, j, worm) or self.coordinates_in_range(x + x_size, y + y_size, i, j, worm))):
                        return True
        return False
    
                
    def coordinates_in_range(self,x,y,i,j, worm):
        """
        Checks if coordinates of an alien collide with particular part of the planet surface.
        """
        if x >= j*20 and x<=(j+1)*20  and y >= 700-20*(i+1) and y <= 700-20*i:
            if worm.jumping:
                worm.y = 700-20*(i+1)-worm.worm_size[1] -1
            return True