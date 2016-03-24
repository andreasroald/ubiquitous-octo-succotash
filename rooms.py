import pygame
from sprites import *
from levels import *

class Room:
    def __init__(self):
        pass

    def init_npcs(self):
        pass

class Room_1(Room):
    # Initialize the room 1 class
    def __init__(self):
        self.level = level_1
        self.npc_list = pygame.sprite.Group()

        self.north_room_index = 1
        self.collide_list = None
        self.player = None

    def init_npcs(self):
        # Room 1 NPCs
        self.name = NPC([
                         [(62, 62), True], [(262, 62), False],
                         [(262, 182), False], [(62, 182), False]
                        ], npc_face_1, {"p1": {"l1": "this is my first",
                                                     "l2": "page.",
                                                     "l3": ""
                                              },
                                        "p2": {"l1": "this is my second",
                                                     "l2": "page.",
                                                     "l3": ""
                                              }
                                        }
                        , self.collide_list, self.player)

        self.npc_list.add(self.name)

class Room_2(Room):
    # Initialize the room 1 class
    def __init__(self):
        self.level = level_2
        self.npc_list = pygame.sprite.Group()

        self.south_room_index = 0
        self.collide_list = None
        self.player = None

    def init_npcs(self):
        # Room 2 NPCs
        self.name = NPC([
                         [(62, 62), True], [(702, 62), False],
                         [(702, 462), False], [(62, 462), False]
                        ], npc_face_1, {"p1": {"l1": "this is my first",
                                                     "l2": "page.",
                                                     "l3": ""
                                              },
                                        "p2": {"l1": "this is my second",
                                                     "l2": "page.",
                                                     "l3": ""
                                              }
                                        }
                        , self.collide_list, self.player)

        self.name2 = NPC([
                         [(702, 462), True], [(62, 462), False],
                         [(62, 62), False], [(702, 62), False]
                        ], npc_face_1, {"p1": {"l1": "this is my first",
                                                     "l2": "page.",
                                                     "l3": ""
                                              },
                                        "p2": {"l1": "this is my second",
                                                     "l2": "page.",
                                                     "l3": ""
                                              }
                                        }
                        , self.collide_list, self.player)

        self.npc_list.add(self.name, self.name2)

room_1 = Room_1()
room_2 = Room_2()

room_list = [room_1, room_2]
