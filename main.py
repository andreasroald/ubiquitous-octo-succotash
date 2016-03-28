import random
import math

import pygame

import levels
from rooms import *
from sprites import *
from resources import *
from settings import *

# Create game class
class Game:
    # Initialize the game class
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 1, 512)
        pygame.init()

        self.game_display = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.running = True

        # Hide windows mouse pointer
        pygame.mouse.set_visible(0)

        # Sounds
        self.footstep_1 = pygame.mixer.Sound('sounds/footstep_1.wav')
        self.footstep_2 = pygame.mixer.Sound('sounds/footstep_2.wav')

        # Converting sprite alpha levels
        for x in resource_lists:
            for y in x:
                y.convert_alpha()


    # Functions that create the different layers
    def create_layer_1(self, level):
        levels.level_x = 0
        levels.level_y = 0
        for rows in level:
            for cols in rows:
                if cols == 1:
                    w = Wall(levels.level_x, levels.level_y, 128, 128, image=grass_1)
                    self.layer_1.add(w)
                if cols == 2:
                    w = Wall(levels.level_x, levels.level_y, 128, 128, image=grass_2)
                    self.layer_1.add(w)
                if cols == 3:
                    w = Wall(levels.level_x, levels.level_y, 128, 128, image=planks_1)
                    self.layer_1.add(w)
                if cols == 4:
                    w = Wall(levels.level_x, levels.level_y, 128, 128, image=red_sand_1)
                    self.layer_1.add(w)
                if cols == 5:
                    w = Wall(levels.level_x, levels.level_y, 128, 128, image=red_sand_2)
                    self.layer_1.add(w)
                if cols == 6:
                    w = Wall(levels.level_x, levels.level_y, 128, 128, image=metal_floor_1)
                    self.layer_1.add(w)

                levels.level_x += 40
            levels.level_x = 0
            levels.level_y += 40

    def create_layer_2(self, level):
        levels.level_x = 0
        levels.level_y = 0
        for rows in level:
            for cols in rows:
                if cols == -1:
                    w = Wall(levels.level_x, levels.level_y, 40, 40, image=void)
                    self.layer_2.add(w)
                if cols == 1:
                    w = Wall(levels.level_x, levels.level_y, 40, 40, image=rock_wall_1)
                    self.layer_2.add(w)
                if cols == 2:
                    w = Wall(levels.level_x, levels.level_y, 160, 80, image=desk_1)
                    self.layer_2.add(w)
                if cols == 3:
                    w = Wall(levels.level_x, levels.level_y, 40, 40, image=office_chair_bottom)
                    self.layer_2.add(w)
                if cols == 4:
                    w = Wall(levels.level_x, levels.level_y, 40, 40, image=flower_pot)
                    self.layer_2.add(w)
                if cols == 5:
                    w = Wall(levels.level_x, levels.level_y, 80, 120, image=bed)
                    self.layer_2.add(w)

                levels.level_x += 40
            levels.level_x = 0
            levels.level_y += 40

    def create_layer_3(self, level):
        levels.level_x = 0
        levels.level_y = 0
        for rows in level:
            for cols in rows:
                if cols == 1:
                    w = Wall(levels.level_x, levels.level_y, 160, 160, image=tree_1)
                    self.layer_3.add(w)

                if cols == 2:
                    w = Wall(levels.level_x, levels.level_y, 40, 40, image=metal_wall_top)
                    self.layer_3.add(w)
                if cols == 3:
                    w = Wall(levels.level_x, levels.level_y, 40, 40, image=metal_wall_left)
                    self.layer_3.add(w)
                if cols == 4:
                    w = Wall(levels.level_x, levels.level_y, 40, 40, image=metal_wall_bottom)
                    self.layer_3.add(w)
                if cols == 5:
                    w = Wall(levels.level_x, levels.level_y, 40, 40, image=metal_wall_right)
                    self.layer_3.add(w)

                if cols == 6:
                    w = Wall(levels.level_x, levels.level_y, 40, 40, image=metal_wall_tlcorner)
                    self.layer_3.add(w)
                if cols == 7:
                    w = Wall(levels.level_x, levels.level_y, 40, 40, image=metal_wall_trcorner)
                    self.layer_3.add(w)
                if cols == 8:
                    w = Wall(levels.level_x, levels.level_y, 40, 40, image=metal_wall_blcorner)
                    self.layer_3.add(w)
                if cols == 9:
                    w = Wall(levels.level_x, levels.level_y, 40, 40, image=metal_wall_brcorner)
                    self.layer_3.add(w)

                if cols == 10:
                    w = Wall(levels.level_x, levels.level_y, 40, 40, image=metal_wall_90deg_lt)
                    self.layer_3.add(w)
                if cols == 11:
                    w = Wall(levels.level_x, levels.level_y, 40, 40, image=metal_wall_90deg_tr)
                    self.layer_3.add(w)
                if cols == 12:
                    w = Wall(levels.level_x, levels.level_y, 40, 40, image=metal_wall_90deg_lb)
                    self.layer_3.add(w)
                if cols == 13:
                    w = Wall(levels.level_x, levels.level_y, 40, 40, image=metal_wall_90deg_br)
                    self.layer_3.add(w)

                if cols == 14:
                    w = Wall(levels.level_x, levels.level_y, 40, 40, image=office_chair_top)
                    self.layer_3.add(w)
                if cols == 15:
                    w = Wall(levels.level_x, levels.level_y, 40, 40, image=plant_1)
                    self.layer_3.add(w)

                levels.level_x += 40
            levels.level_x = 0
            levels.level_y += 40

    # Function that runs when a new room is entered
    def new_room(self):
        # empty all the layers
        self.layer_1.empty()
        self.layer_2.empty()
        self.layer_3.empty()

        # create the new layers
        self.create_layer_1(self.current_room.level[0])
        self.create_layer_2(self.current_room.level[1])
        self.create_layer_3(self.current_room.level[2])

        # reset the room variables and initialize NPCS
        self.current_room.collide_list = self.layer_2
        self.current_room.npc_list.empty()
        if not self.current_room.cleared:
            self.current_room.init_npcs()

    # Starting a new game
    def new(self):

        # create the layer group
        self.layer_1 = pygame.sprite.Group()
        self.layer_2 = pygame.sprite.Group()
        self.layer_3 = pygame.sprite.Group()

        # starting room
        self.current_room = room_1

        # creating the player object
        self.player = Player(self.layer_2, self.current_room.npc_list, self.game_display)

        # resetting the room
        self.current_room.collide_list = self.layer_2
        self.current_room.player = self.player
        self.current_room.npc_list.empty()

        # making enemies re-spawn if their room was previously cleared
        for reset_enemies in room_list:
            reset_enemies.cleared = False

        # create the NPCs of the current room
        self.current_room.init_npcs()

        # text boxes
        self.text_boxes = pygame.sprite.Group()
        self.text_page = 1

        # creating the custom mouse pointer
        self.pointer = Pointer()

        # footstep sound variables
        self.footsteps = [self.footstep_1, self.footstep_2]
        self.prev_footstep = pygame.time.get_ticks()
        self.current_time = pygame.time.get_ticks()
        self.footstep_index = 0

        # player detection variables
        self.player_seen = False
        self.seen_by = -1
        self.not_cleared_warning = False

        # creating the layers of the room
        self.new_room()

        # starting the game loop
        self.run()

    # Game loop
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    # Game loop - Events
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.player.in_conversation:
                        if self.text_page < len(self.player.talking_with.lines):
                            self.text_page += 1
                        else:
                            self.player.in_conversation = False
                            self.player.talking_with = None
                            self.text_page = 1
                    else:
                        self.player.test_for_npc()

                if event.key == pygame.K_SPACE:
                    for kill_npcs in self.current_room.npc_list:
                        if kill_npcs.kill_zone.colliderect(self.player.rect) and not self.player_seen:
                            kill_npcs.die()
                            self.player.killing_npc = True

                if event.key == pygame.K_r:
                    self.playing = False

    # Game loop - Update
    def update(self):
        # update player, npc and time
        self.current_room.npc_list.update()
        self.player.update()
        self.current_time = pygame.time.get_ticks()
        self.not_cleared_warning = False

        # Reposition mouse pointer
        self.pointer.update()

        # Make player switch room
        if self.player.rect.center[1] < 0:
            if self.current_room.cleared:
                self.current_room = room_list[self.current_room.north_room_index]
                self.current_room.player = self.player
                self.new_room()
                self.player.rect.y = display_height - (self.player.rect[3] / 2)
                self.player.npc_list = self.current_room.npc_list
            else:
                self.player.rect.y += 5
                self.not_cleared_warning = True

        if self.player.rect.center[1] > display_height:
            if self.current_room.cleared:
                self.current_room = room_list[self.current_room.south_room_index]
                self.current_room.player = self.player
                self.new_room()
                self.player.rect.y = 0 - (self.player.rect[3] / 2)
                self.player.npc_list = self.current_room.npc_list
            else:
                self.player.rect.y -= 5
                self.not_cleared_warning = True

        # Make footstep sounds
        if self.player.moving_up or self.player.moving_left or self.player.moving_down or self.player.moving_right:
            if not self.player.in_conversation and not self.player.killing_npc:
                if self.current_time - self.prev_footstep > 500:
                    self.prev_footstep = pygame.time.get_ticks()
                    self.player.sound_level = 40
                    pygame.mixer.Sound.play(self.footstep_1)

        for resize_hear_zone in self.current_room.npc_list:
            resize_hear_zone.hear_zone.width = self.player.sound_level * 10
            resize_hear_zone.hear_zone.height = self.player.sound_level * 10

        # Check if the player actually is in the enemies line of sight
        for npc_vision in self.current_room.npc_list:
            if npc_vision.see_zone.colliderect(self.player.rect):
                if npc_vision.rect.x < self.player.rect.x and npc_vision.rect.y < self.player.rect.y:
                    npc_vision.player_npc_rect.width = abs(self.player.rect.x - npc_vision.rect.x)
                    npc_vision.player_npc_rect.height = abs(self.player.rect.y - npc_vision.rect.y)
                    npc_vision.player_npc_rect.x = npc_vision.rect.center[0]
                    npc_vision.player_npc_rect.y = npc_vision.rect.center[1]
                elif npc_vision.rect.x < self.player.rect.x and npc_vision.rect.y > self.player.rect.y:
                    npc_vision.player_npc_rect.width = abs(self.player.rect.x - npc_vision.rect.x)
                    npc_vision.player_npc_rect.height = abs(self.player.rect.y - npc_vision.rect.y)
                    npc_vision.player_npc_rect.x = npc_vision.rect.center[0]
                    npc_vision.player_npc_rect.y = self.player.rect.center[1]
                elif npc_vision.rect.x > self.player.rect.x and npc_vision.rect.y < self.player.rect.y:
                    npc_vision.player_npc_rect.width = abs(self.player.rect.x - npc_vision.rect.x)
                    npc_vision.player_npc_rect.height = abs(self.player.rect.y - npc_vision.rect.y)
                    npc_vision.player_npc_rect.x = self.player.rect.center[0]
                    npc_vision.player_npc_rect.y = npc_vision.rect.center[1]
                elif npc_vision.rect.x > self.player.rect.x and npc_vision.rect.y > self.player.rect.y:
                    npc_vision.player_npc_rect.width = abs(self.player.rect.x - npc_vision.rect.x)
                    npc_vision.player_npc_rect.height = abs(self.player.rect.y - npc_vision.rect.y)
                    npc_vision.player_npc_rect.x = self.player.rect.center[0]
                    npc_vision.player_npc_rect.y = self.player.rect.center[1]

                if npc_vision.player_npc_rect.height <= 0 or npc_vision.player_npc_rect.width <= 0:
                    npc_vision.player_npc_rect.height = 1
                    npc_vision.player_npc_rect.width = 1

                for solid_tiles in self.layer_2:
                    if npc_vision.player_npc_rect.colliderect(solid_tiles.rect):
                        self.player_seen = False
                        npc_vision.seeing_player = False
                        break
                else:
                    self.player_seen = True
                    self.seen_by = npc_vision.id
                    npc_vision.player_pos = self.player.rect.center
                    npc_vision.seeing_player = True

            else:
                if self.seen_by == npc_vision.id:
                    npc_vision.player_npc_rect.width = 0
                    npc_vision.player_npc_rect.height = 0
                    npc_vision.player_npc_rect.x = -1
                    npc_vision.player_npc_rect.y = -1
                    self.player_seen = False
                    npc_vision.seeing_player = False

        # Make dying NPCS die (mwhahahah)
        for kill_npcs in self.current_room.npc_list:
            if kill_npcs.dying:
                kill_npcs.die()
            if kill_npcs.dead:
                self.current_room.npc_list.remove(kill_npcs)
                self.player.killing_npc = False

        # Check if room is empty
        if not self.current_room.npc_list.sprites():
            self.current_room.cleared = True

    # Game loop - Rendering/Drawing
    def draw(self):

        # draw layer 1 and layer 2
        self.layer_1.draw(self.game_display)
        self.layer_2.draw(self.game_display)

        # draw all NPCs
        for draw_npcs in self.current_room.npc_list:
            draw_npcs.draw(self.game_display)

        # draw the player
        self.player.draw(self.game_display)

        # draw layer 3
        self.layer_3.draw(self.game_display)

        # draw scanlines overlay, show warning message if player is detected
        if self.player_seen:
            self.game_display.blit(scanlines_seen, (0, 0))
            render_text_center("DETECTED", red, self.game_display, y=225, size="large")
        else:
            self.game_display.blit(scanlines, (0, 0))

        # notify the player if the room needs to be cleared
        if self.not_cleared_warning:
            render_text_center("CLEAR THE ROOM TO PROCEED", white, self.game_display, y=225, size="medium")

        # notify the player when the room is cleared
        if self.current_room.cleared:
            render_text_center("ROOM CLEARED", white, self.game_display, y=225, size="large")

        # draw text-boxes
        if self.player.in_conversation:
            self.text_boxes.empty()
            self.talk_box = Text_Box(self.player.talking_with.face, self.player.talking_with.lines, self.text_page)
            self.text_boxes.add(self.talk_box)
            self.text_boxes.draw(self.game_display)

        # draw the mouse pointer
        self.pointer.draw(self.game_display)

        # update the display
        pygame.display.update()
        pygame.display.set_caption(title + " running at " + str(int(self.clock.get_fps())) + " frames per second")

game = Game()

while game.running:
    game.new()

pygame.quit()
quit()
