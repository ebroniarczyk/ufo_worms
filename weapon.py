import pygame, math, time
from enum import Enum

class WeaponType(Enum):

    MELEE = 1
    LOADABLE = 2
    DOUBLE_SHOT = 3

# bazuka, granat, paluch, strzelba    

class Weapon(object):

    def __init__(self, team, battle, game):
        self.team = team
        self.owner = team.get_selected_worm()
        self.force = 0
        self.ammo = -1
        self.gravity = game.gravity
        self.type = WeaponType.LOADABLE
        self.shooting = False
        self.bullet_x = int(self.owner.x + int(self.owner.face_right) * self.owner.worm_size[0])
        self.bullet_y = int(self.owner.y + self.owner.worm_size[1]/2)
        self.bullet_current_y = 0
        self.t_init_shot = 0
        self.t_shot = 10e8
        self.bullet_v_vertical = 0
        self.bullet_v_horizontal = 0
        self.battle = battle

    def set_current_owner(self):
        """
        Sets current owner of the weapon.
        """
        self.owner = self.team.get_selected_worm()
        self.bullet_x = int(self.owner.x + self.owner.worm_size[0]/2)
        self.bullet_y = int(self.owner.y + self.owner.worm_size[1]/2)

    def draw(self, screen):
        """
        Draws bullet and rectangle of shot force.
        """
        if self.type == WeaponType.LOADABLE:
            if self.shooting == False and self.force != 0:
                pygame.draw.rect(screen, (255,255,255), pygame.Rect(1100, 650, 70, 20), 1)
                pygame.draw.rect(screen, (255,255,255), pygame.Rect(1100, 650, int(self.force), 20))
            if self.shooting == True:
                pygame.draw.circle(screen, (200,20,0), (int(self.bullet_x), int(self.bullet_y)), 4)

    def action(self, key, key_event_type):
        """
        Makes alien shoot if Spacebar is pressed.
        """
        if key == pygame.K_SPACE and self.type == WeaponType.LOADABLE:
            self.force += 0.1
            if self.force >= 70 or key_event_type == pygame.KEYUP:
                self.__shoot()
            # if self.battle.get_preparation() == False and self.battle.get_time() <=1:
            #     self.__shoot()
            #     self.force = 0
                if self.battle.sound:
                    shooting_sound = pygame.mixer.Sound("shoot.wav")
                    shooting_sound.play()
        self.check_preparation()

    def check_preparation(self):
        """
        Starts new round if alien starts to shoot during preparation time.
        """
        if self.battle.get_preparation() and self.shooting:
            self.battle.next_round()
            
    def update(self):
        """
        Updates bullet coordinates.
        """
        self.__update_bullet_position()

    def __shoot(self):
        if self.type == WeaponType.LOADABLE and self.shooting == False :
            self.shooting = True
            self.bullet_x = int(self.owner.x + self.owner.worm_size[0]/2)
            self.bullet_y = int(self.owner.y + self.owner.worm_size[1]/2)
            self.bullet_current_y = self.bullet_y  + self.owner.worm_size[1]/2
            self.t_init_shot = time.clock()
            self.t_shot = self.t_init_shot
            angle_radians = math.radians(self.owner.angle)
            self.bullet_v_vertical = 20*self.force*math.sin(angle_radians)
            if self.owner.face_right:
                self.bullet_v_horizontal = 20*self.force*math.cos(angle_radians)
            if self.owner.face_right == False:
                self.bullet_v_horizontal = -20*self.force*math.cos(angle_radians)
        self.force = 0

    def __update_bullet_position(self):
        """
        Sets bullet coordinates.
        Checks if any alien is hit.
        Removes alien when its hp = 0.
        """
        if self.shooting:
            delta = 1/300
            if(time.clock()-self.t_shot >= delta):
                self.t_shot = time.clock()
                v_vert = self.bullet_v_vertical - (self.t_shot - self.t_init_shot) * self.gravity
                self.bullet_x = self.bullet_x + self.bullet_v_horizontal*delta
                self.bullet_y = self.bullet_y - v_vert*delta
                if self.bullet_y >= 700:
                    self.shooting = False
                for worm in self.battle.get_all_worms():
                    if (worm != self.owner and worm.is_alive and
                    int(self.bullet_x) in range(int(worm.x), int(worm.x)+worm.worm_size[0]) and int(self.bullet_y) in range(int(worm.y), int(worm.y)+worm.worm_size[1])):
                        self.shooting = False
                        worm.update_hp(50)
                        if worm.is_alive == False:
                            for team in self.battle.teams:
                                if worm in team.worms:
                                    team.worms.remove(worm)
                                    if len(team.worms) == 0:
                                        self.battle.teams.remove(team)
                                        if len(self.battle.teams) == 1:
                                            self.battle.show = False
                                            self.battle.end_show = True
