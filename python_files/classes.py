from typing import Tuple, Set

import pygame

import constants


class Character:
    def __init__(self, image: str, health_points: int, x: int, y: int) -> None:
        self.image = pygame.image.load(image)
        self.health_points = health_points
        self.x = x
        self.y = y


    def set_coordinates(self, x: int, y: int) -> None:
        '''
        Sets new coordinates of a character

        Args:
            x (int): x coordinate
            y (int): y coordinate

        Returns:
            None
        '''
        self.x = x
        self.y = y


    def move_character(self, current_x: int, current_y: int, up: bool = False, right: bool = False, down: bool = False, left: bool = False) -> None:
        '''
        Moves character to new coordinates

        Args:
            current_x (int): current x coordinate
            current_t (int): current y coordinate
            up (bool): movement direction. Default value is False
            right (bool): movement direction. Default value is False
            down (bool): movement direction. Default value is False
            left (bool): movement direction. Default value is False

        Returns:
            None
        '''
        if up:
            self.y -= 1
        elif right:
            self.x += 1
        elif down:
            self.y += 1
        else:
            self.x -= 1


class Block:
    def __init__(self, block_type: str, is_movable: bool, image: str, objects_coordinates: Set[Tuple[int, int]]) -> None:
        self.block_type = block_type
        self.is_movable = is_movable
        self.image = pygame.image.load(image)
        self.objects_coordinates = objects_coordinates


    def move_block(self, current_x: int, current_y: int, up: bool = False, right: bool = False, down: bool = False, left: bool = False) -> None:
        '''
        Moves a block to new coordinates

        Args:
            current_x (int): current x coordinate
            current_t (int): current y coordinate
            up (bool): movement direction. Default value is False
            right (bool): movement direction. Default value is False
            down (bool): movement direction. Default value is False
            left (bool): movement direction. Default value is False

        Returns:
            None
        '''
        # step 1 delete cur coordinates
        self.objects_coordinates.discard((current_x, current_y))
        # step 2 add new coordinates
        if up:
            self.objects_coordinates.add((current_x, current_y - 1))
        elif right:
            self.objects_coordinates.add((current_x + 1, current_y))
        elif down:
            self.objects_coordinates.add((current_x, current_y + 1))
        else:
            self.objects_coordinates.add((current_x - 1, current_y))


class Player(Character):
    def __init__(self, image: str, health_points: int, x: int, y: int) -> None:
        super().__init__(image, health_points, x, y)


class Archer(Character):
    def __init__(self, image: str, health_points: int, x: int, y: int, player_actions_before_shot: int) -> None:
        super().__init__(image, health_points, x, y)
        self.player_actions_before_shot = player_actions_before_shot


    def shoot(self, player: Player) -> None:
        pass


class Rock(Block):
    def __init__(self, block_type: str, is_movable: bool, image: str, objects_coordinates: Set[Tuple[int, int]]) -> None:
        super().__init__(block_type, is_movable, image, objects_coordinates)


class Box(Block):
    def __init__(self, block_type: str, is_movable: bool, image: str, objects_coordinates: Set[Tuple[int, int]]) -> None:
        super().__init__(block_type, is_movable, image, objects_coordinates)