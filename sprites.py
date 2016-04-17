import pygame
import random

from settings import *
from resources import *

# Player class
class Player(pygame.sprite.Sprite):
    # Initialize the player class
    def __init__(self, solid_list):
        pygame.sprite.Sprite.__init__(self)

        self.image = player_walk_1_right
        #self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.center = (64, 128)

        self.moving = False
        self.left_lock = False
        self.right_lock = False

        self.acceleration = 0
        self.x_top_speed = 6
        self.y_top_speed = 30
        self.x_velocity = 0
        self.y_velocity = 0

        self.jumping = False
        self.jump_rect = pygame.Rect((0, 0, 64, 48))
        self.should_jump = False

        self.should_roll = False
        self.roll_index = 0
        self.roll_counter = 0
        self.roll_list = player_roll_list_right

        self.walk_index = 0
        self.walk_counter = 0
        self.walk_list = player_walk_list_right
        self.direction = "right"
        self.footstep_counter = 0

        self.space = False

        # Solid list is the sprite group that contains the walls
        self.solid_list = solid_list

    # Player class event handling
    def events(self):
        #Reset moving & acceleration
        self.moving = False
        self.acceleration = 0

        # Movement keys handling
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and not self.left_lock:
            self.direction = "left"
            self.right_lock = True
            self.moving = True
            self.acceleration = -player_acc
            self.accelerate(self.acceleration)
        else:
            self.right_lock = False

        if keys[pygame.K_d] and not self.right_lock:
            self.direction = "right"
            self.left_lock = True
            self.moving = True
            self.acceleration = player_acc
            self.accelerate(self.acceleration)
        else:
            self.left_lock = False

        if not keys[pygame.K_d] and not keys[pygame.K_a]:
            if self.x_velocity != 0:
                self.moving = True
            self.accelerate(self.acceleration)

        # Check if space is still held
        if keys[pygame.K_SPACE] or keys[pygame.K_w]:
            self.space = True
        elif self.space:
            self.space = False

    #Accelerate the player movement with acc_movement
    def accelerate(self, acc_movement):
        if acc_movement > 0:
            if self.x_velocity == self.x_top_speed:
                self.x_velocity = self.x_top_speed

            elif acc_movement < self.x_top_speed:
                self.x_velocity += acc_movement

        elif acc_movement < 0:
            if self.x_velocity == -self.x_top_speed:
                self.x_velocity = -self.x_top_speed

            elif acc_movement > -self.x_top_speed:
                self.x_velocity += acc_movement

        #If x_velocity is not 0, slowly make x_velocity slower
        else:
            if self.x_velocity != 0:
                if self.x_velocity > 0:
                    # Decelerate faster than you accelerate
                    if self.x_velocity - player_acc * 3 > 0:
                        self.x_velocity -= player_acc * 3
                    else:
                        self.x_velocity -= player_acc
                elif self.x_velocity < 0:
                    if self.x_velocity + player_acc * 3 < 0:
                        self.x_velocity += player_acc * 3
                    else:
                        self.x_velocity += player_acc

    # Make the player jump
    def jump(self):
        if not self.jumping:
            self.jumping = True
            self.y_velocity = -15

    # If space is pressed and the jump rect is touching the ground, jump automaticly right after landing
    # This makes the game feel more responsive and prevents the "aw shit i pressed space why didnt i jump" - situations
    def test_for_jump(self):
        for tiles in self.solid_list:
            if self.jump_rect.colliderect(tiles.rect):
                self.should_jump = True
                break

    # Update the player class
    def update(self):
        self.events()

        # X-Axis movement
        if self.moving:
            self.rect.x += self.x_velocity

        # Check if the player hit any walls during X-movement
        hit_list = pygame.sprite.spritecollide(self, self.solid_list, False)
        for hits in hit_list:
            if self.x_velocity > 0:
                self.rect.right = hits.rect.left
                self.x_velocity = player_acc # Set x_velocity to player_acc/-player_acc so that x_velocity doesnt build up
            else:
                self.rect.left = hits.rect.right
                self.x_velocity = -player_acc

        # Y-Axis Movement
        if self.y_velocity < self.y_top_speed:
            self.y_velocity += player_grav
        self.rect.y += self.y_velocity

        # Cut jump if space is not pressed
        if self.y_velocity < -5:
            if not self.space:
                self.y_velocity = -5

        # Check if the player hit any walls during Y-movement
        hit_list = pygame.sprite.spritecollide(self, self.solid_list, False)
        for hits in hit_list:
            if self.y_velocity > 0:

                # Roll if player has enough momentum
                if self.should_roll == False and self.y_velocity > 18:
                    if self.x_velocity == self.x_top_speed or self.x_velocity == -self.x_top_speed:
                        self.should_roll = True
                        pygame.mixer.Sound.play(roll)

                self.rect.bottom = hits.rect.top
                self.y_velocity = player_grav # Set y_velocity to player_grav so that y_velocity doesnt build up
                self.jumping = False

                if self.should_jump:
                    self.jump()
                    self.should_jump = False

                break
            else:
                self.rect.top = hits.rect.bottom
                self.y_velocity = 0
                self.jumping = True
                break
        # If loop doesnt break, then player is in-air and shouldnt be able to jump
        else:
            self.jumping = True

        # Change list based on direction
        if self.direction == "left":
            self.walk_list = player_walk_list_left
        elif self.direction == "right":
            self.walk_list = player_walk_list_right

        # Walk animations and footstep sounds
        if self.x_velocity != 0 and not self.jumping:
            self.walk_counter = (self.walk_counter + 1) % 9

            if self.walk_counter == 8:
                self.walk_index = (self.walk_index + 1) % 4
                self.image = self.walk_list[self.walk_index]

            self.footstep_counter = (self.footstep_counter + 1) % 20

            if self.footstep_counter == 5:
                pygame.mixer.Sound.play(footstep_1)

        else:
            self.walk_index = 0
            self.image = self.walk_list[self.walk_index]


        # Prioritize jumping animations over walking animations
        if self.jumping:
            if self.direction == "left":
                self.image = player_jump_left
            elif self.direction == "right":
                self.image = player_jump_right

        # Player rolling
        if self.should_roll:
            if self.x_velocity < 0:
                self.roll_list = player_roll_list_left
            elif self.x_velocity > 0:
                self.roll_list = player_roll_list_right

            self.roll_counter = (self.roll_counter + 1) % 5

            if self.roll_counter == 4:
                self.roll_index += 1

            self.image = self.roll_list[self.roll_index]

            if self.roll_index >= 5:
                self.roll_index = 0
                self.roll_counter = 0
                self.should_roll = False

        # Reposition jump Rect
        self.jump_rect.top = self.rect.bottom
        self.jump_rect.x = self.rect.x

    # Player drawing function
    def draw(self, display):
        display.blit(self.image, self.rect)

# Wall class
class Wall(pygame.sprite.Sprite):
    # Initialize the wall class
    def __init__(self, x, y, w, h, color=black, image=None):
        pygame.sprite.Sprite.__init__(self)
        if image is None:
            self.image = pygame.Surface((w, h))
            self.image.fill(color)
        else:
            self.image = image

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Cloud class
class Cloud(pygame.sprite.Sprite):
    # Initialize the cloud class
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = cloud
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed = random.randrange(1, 3)

    # Slowly move to the left
    def update(self):
        self.rect.x -= self.speed
