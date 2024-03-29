import pygame as pg

vec2 = pg.math.Vector2

RES = WIDTH, HEIGHT = vec2(1280, 720)
CENTER = H_WIDTH, H_HEIGHT = RES // 2
TILE_SIZE = 250

PLAYER_SPEED = 0.4
PLAYER_ROT_SPEED = 0.0015

BG_COLOR = 'olivedrab'
NUM_ANGLES = 180 # multiply of 360 -> 24, 30, 36, 40, 45, 60, 72, 90, 12, 180

# entity sprite settings
ENTITY_SPRITE_ATTRS = {
    'player': {
        'path': 'assets/entities/player/player.png',
        'num_layers': 7,
        'scale': 0.30,
        'y_offset': 0,
    },
    'kitty': {
        'path': 'assets/entities/cats/kitty.png',
        'num_layers': 8,
        'scale': 0.6,
        'y_offset': -20,
    },
}

# stacked sprites settings
STACKED_SPRITE_ATTRS = {
    'grass': {
        'path': 'assets/stacked_sprites/StackedSprite/grass.png',
        'num_layers': 11,
        'scale': 7,
        'y_offset': -40,
        'outline': False,
    },
    'blue_tree': {
        'path': 'assets/stacked_sprites/StackedSprite/blue_tree.png',
        'num_layers': 43,
        'scale': 8,
        'y_offset': -170,
    },
    'car': {
        'path': 'assets/stacked_sprites/StackedSprite/car.png',
        'num_layers': 9,
        'scale': 10,
        'y_offset': -10,
    },
    'van': {
        'path': 'assets/stacked_sprites/StackedSprite/van.png',
        'num_layers': 20,
        'scale': 6,
        'y_offset': -30,
    },
    'tank': {
        'path': 'assets/stacked_sprites/StackedSprite/tank.png',
        'num_layers': 17,
        'scale': 8,
        'y_offset': -40,
    },
}