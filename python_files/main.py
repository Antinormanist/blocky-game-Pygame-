from typing import List, Set, Tuple, Optional, Dict

import pygame

import constants
import functions
import classes


def main():
    pygame.init()

    functions.load_background_music()

    width = constants.WINDOW_WIDTH
    height = constants.WINDOW_HEIGHT
    screen = pygame.display.set_mode((width, height))

    box_coordinates = {(4, 0), (6, 8)}
    rock_coordinates = {(2, 2), (4, 6), (7, 9)}

    player = classes.Player(constants.PLAYER_IMAGE, 100, 0, 0)
    boxes = classes.Box('box', True, constants.BOX_IMAGE, box_coordinates)
    rocks = classes.Rock('rock', False, constants.ROCK_IMAGE, rock_coordinates)

    all_obstacles = (boxes, rocks)

    running = True
    while running:
        screen.fill(constants.BACKGROUND_RGB)
        screen.blit(player.image, (player.x * 50, player.y * 50))
        
        functions.show_obstacles(screen, all_obstacles)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    functions.move_player_up(player, all_obstacles)
                elif event.key == pygame.K_d:
                    functions.move_player_right(player, all_obstacles)
                elif event.key == pygame.K_s:
                    functions.move_player_down(player, all_obstacles)
                elif event.key == pygame.K_a:
                    functions.move_player_left(player, all_obstacles)
                    

        pygame.display.flip()

    pygame.quit()



if __name__ == '__main__':
    main()