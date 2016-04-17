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

player_fall_right = pygame.image.load("sprites/player_fall_right.png")
player_fall_left = pygame.image.load("sprites/player_fall_left.png")

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

# Tilesets
tileset_template = pygame.image.load("sprites/tileset_template.png")
tileset_grass = pygame.image.load("sprites/tileset_grass.png")
tileset_details = pygame.image.load("sprites/tileset_details.png")

# Backgrounds & clouds
sky_background = pygame.image.load("sprites/background.png")
cloud = pygame.image.load("sprites/cloud.png")

# -- SOUNDS --
#jump = pygame.mixer.Sound("sounds/jump.wav")
roll = pygame.mixer.Sound("sounds/roll.wav")
footstep_1 = pygame.mixer.Sound("sounds/footstep_1.wav")
