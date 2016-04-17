import random

import pygame

from settings import *
from sprites import *
from tiles import *
from levels import *

# Create the game class
class Game:
    # Initialize the game class
    def __init__(self):
        pygame.init()

        self.game_display = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.running = True # To exit the game completely, make running False

    # Function that creates a level from a list and returns the level list
    def create_level(self, level, solid=True):
        level_x = 0

        # Make the bottom-left tile aligned with the bottom-left of the screen
        if len(level) <= 20:
            level_y = 0
        else:
            level_y = 0 - (32 * (len(level) - 20))

        for rows in level:
            for cols in rows:
                for tilesets in tileset_list:
                    if int(cols) == tilesets.id:
                        for tiles in tilesets.all_tiles:
                            if cols == tiles["id"]:
                                w = Wall(level_x, level_y, 32, 32, image=tiles["image"])
                                if solid:
                                    self.walls.add(w)
                                else:
                                    self.details.add(w)

                level_x += 32
            level_x = 0
            level_y += 32

        return level

    # Starting a new game
    def new(self):
        # Sprite groups
        self.walls = pygame.sprite.Group()
        self.details = pygame.sprite.Group()
        self.clouds = pygame.sprite.Group()

        # Creating an instance of the player
        self.player = Player(self.walls)

        # Create the level and set current_level to its level list (used for camera movement)
        self.current_level = self.create_level(level)

        # Create the details Layer
        self.create_level(level_details, solid=False)

        # We blit surfaces to the world surface, then blit the world surface to the game display
        self.world_surface = pygame.Surface((len(self.current_level[0]) * 32, display_height))
        self.background = pygame.Surface((display_width, display_height))
        self.background.blit(sky_background, (0, 0))

        # Camera variables
        self.cam_x_offset = 0

        # Screen shake variables
        self.shake_amount = 10

        # Starting the game loop
        self.loop()

    # Game loop
    def loop(self):
        self.playing = True # To reset the game, but not close it, make playing False
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

    # Game loop - Events
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_w:
                    if self.player.jumping:
                        self.player.test_for_jump()
                    else:
                        self.player.jump()

    # Game loop - Updates
    def update(self):
        self.player.update()
        self.clouds.update()

        # Horizontal Camera scrolling
        if self.player.rect.center[0] > self.cam_x_offset + 800 / 2:
            if self.player.x_velocity > 0 and self.cam_x_offset < (len(self.current_level[0]) - 25) * 32:
                self.cam_x_offset += abs(self.player.x_velocity)

        if self.player.rect.center[0] < self.cam_x_offset + 800 / 2:
            if self.player.x_velocity < 0 and self.cam_x_offset > 0:
                self.cam_x_offset -= abs(self.player.x_velocity)

        if self.cam_x_offset < 0:
            self.cam_x_offset = 0


        # Reset game if player is out of the screen
        if self.player.rect.y > display_height+64:
            self.playing = False

        # Randomly spawn clouds
        if random.randint(0, 700) == 700:
            c = Cloud(display_width, random.randint(0, 300))
            self.clouds.add(c)

        # Move clouds, and delete off screen clouds
        for clouds in self.clouds:

            if clouds.rect.x == 0 - clouds.rect.width:
                clouds.kill()

        # Slowly stop screen shake
        if self.shake_amount > 0:
            self.shake_amount -= 0.5

    # Game loop - Draw
    def draw(self):

        self.background.blit(sky_background, (0, 0))
        self.clouds.draw(self.background)
        self.world_surface.blit(self.background, (0+self.cam_x_offset, 0))

        self.player.draw(self.world_surface)
        self.walls.draw(self.world_surface)
        self.details.draw(self.world_surface)

        # If shake amount is more than 0, blit the world at a random location between
        # negative and positive shake amount, instead of 0, 0
        if self.shake_amount > 0:
            self.game_display.blit(self.world_surface, (random.randint(int(-self.shake_amount), int(self.shake_amount))-self.cam_x_offset,
                                                        random.randint(int(-self.shake_amount), int(self.shake_amount))))
        else:
            self.game_display.blit(self.world_surface, (0-self.cam_x_offset, 0))

        pygame.display.update()
        pygame.display.set_caption(title + " running at " + str(int(self.clock.get_fps())) + " frames per second")

# Creating the game object
game = Game()

# Starting the game loop
while game.running:
    game.new()

pygame.quit()
quit()
