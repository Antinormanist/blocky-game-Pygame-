import pygame

pygame.init()

width = 500
height = 500
screen = pygame.display.set_mode((width, height))

player = pygame.image.load('.\\images\\cube.jpg')
player_x = player_y = 0

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(player, (player_x * 50, player_y * 50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                if player_x < width // 50 - 1:
                    player_x += 1
            elif event.key == pygame.K_a:
                if 0 < player_x: 
                    player_x -= 1
            elif event.key == pygame.K_w:
                if 0 < player_y:
                    player_y -= 1
            elif event.key == pygame.K_s:
                if player_y < height // 50 - 1:
                    player_y += 1

    pygame.display.flip()

pygame.quit()