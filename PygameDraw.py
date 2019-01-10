def Draw():
    import pygame

    """Initializing Pygame."""
    pygame.init()

    """Title of window."""
    pygame.display.set_caption('Pygame Draw')

    """Binary color setup."""
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    """Interface parameters setup"""
    screen = pygame.display.set_mode((128, 128))
    screen.fill(WHITE)
    mouse = pygame.mouse

    """Drawing interface."""
    program_exit = False
    while not program_exit:
        left_pressed, middle_pressed, right_pressed = mouse.get_pressed()
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                program_exit = True
            elif left_pressed:
                pygame.draw.circle(screen, BLACK, (pygame.mouse.get_pos()), 10)
        pygame.display.update()

    """Grabs a 2d array of the pixels of the drawing interface."""
    screen_array = pygame.surfarray.pixels2d(screen)

    """Modifying the array (from 128x128 to 8x8 pixels) and turning it into a 1d list."""
    lst = []
    row_col_num = [1, 2, 3, 4, 5, 6, 7, 8]
    for j in row_col_num:
        for i in row_col_num:
            lst.append((1 - (sum(sum(screen_array[i*16-16:i*16, j*16-16:j*16])) / 256 / 16777215)) * 7.62)

    """Quitting Pygame."""
    pygame.quit()

    """Returning the list of compressed data of the drawing."""
    return lst
