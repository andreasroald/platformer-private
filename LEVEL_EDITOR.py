import pygame
import random

from settings import *
from tiles import *

class Wall(pygame.sprite.Sprite):
    # Initialize the wall class
    def __init__(self, x, y, w=32, h=32, color=black, image=None, id=0):
        pygame.sprite.Sprite.__init__(self)
        if image is None:
            self.image = pygame.Surface((w, h))
            self.image.fill(color)
        else:
            self.image = image

        self.id = id
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Editor:
    # Initialize the editor
    def __init__(self):
        pygame.init()

        # Ask for level width and level height, make the level 25x20 tiles (800x640px)
        # if non-valid value is entered
        try:
            self.display_width = int(input("Enter the level width: ")) * 32
        except (ValueError, EOFError):
            self.display_width = 25 * 32

        try:
            self.display_height = int(input("Enter the level height: ")) * 32
        except (ValueError, EOFError):
            self.display_height = 20 * 32

        self.level_surface = pygame.Surface((self.display_width, self.display_height))
        self.game_display = pygame.display.set_mode((self.display_width, self.display_height + 100))
        pygame.display.set_caption("LEVEL EDITOR v3")

        # Framerate
        self.clock = clock = pygame.time.Clock()
        self.FPS = 60

        self.running = True

    # Make text object
    def text_object(self, msg, color, size):

        if size == "small":
            self.text_surface = smallfont.render(msg, False, color)
        elif size == "medium":
            self.text_surface = medfont.render(msg, False, color)
        elif size == "large":
            self.text_surface = largefont.render(msg, False, color)
        elif size == "huge":
            self.text_surface = hugefont.render(msg, False, color)

        return self.text_surface, self.text_surface.get_rect()

    # Render the text object
    def render_text(self, msg, color, y_displace=0, x_displace=0,  size="small"):
        self.text_surface, self.text_rect = self.text_object(msg, color, size)
        self.text_rect.x = (self.display_width / 2) + x_displace
        self.text_rect.y = (self.display_height / 2) + y_displace
        self.game_display.blit(self.text_surface, self.text_rect)

    # Get the coordinates of each tile
    def get_coordinates(self):
        coord_list = []

        for x in range(0, int(self.display_height / 32)):
            for y in range(0, int(self.display_width / 32)):
                coord_list.append((y*32, x*32))
        return coord_list

    # Starting a new game
    def new(self):
        self.coordinates = self.get_coordinates()
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()

        self.current_tileset = tileset_grass
        self.tileset_name = "tileset_grass"
        self.current_tile = 0

        self.output_level = []

        # Appending the amount of rows to output_level
        for x in range(int(self.display_height / 32)):
            self.output_level.append([])

            for y in range(int(self.display_width / 32)):
                self.output_level[x].append(0)

        self.background_details = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.details = pygame.sprite.Group()
        self.current_layer = "walls"

        self.run()

    # Game loop
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(self.FPS)
            self.events()
            self.update()
            self.draw()

    # Game loop - Events
    def events(self):
        # --- KEYBOARD AND QUIT EVENTS ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

            if event.type == pygame.KEYDOWN:
                # Clear the map if escape is pressed
                if event.key == pygame.K_ESCAPE:
                    self.walls.empty()

                # Tile switching
                if event.key == pygame.K_UP:
                    if self.current_tile < 12:
                        self.current_tile += 1

                if event.key == pygame.K_DOWN:
                    if self.current_tile > 0:
                        self.current_tile -= 1

                # Layer switching
                if event.key == pygame.K_1:
                    self.current_layer = "walls"
                if event.key == pygame.K_2:
                    self.current_layer = "details"
                if event.key == pygame.K_3:
                    self.current_layer = "background_details"

                # Tileset switching
                if event.key == pygame.K_F1:
                    self.current_tileset = tileset_grass
                    self.tileset_name = "tileset_grass"
                if event.key == pygame.K_F2:
                    self.current_tileset = tileset_details
                    self.tileset_name = "tileset_details"
                if event.key == pygame.K_F3:
                    self.current_tileset = tileset_oak_trees
                    self.tileset_name = "tileset_oak_trees"

                # Printing the level
                if event.key == pygame.K_RETURN:
                    # Layer 1 printing
                    for coords in self.coordinates:
                        for w in self.walls:
                            if w.rect.x == coords[0] and w.rect.y == coords[1]:
                                self.output_level[int(coords[1]/32)][int(coords[0]/32)] = w.id

                    print("WALLS:")
                    for level in self.output_level:
                        print("{},".format(level))

                    # Resetting output_level
                    self.output_level = []

                    # Appending the amount of rows to output_level
                    for x in range(int(self.display_height / 32)):
                        self.output_level.append([])

                        for y in range(int(self.display_width / 32)):
                            self.output_level[x].append(0)

                    # Layer 2 Printing
                    for coords in self.coordinates:
                        for w in self.details:
                            if w.rect.x == coords[0] and w.rect.y == coords[1]:
                                self.output_level[int(coords[1]/32)][int(coords[0]/32)] = w.id

                    print("DETAILS:")
                    for level in self.output_level:
                        print("{},".format(level))

                    # Resetting output_level
                    self.output_level = []

                    # Appending the amount of rows to output_level
                    for x in range(int(self.display_height / 32)):
                        self.output_level.append([])

                        for y in range(int(self.display_width / 32)):
                            self.output_level[x].append(0)

                    # Layer 3 Printing
                    for coords in self.coordinates:
                        for w in self.background_details:
                            if w.rect.x == coords[0] and w.rect.y == coords[1]:
                                self.output_level[int(coords[1]/32)][int(coords[0]/32)] = w.id

                    print("BG-DETAILS:")
                    for level in self.output_level:
                        print("{},".format(level))



        # --- MOUSE EVENTS ---
        # Tile placement
        if self.click[0]:
            for x in self.coordinates:
                if x[0] < self.mouse_x < x[0] + 32:
                    if x[1] < self.mouse_y < x[1] + 32:
                        # Erasing any previous tiles at this location

                        if self.current_layer == "walls":
                            for w in self.walls:
                                if w.rect.x == x[0] and w.rect.y == x[1]:
                                    self.walls.remove(w)
                                    break
                        elif self.current_layer == "details":
                            for w in self.details:
                                if w.rect.x == x[0] and w.rect.y == x[1]:
                                    self.details.remove(w)
                                    break
                        elif self.current_layer == "background_details":
                            for w in self.background_details:
                                if w.rect.x == x[0] and w.rect.y == x[1]:
                                    self.background_details.remove(w)
                                    break

                        w = Wall(x[0], x[1], image=self.current_tileset.all_tiles[self.current_tile]["image"], id=self.current_tileset.all_tiles[self.current_tile]["id"])

                        if self.current_layer == "walls":
                            self.walls.add(w)
                        elif self.current_layer == "details":
                            self.details.add(w)
                        elif self.current_layer == "background_details":
                            self.background_details.add(w)

                        break

        # Tile erasing
        if self.click[2]:
            for x in self.coordinates:
                if x[0] < self.mouse_x < x[0]+32:
                    if x[1] < self.mouse_y < x[1]+32:
                        if self.current_layer == "walls":
                            for w in self.walls:
                                if w.rect.x == x[0] and w.rect.y == x[1]:
                                    self.walls.remove(w)
                                    break
                        elif self.current_layer == "details":
                            for w in self.details:
                                if w.rect.x == x[0] and w.rect.y == x[1]:
                                    self.details.remove(w)
                                    break
                        elif self.current_layer == "background_details":
                            for w in self.background_details:
                                if w.rect.x == x[0] and w.rect.y == x[1]:
                                    self.background_details.remove(w)
                                    break

    # Game loop - Update
    def update(self):
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()

    # Game loop - Rendering/Drawing
    def draw(self):
        self.game_display.fill(black)
        self.level_surface.fill(white)

        self.background_details.draw(self.level_surface)
        self.walls.draw(self.level_surface)
        self.details.draw(self.level_surface)

        self.game_display.blit(self.level_surface, (0, 0))

        self.render_text("layer: {}".format(self.current_layer), white, size="small", y_displace=375, x_displace= -(self.display_width / 2 - 10))
        self.render_text("tileset: {}".format(self.tileset_name), white, size="small", y_displace=395, x_displace= -(self.display_width / 2 - 10))

        self.game_display.blit(self.current_tileset.all_tiles[self.current_tile]["image"], (10, self.display_height + 10))

        pygame.display.update()

# Creating the game window
e = Editor()

while e.running:
    e.new()

pygame.quit()
quit()
