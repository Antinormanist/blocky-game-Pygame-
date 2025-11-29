from typing import List, Set, Tuple, Optional, Dict
import pygame

def main():
    BACKGROUND_RGB = (141, 201, 115)

    pygame.init()

    width = 500
    height = 500
    screen = pygame.display.set_mode((width, height))

    player = pygame.image.load('.\\images\\cube.jpg')
    box = pygame.image.load('.\\images\\box.jpg')
    rock = pygame.image.load('.\\images\\rock.jpg')

    box_coordinates = {(4, 0), (6, 8)}
    rock_coordinates = {(2, 2), (4, 6), (7, 9)}

    all_immovable_obstacle_coordinates = {'rock': rock_coordinates, 'box': box_coordinates}

    player_x = player_y = 0

    running = True
    while running:
        screen.fill(BACKGROUND_RGB)
        screen.blit(player, (player_x * 50, player_y * 50))
        
        for rock_x, rock_y in rock_coordinates:
            screen.blit(rock, (rock_x * 50, rock_y * 50))

        for box_x, box_y in box_coordinates:
            screen.blit(box, (box_x * 50, box_y * 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    if player_x < width // 50 - 1:
                        has_collision, obstacle = check_if_target_has_collision(player_x + 1, player_y, all_immovable_obstacle_coordinates)
                        if has_collision:
                            if obstacle == 'box':
                                box_x = player_x + 1
                                box_y = player_y 
                                if not check_if_target_has_collision(box_x + 1, box_y, all_immovable_obstacle_coordinates)[0] and box_x < width // 50 - 1:
                                    box_coordinates.discard((box_x, box_y))
                                    box_coordinates.add((box_x + 1, box_y))
                                    player_x += 1
                        else:
                            player_x += 1
                elif event.key == pygame.K_a:
                    if 0 < player_x:
                        has_collision, obstacle = check_if_target_has_collision(player_x - 1, player_y, all_immovable_obstacle_coordinates)
                        if has_collision:
                            if obstacle == 'box':
                                box_x = player_x - 1
                                box_y = player_y 
                                if not check_if_target_has_collision(box_x - 1, box_y, all_immovable_obstacle_coordinates)[0] and 0 < box_x:
                                    box_coordinates.discard((box_x, box_y))
                                    box_coordinates.add((box_x - 1, box_y))
                                    player_x -= 1
                        else:
                            player_x -= 1
                elif event.key == pygame.K_w:
                    if 0 < player_y:
                        has_collision, obstacle = check_if_target_has_collision(player_x, player_y - 1, all_immovable_obstacle_coordinates)
                        if has_collision:
                            if obstacle == 'box':
                                box_x = player_x
                                box_y = player_y - 1
                                if not check_if_target_has_collision(box_x, box_y - 1, all_immovable_obstacle_coordinates)[0] and 0 < box_y:
                                    box_coordinates.discard((box_x, box_y))
                                    box_coordinates.add((box_x, box_y - 1))
                                    player_y -= 1
                        else:
                            player_y -= 1
                elif event.key == pygame.K_s:
                    if player_y < height // 50 - 1:
                        has_collision, obstacle = check_if_target_has_collision(player_x, player_y + 1, all_immovable_obstacle_coordinates)
                        if has_collision:
                            if obstacle == 'box':
                                box_x = player_x
                                box_y = player_y + 1
                                if not check_if_target_has_collision(box_x, box_y + 1, all_immovable_obstacle_coordinates)[0] and box_y < height // 50 - 1:
                                    box_coordinates.discard((box_x, box_y))
                                    box_coordinates.add((box_x, box_y + 1))
                                    player_y += 1
                        else:
                            player_y += 1

        pygame.display.flip()

    pygame.quit()


def check_if_target_has_collision(target_x: int, target_y: int, obstacles: Dict[str, Set[Tuple[int]]]) -> Tuple[bool, Optional[str]]:
    '''
    Returns True and collisiong block if player has any collision with an obstacle, otherwise True
    '''
    for obstacle_type, obstacle_coordinates in obstacles.items():
        for obstacle_x, obstacle_y in obstacle_coordinates:
            if (target_x, target_y) == (obstacle_x, obstacle_y):
                return (True, obstacle_type)
    return (False, None)





if __name__ == '__main__':
    main()