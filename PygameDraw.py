import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


screen = pygame.display.set_mode((160, 160))
pygame.display.set_caption('Pygame Draw')

game_exit = False

while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True

pygame.quit()
quit()