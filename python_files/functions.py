from typing import Dict, Set, Tuple, Optional

import pygame

import constants
import classes


def load_background_music():
    mixer = pygame.mixer
    mixer.init()
    mixer.music.load(constants.BACKGROUND_MUSIC_1)
    mixer.music.play()


def check_if_target_has_collision(target_x: int, target_y: int, obstacles: Tuple[classes.Block]) -> Tuple[bool, Optional[classes.Block]]:
    '''
    Returns True and collisiong block if player has any collision with an obstacle, otherwise True

    Args:
        target_x (int): x coordinate of a target
        target_y (int) y coordinate of a target
        obstacles (tuple(Block)): all obstacle classes

    Returns:
        tuple(bool, None|Block): if player has any collision or not and obstacle class
    '''
    for obstacle_class in obstacles:
        for obstacle_x, obstacle_y in obstacle_class.objects_coordinates:
            if (target_x, target_y) == (obstacle_x, obstacle_y):
                return (True, obstacle_class)

    return False, None


def show_obstacles(screen, obstacles: Tuple[classes.Block]) -> None:
    '''
    Sets obstacles on the screen

    Args:
        screen: game window
        obstacles (tuple(Block)): a tuple of obstacle classes
    
    Returns:
        None
    '''
    for obstacle in obstacles:
        for obstacle_x, obstacle_y in obstacle.objects_coordinates:
            screen.blit(obstacle.image, (obstacle_x * 50, obstacle_y * 50))
            

# BLOCKS MOVEMENTS

def move_block_up(block_x: int, block_y: int, obstacle: classes.Block, all_obstacles: Tuple[classes.Block]) -> bool:
    '''
    Moves block up if it can

    Args:
        block_x (int): x coordinate of a block
        block_y (int): x coordinate of a block
        obstacle (Block): obstacle
        all_obstacles (tuple(Block)): all obstacle classes

    Returns:
        bool: True if was moved
    '''
    if 0 < block_y:
        has_collision, _ = check_if_target_has_collision(block_x, block_y - 1, all_obstacles)
        if not has_collision:
            obstacle.move_block(block_x, block_y, up=True)
            return True
    return False


def move_block_right(block_x: int, block_y: int, obstacle: classes.Block, all_obstacles: Tuple[classes.Block]) -> bool:
    '''
    Moves block right if it can

    Args:
        block_x (int): x coordinate of a block
        block_y (int): x coordinate of a block
        obstacle (Block): obstacle
        all_obstacles (tuple(Block)): all obstacle classes

    Returns:
        bool: True if was moved
    '''
    if block_x < constants.WINDOW_WIDTH // 50 - 1:
        has_collision, _ = check_if_target_has_collision(block_x + 1, block_y, all_obstacles)
        if not has_collision:
            obstacle.move_block(block_x, block_y, right=True)
            return True
    return False


def move_block_down(block_x: int, block_y: int, obstacle: classes.Block, all_obstacles: Tuple[classes.Block]) -> bool:
    '''
    Moves block down if it can

    Args:
        block_x (int): x coordinate of a block
        block_y (int): x coordinate of a block
        obstacle (Block): obstacle
        all_obstacles (tuple(Block)): all obstacle classes

    Returns:
        bool: True if was moved
    '''
    if block_y < constants.WINDOW_HEIGHT // 50 - 1:
        has_collision, _ = check_if_target_has_collision(block_x, block_y + 1, all_obstacles)
        if not has_collision:
            obstacle.move_block(block_x, block_y, down=True)
            return True
    return False


def move_block_left(block_x: int, block_y: int, obstacle: classes.Block, all_obstacles: Tuple[classes.Block]) -> bool:
    '''
    Moves block left if it can

    Args:
        block_x (int): x coordinate of a block
        block_y (int): x coordinate of a block
        obstacle (Block): obstacle
        all_obstacles (tuple(Block)): all obstacle classes

    Returns:
        bool: True if was moved
    '''
    if 0 < block_x:
        has_collision, _ = check_if_target_has_collision(block_x - 1, block_y, all_obstacles)
        if not has_collision:
            obstacle.move_block(block_x, block_y, left=True)
            return True
    return False


# PLAYER MOVEMENTS

def move_player_up(player: classes.Character, all_obstacles: Tuple[classes.Block]) -> bool:
    '''
    Moves player up if it can

    Args:
        player (Character): player class
        all_obstacles (tuple(Block)): all obstacle classes

    Returns:
        bool: True if was moved
    '''
    if 0 < player.y:
        has_collision, obstacle = check_if_target_has_collision(player.x, player.y - 1, all_obstacles)
        if has_collision:
            if obstacle.is_movable:
                if move_block_up(player.x, player.y - 1, obstacle, all_obstacles):
                    player.move_character(player.x, player.y, up=True)
                    return True
        else:
            player.move_character(player.x, player.y, up=True)
            return True
    return False


def move_player_right(player: classes.Character, all_obstacles: Tuple[classes.Block]) -> bool:
    '''
    Moves player right if it can

    Args:
        player (Character): player class
        all_obstacles (tuple(Block)): all obstacle classes

    Returns:
        bool: True if was moved
    '''
    if player.x < constants.WINDOW_WIDTH // 50 - 1:
        has_collision, obstacle = check_if_target_has_collision(player.x + 1, player.y, all_obstacles)
        if has_collision:
            if obstacle.is_movable:
                if move_block_right(player.x + 1, player.y, obstacle, all_obstacles):
                    player.move_character(player.x, player.y, right=True)
                    return True
        else:
            player.move_character(player.x, player.y, right=True)
            return True
    return False


def move_player_down(player: classes.Character, all_obstacles: Tuple[classes.Block]) -> bool:
    '''
    Moves player down if it can

    Args:
        player (Character): player class
        all_obstacles (tuple(Block)): all obstacle classes

    Returns:
        bool: True if was moved
    '''
    if player.y < constants.WINDOW_HEIGHT // 50 - 1:
        has_collision, obstacle = check_if_target_has_collision(player.x, player.y + 1, all_obstacles)
        if has_collision:
            if obstacle.is_movable:
                if move_block_down(player.x, player.y + 1, obstacle, all_obstacles):
                    player.move_character(player.x, player.y, down=True)
                    return True
        else:
            player.move_character(player.x, player.y, down=True)
            return True
    return False


def move_player_left(player: classes.Character, all_obstacles: Tuple[classes.Block]) -> bool:
    '''
    Moves player up if it can

    Args:
        player (Character): player class
        all_obstacles (tuple(Block)): all obstacle classes

    Returns:
        bool: True if was moved
    '''
    if 0 < player.x:
        has_collision, obstacle = check_if_target_has_collision(player.x - 1, player.y, all_obstacles)
        if has_collision:
            if obstacle.is_movable:
                if move_block_left(player.x - 1, player.y, obstacle, all_obstacles):
                    player.move_character(player.x, player.y, left=True)
                    return True
        else:
            player.move_character(player.x, player.y, left=True)
            return True
    return False