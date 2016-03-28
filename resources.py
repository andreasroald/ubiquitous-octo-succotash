import pygame

# Player images
player_standing = pygame.image.load("sprites/player/player_standing.png")
player_killing = pygame.image.load("sprites/player/player_killing_1.png")

player_list = [player_standing]
for load_player_walk in range(12):
    player_list.append(pygame.image.load("sprites/player/player_walk_{}.png".format(load_player_walk+1)))

# Enemy images
enemy_dying_list = []
for load_enemy_dying in range(19):
    enemy_dying_list.append(pygame.image.load("sprites/player/enemy_dying_{}.png".format(load_enemy_dying+1)))


# Layer 1 images
grass_1 = pygame.image.load("sprites/layer 1/grass_1.png")
grass_2 = pygame.image.load("sprites/layer 1/grass_2.png")
planks_1 = pygame.image.load("sprites/layer 1/planks_1.png")
red_sand_1 = pygame.image.load("sprites/layer 1/red_sand_1.png")
red_sand_2 = pygame.image.load("sprites/layer 1/red_sand_2.png")
metal_floor_1 = pygame.image.load("sprites/layer 1/metal_floor_1.png")
layer_1_list = [grass_1, grass_2, planks_1, red_sand_1, red_sand_2, metal_floor_1]

# Layer 2 images
void = pygame.Surface((40, 40))
void.fill((0, 0, 0))
rock_wall_1 = pygame.image.load("sprites/layer 2/rock_wall_1.png")
desk_1 = pygame.image.load("sprites/layer 2/desk_1.png")
office_chair_bottom = pygame.image.load("sprites/layer 2/office_chair_bottom.png")
flower_pot = pygame.image.load("sprites/layer 2/flower_pot.png")
bed = pygame.image.load("sprites/layer 2/bed.png")
layer_2_list = [void, rock_wall_1, desk_1, office_chair_bottom, flower_pot]

# Layer 3 images
tree_1 = pygame.image.load("sprites/layer 3/tree_1.png")

metal_wall_top = pygame.image.load("sprites/layer 3/metal_wall_top.png")
metal_wall_left = pygame.image.load("sprites/layer 3/metal_wall_left.png")
metal_wall_bottom = pygame.image.load("sprites/layer 3/metal_wall_bottom.png")
metal_wall_right = pygame.image.load("sprites/layer 3/metal_wall_right.png")

metal_wall_tlcorner = pygame.image.load("sprites/layer 3/metal_wall_tlcorner.png")
metal_wall_trcorner = pygame.image.load("sprites/layer 3/metal_wall_trcorner.png")
metal_wall_blcorner = pygame.image.load("sprites/layer 3/metal_wall_blcorner.png")
metal_wall_brcorner = pygame.image.load("sprites/layer 3/metal_wall_brcorner.png")

metal_wall_90deg_lt = pygame.image.load("sprites/layer 3/metal_wall_90deg_lt.png")
metal_wall_90deg_tr = pygame.image.load("sprites/layer 3/metal_wall_90deg_tr.png")
metal_wall_90deg_lb = pygame.image.load("sprites/layer 3/metal_wall_90deg_lb.png")
metal_wall_90deg_br = pygame.image.load("sprites/layer 3/metal_wall_90deg_br.png")

office_chair_top = pygame.image.load("sprites/layer 3/office_chair_top.png")
plant_1 = pygame.image.load("sprites/layer 3/plant_1.png")

door = pygame.Surface((40, 40))

layer_3_list = [tree_1, desk_1, metal_wall_top, metal_wall_left, metal_wall_bottom, metal_wall_right,
                metal_wall_tlcorner, metal_wall_trcorner, metal_wall_blcorner, metal_wall_brcorner,
                metal_wall_90deg_lt, metal_wall_90deg_tr, metal_wall_90deg_lb, metal_wall_90deg_br,
                office_chair_top, plant_1]

# GUI and misc
eye = pygame.image.load("sprites/gui/eye.png")
pointer = pygame.image.load("sprites/gui/pointer.png")
pointer_eye = pygame.image.load("sprites/gui/pointer_eye.png")
scanlines = pygame.image.load("sprites/scanlines.png")
scanlines_seen = pygame.image.load("sprites/scanlines_seen.png")

# Face images
npc_face_1 = pygame.image.load("sprites/faces/npc_face_1.png")
face_list = [npc_face_1]

resource_lists = [player_list, layer_1_list, layer_2_list, layer_3_list, face_list]
