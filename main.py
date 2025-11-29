from typing import List, Set, Tuple
import pygame

def main():
    pygame.init()

    width = 500
    height = 500
    screen = pygame.display.set_mode((width, height))

    player = pygame.image.load('.\\images\\cube.jpg')
    rock = pygame.image.load('.\\images\\rock.jpg')

    rock_coordinates = {(2, 2), (4, 6), (7, 9)}

    all_immovable_obstacle_coordinates = [rock_coordinates]

    player_x = player_y = 0

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(player, (player_x * 50, player_y * 50))
        
        for rock_x, rock_y in rock_coordinates:
            screen.blit(rock, (rock_x * 50, rock_y * 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    if player_x < width // 50 - 1:
                        if not check_if_player_has_collision(player_x + 1, player_y, all_immovable_obstacle_coordinates):
                            player_x += 1
                elif event.key == pygame.K_a:
                    if 0 < player_x:
                        if not check_if_player_has_collision(player_x - 1, player_y, all_immovable_obstacle_coordinates):
                            player_x -= 1
                elif event.key == pygame.K_w:
                    if 0 < player_y:
                        if not check_if_player_has_collision(player_x, player_y - 1, all_immovable_obstacle_coordinates):
                            player_y -= 1
                elif event.key == pygame.K_s:
                    if player_y < height // 50 - 1:
                        if not check_if_player_has_collision(player_x, player_y + 1, all_immovable_obstacle_coordinates):
                            player_y += 1

        pygame.display.flip()

    pygame.quit()


def check_if_player_has_collision(player_x: int, player_y: int, obstacles: List[Set[Tuple[int]]]) -> bool:
    '''
    Returns True if player has any collision with an obstacle, otherwise True
    '''
    for obstacle_coordinates in obstacles:
        for obstacle_x, obstacle_y in obstacle_coordinates:
            if (player_x, player_y) == (obstacle_x, obstacle_y):
                return True
    return False


if __name__ == '__main__':
    main()