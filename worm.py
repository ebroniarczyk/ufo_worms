import pygame, time, math
from weapon import Weapon

class Worm(object):
    
    def __init__(self, game, battle, x, color, ground):
        self.game = game
        self.x = x
        self.y = 300.0
        self.worm_size = (64,64)
        self.face_right = True
        self.v_vertical = 0
        self.v_horizontal = 0
        self.moving = False
        self.jumping = True
        self.t_init_jump = time.clock()
        self.t_jump = time.clock()
        self.gravity = game.gravity
        self.current_y = 0
        self.gunpoint_position = (0, 0)
        self.angle = 0
        self.battle = battle
        self.team_color = color
        self.hp = 100
        self.is_alive = True
        self.myfont = pygame.font.SysFont('Calibri', 20)
        self.ground = ground

    def draw(self, screen):
        """
        Draws aliens and their hp on screen.
        """
        if self.is_alive:
            image = None
            if self.moving:
                image = pygame.transform.scale(self.game.images[self.team_color][1], (64, 128))
            elif self.jumping:
                image = pygame.transform.scale(self.game.images[self.team_color][3], (64, 128))
            else:
                image = pygame.transform.scale(self.game.images[self.team_color][0], (64, 128))

            if self.face_right == False:
                image = pygame.transform.flip(image, True, False)

            # pygame.draw.rect(screen, (210, 0, 90), pygame.Rect(self.x, self.y, self.worm_size[0], self.worm_size[1]))
            screen.blit(image, pygame.Rect(self.x, self.y - 64, self.worm_size[0], self.worm_size[1]))

            hp_text = self.myfont.render(str(self.hp)+' hp', False, (200,40,70))
            screen.blit(hp_text, (self.x + 10, self.y - 30))

    def get_gunpoint_position(self):
        """
        Returns gunpoint coordinates.
        """
        return(self.gunpoint_position)

    def get_position(self):
        """
        Returns alien coordinates.
        """
        return(self.x, self.y)

    def action(self, key, key_event_type):
        """
        Makes alien move right/left, jump by pressing appropriate keys.
        Controls gunpoint position.
        """
        if key == pygame.K_UP and self.angle < 90:
            self.angle += 0.1
        elif key == pygame.K_DOWN and self.angle > -90:
            self.angle -= 0.1
        if self.jumping == False:
            if key == pygame.K_RIGHT:
                self.moving = True
                self.__update_x(1)
                self.face_right = True
                if key_event_type == pygame.KEYUP:
                    self.moving = False
            if key == pygame.K_LEFT:
                self.moving = True
                self.__update_x(-1)
                self.face_right = False
                if key_event_type == pygame.KEYUP:
                    self.moving = False
        if key == pygame.K_RETURN and key_event_type == pygame.KEYDOWN and self.jumping == False:
            if self.battle.sound:
                jumping_sound = pygame.mixer.Sound("jump.wav")
                jumping_sound.play()
            self.jumping = True
            self.current_y = self.y
            self.t_init_jump = time.clock()
            self.t_jump = self.t_init_jump
            self.v_vertical = 500
            if self.face_right:
                self.v_horizontal = 50
            if self.face_right == False:
                self.v_horizontal = -50
        self.check_preparation()

    def update_hp(self, hp_change):
        """
        Updates hp of an alien and sets `is.alive` as False if hp <= 0.
        """
        self.hp = self.hp - hp_change
        if self.hp <=0:
            self.hp = 0
            self.is_alive = False

    def check_preparation(self):
        """
        Starts new round if alien starts to move/jump during the preparation time.
        """
        if self.battle.get_preparation() and (self.moving or self.jumping):
            self.battle.next_round()

    def update(self):
        """
        Updates gunpoint coordinates and coordinates of an alien while jumping.
        """
        self.__update_gunpoint_position()
        self.__update_position_after_jump()

    def __update_x(self, delta_x):
        """
        Changes x-coordinate of an alien by delta_x.
        """
        if not self.ground.check_collision(self.x + delta_x, self.y, self.worm_size[0], self.worm_size[1], self):
            self.x += delta_x
            if not self.ground.check_collision(self.x, self.y+1, self.worm_size[0], self.worm_size[1], self) and self.jumping == False:
                self.jumping = True
                self.t_init_jump = time.clock()
                self.t_jump = self.t_init_jump
            if self.x <0:
                self.x = 0
            elif self.x > 1200:
                self.x = 1200 - self.worm_size[0]   
        else:
            self.v_horizontal = 0 
            

    def __update_y(self, delta_y):
        """
        Changes y-coordinate of an alien by delta_y.
        """
        if not self.ground.check_collision(self.x, self.y+delta_y, self.worm_size[0], self.worm_size[1], self):
            self.y += delta_y
            return True
        else:
            self.v_vertical = 0
            return False

    def __update_position_after_jump(self):
        """
        Updates coordinates of an alien while jumping.
        """
        if self.jumping:
            delta = 1/60
            if(time.clock()-self.t_jump >= delta):
                self.t_jump = time.clock()
                v_vert = self.v_vertical - (self.t_jump - self.t_init_jump) * self.gravity
                if (self.v_horizontal != 0):
                    self.__update_x(self.v_horizontal*delta)
                if not self.__update_y(- v_vert*delta):
                    self.jumping = False
            
    def __update_gunpoint_position(self):
        """
        Sets coordinates of a gunpoint.
        """
        angle_radians = math.radians(self.angle)
        if self.face_right:
            self.gunpoint_position = (int(self.x + self.worm_size[0] / 2 + 150*math.cos(angle_radians)) , int(self.y + self.worm_size[1] / 2 - 150*math.sin(angle_radians)))
        else:
            self.gunpoint_position = (int(self.x + self.worm_size[0] / 2 - 150*math.cos(angle_radians)) , int(self.y + self.worm_size[1] / 2 - 150*math.sin(angle_radians)))

    
