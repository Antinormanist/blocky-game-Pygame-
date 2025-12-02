import random

import pygame

import classes

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

BACKGROUND_RGB = (141, 201, 115)

BACKGROUND_MUSIC_1 = '.\\soundtracks\\undertale_core.mp3'

SETTINGS_IMAGE = '.\\images\\settings.jpg'
PLAYER_IMAGE = '.\\images\\cube.jpg'
ARCHER_IMAGE = '.\\images\\archer.jpg'
ROCK_IMAGE = '.\\images\\rock.jpg'
BOX_IMAGE = '.\\images\\box.jpg'

SETTINGS = pygame.image.load(SETTINGS_IMAGE)

REGIONS = {1: {}}

# get zones obstacle
ZONES_DIRECTIONS = {
    1: [None, 2, 3, None],
    2: [None, None, 4, 1],
    3: [1, 4, None, None],
    4: [2, None, None, 3]
}

# get zones directions

ZONES_OBSTACLES = {
    1: [classes.Archer(ARCHER_IMAGE, 50, 8, 8, random.randint(3, 6)), classes.Box('box', True, BOX_IMAGE, {(1, 1), (5, 3), (8, 12)}), classes.Rock('rock', False, ROCK_IMAGE, {(1, 2), (7, 0), (9, 9), (16, 0), (0, 12), (6, 2)})], 
    2: [classes.Rock('rock', False, ROCK_IMAGE, 
                     {(x, 0) for x in range(1, 16)} | 
                     {(x, 14) for x in range(1, 16)} | 
                     {(15, y) for y in range(15)} | 
                     {(x, y) for x in range(1, 14, 4) for y in range(1, 13)} | 
                     {(x, y) for x in range(3, 12, 4) for y in range(2, 14)})], 
    3: [classes.Box('box', True, BOX_IMAGE, {(x, y) for x in range(1, 15, 2) for y in range(1, 16, 2)})], 
    4: []
}