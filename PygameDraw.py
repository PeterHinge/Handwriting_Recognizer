import pygame

pygame.init()

"""Title of window."""
pygame.display.set_caption('Pygame Draw')

"""Binary color setup."""
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


screen = pygame.display.set_mode((128, 128))
screen.fill(WHITE)
mouse = pygame.mouse
clock = pygame.time.Clock()

game_exit = False

while not game_exit:
    left_pressed, middle_pressed, right_pressed = mouse.get_pressed()
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            game_exit = True
        elif left_pressed:
            pygame.draw.circle(screen, BLACK, (pygame.mouse.get_pos()), 10)
    pygame.display.update()

screen_array = pygame.surfarray.array2d(screen)

print(screen_array)

pygame.quit()

quit()