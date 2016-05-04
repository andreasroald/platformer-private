import pygame

# Initialize pygame so that sounds can load
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

# -- IMAGES --

# Player sprites
player_walk_1_right = pygame.image.load("sprites/player_walk_1_right.png")
player_walk_2_right = pygame.image.load("sprites/player_walk_2_right.png")
player_walk_3_right = pygame.image.load("sprites/player_walk_3_right.png")
player_walk_4_right = pygame.image.load("sprites/player_walk_4_right.png")

player_walk_1_left = pygame.image.load("sprites/player_walk_1_left.png")
player_walk_2_left = pygame.image.load("sprites/player_walk_2_left.png")
player_walk_3_left = pygame.image.load("sprites/player_walk_3_left.png")
player_walk_4_left = pygame.image.load("sprites/player_walk_4_left.png")

player_walk_list_right = [player_walk_1_right, player_walk_2_right,
                          player_walk_3_right, player_walk_4_right]

player_walk_list_left = [player_walk_1_left, player_walk_2_left,
                          player_walk_3_left, player_walk_4_left]

player_jump_right = pygame.image.load("sprites/player_jump_right.png")
player_jump_left = pygame.image.load("sprites/player_jump_left.png")

player_roll_right_1 = pygame.image.load("sprites/player_roll_right_1.png")
player_roll_right_2 = pygame.image.load("sprites/player_roll_right_2.png")
player_roll_right_3 = pygame.image.load("sprites/player_roll_right_3.png")
player_roll_right_4 = pygame.image.load("sprites/player_roll_right_4.png")

player_roll_list_right = [player_roll_right_1, player_roll_right_2, player_roll_right_3,
                          player_roll_right_4, player_roll_right_2, player_roll_right_1]

player_roll_left_1 = pygame.image.load("sprites/player_roll_left_1.png")
player_roll_left_2 = pygame.image.load("sprites/player_roll_left_2.png")
player_roll_left_3 = pygame.image.load("sprites/player_roll_left_3.png")
player_roll_left_4 = pygame.image.load("sprites/player_roll_left_4.png")

player_roll_list_left = [player_roll_left_1, player_roll_left_2, player_roll_left_3,
                          player_roll_left_4, player_roll_left_2, player_roll_left_1]

# Attack sprites
fireball_right = pygame.image.load("sprites/fireball_right.png")
fireball_left = pygame.image.load("sprites/fireball_left.png")

# Animals
bird_left_blue = pygame.image.load("sprites/bird_left_blue.png")
bird_right_blue = pygame.image.load("sprites/bird_right_blue.png")
bird_left_red = pygame.image.load("sprites/bird_left_red.png")
bird_right_red = pygame.image.load("sprites/bird_right_red.png")
bird_left_yellow = pygame.image.load("sprites/bird_left_yellow.png")
bird_right_yellow = pygame.image.load("sprites/bird_right_yellow.png")

# Tilesets
tileset_template = pygame.image.load("sprites/tileset_template.png")
tileset_grass = pygame.image.load("sprites/tileset_grass.png")
tileset_details = pygame.image.load("sprites/tileset_details.png")
tileset_oak_trees = pygame.image.load("sprites/tileset_oak_trees.png")
tileset_house_1 = pygame.image.load("sprites/tileset_house_1.png")
tileset_platforms = pygame.image.load("sprites/tileset_platforms.png")

# Backgrounds & clouds
sky_background = pygame.image.load("sprites/background.png")
cloud = pygame.image.load("sprites/cloud.png")

# -- SOUNDS --
#jump = pygame.mixer.Sound("sounds/jump.wav")
roll = pygame.mixer.Sound("sounds/roll.wav")
footstep_1 = pygame.mixer.Sound("sounds/footstep_1.wav")
fireball_sound = pygame.mixer.Sound("sounds/fireball.wav")

# -- SPRITE LISTS -- (used for pixel format converting)
player_list = [player_walk_1_right, player_walk_2_right, player_walk_3_right,
               player_walk_4_right, player_walk_1_left, player_walk_2_left,
               player_walk_3_left, player_walk_4_left, player_jump_right,
               player_jump_left, player_roll_right_1, player_roll_right_2,
               player_roll_right_3, player_roll_right_4, player_roll_right_2,
               player_roll_right_1, player_roll_left_1, player_roll_left_2,
               player_roll_left_3, player_roll_left_4, player_roll_left_2,
               player_roll_left_1]

attack_list = [fireball_right, fireball_left]

animal_list = [bird_left_blue, bird_right_blue, bird_left_red, bird_right_red,
               bird_left_yellow, bird_right_yellow]

tileset_list = [tileset_grass, tileset_details, tileset_oak_trees, tileset_house_1]

background_list = [sky_background, cloud]

all_sprites = [player_list, attack_list, animal_list, tileset_list, background_list]
