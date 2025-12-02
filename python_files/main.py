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
    settings = constants.SETTINGS

    player = classes.Player(constants.PLAYER_IMAGE, 100, 0, 0)

    current_region = 1
    current_zone = 1

    running = True
    while running:
        obstacles = constants.ZONES_OBSTACLES[current_zone]

        # screen blits

        screen.fill(constants.BACKGROUND_RGB)
        screen.blit(player.image, (player.x * 50, player.y * 50))
        
        functions.show_obstacles(screen, obstacles)

        # load settings
        screen.blit(settings, (constants.WINDOW_WIDTH - 25, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # movements
                if event.key == pygame.K_w:
                    if player.y == 0:
                        new_region = constants.ZONES_DIRECTIONS[current_zone][0]
                        if new_region:
                            # has region
                            current_zone = new_region
                            player.set_coordinates(player.x, constants.WINDOW_HEIGHT // 50 - 1)
                            continue
                    
                    functions.move_player_up(player, obstacles)
                elif event.key == pygame.K_d:
                    if player.x == constants.WINDOW_WIDTH // 50 - 1:
                        new_region = constants.ZONES_DIRECTIONS[current_zone][1]
                        if new_region:
                            # has region
                            current_zone = new_region
                            player.set_coordinates(0, player.y)
                            continue
                    functions.move_player_right(player, obstacles)
                elif event.key == pygame.K_s:
                    if player.y == constants.WINDOW_HEIGHT // 50 - 1:
                        new_region = constants.ZONES_DIRECTIONS[current_zone][2]
                        if new_region:
                            # has region
                            current_zone = new_region
                            player.set_coordinates(player.x, 0)
                            continue
                    functions.move_player_down(player, obstacles)
                elif event.key == pygame.K_a:
                    if player.x == 0:
                        new_region = constants.ZONES_DIRECTIONS[current_zone][3]
                        if new_region:
                            # has region
                            current_zone = new_region
                            player.set_coordinates(constants.WINDOW_WIDTH // 50 - 1, player.y)
                            continue
                    functions.move_player_left(player, obstacles)
                # settings
                elif event.key == pygame.K_BACKQUOTE:
                    pass
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if constants.WINDOW_WIDTH  - 25 <= x and y <= 25:
                    # show settings menu
                    pass
                    

        pygame.display.flip()

    pygame.quit()



if __name__ == '__main__':
    main()