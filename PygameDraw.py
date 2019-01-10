import pygame
import numpy as np


"""Initialize Pygame."""
pygame.init()


"""Title of window."""
pygame.display.set_caption('Pygame Draw')


"""Binary color setup."""
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


"""Program parameters setup"""
screen = pygame.display.set_mode((128, 128))
screen.fill(WHITE)
mouse = pygame.mouse
clock = pygame.time.Clock()


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


screen_array = pygame.surfarray.pixels2d(screen)

"""
string = str(screen_array)
print(string)


screen_lst = [i for i in string.split()]
print(screen_lst)


string2 = str(screen_lst).replace("'", "")
string2 = string2[3: -3]
string2 = string2.replace('[, ', '[')
print(string2)


lst = [[i.strip() for i in row.split(',')] for row in string2.split(',')]
print(lst)
"""


def blockshaped(arr, nrows, ncols):
    """
    Return an array of shape (n, nrows, ncols) where
    n * nrows * ncols = arr.size

    If arr is a 2D array, the returned array should look like n subblocks with
    each subblock preserving the "physical" layout of arr.
    """
    h, w = arr.shape
    return (arr.reshape(h//nrows, nrows, -1, ncols)
               .swapaxes(1,2)
               .reshape(-1, nrows, ncols))



print(screen_array.dtype)
print(screen_array.ndim)
print(screen_array.size)
print(screen_array.shape)

print(1 - (sum(sum(screen_array[0:16, 0:16])) / 256 / 16777215))
print(1 - (sum(sum(screen_array[16:32, 0:16])) / 256 / 16777215))
print(1 - (sum(sum(screen_array[32:48, 0:16])) / 256 / 16777215))
print(1 - (sum(sum(screen_array[48:64, 0:16])) / 256 / 16777215))





"""
redone = blockshaped(screen_array, 8, 8)

print(redone)


print(screen_array)

new = np.reshape(screen_array, (-1,1))
print(new)


# numpy.ravel
"""


pygame.quit()

quit()