import pygame
from sprites import *
from levels import *

class Room_1:
    # Initialize the room 1 class
    def __init__(self):
        self.level = level_1
        self.npc_list = pygame.sprite.Group()

        self.north_room_index = 1

        # Room 1 NPCs
        self.name = NPC(375, 375, npc_face_1, {"p1": {"l1": "this is my first",
                                                     "l2": "page.",
                                                     "l3": ""},
                                              "p2": {"l1": "this is my second",
                                                     "l2": "page.",
                                                     "l3": ""}
                                             })

        self.npc_list.add(self.name)

class Room_2:
    # Initialize the room 1 class
    def __init__(self):
        self.level = level_2
        self.npc_list = pygame.sprite.Group()

        self.south_room_index = 0


room_1 = Room_1()
room_2 = Room_2()

room_list = [room_1, room_2]
