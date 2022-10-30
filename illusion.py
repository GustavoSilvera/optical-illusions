import pygame
import random
import math


class Circle:
    def __init__(self, center, color, radius):
        self.center = center
        self.color = color
        self.radius = radius


def RGBColor(idx: int) -> tuple:
    color = None
    if idx == 0:
        color = (255, 0, 0)
    elif idx == 1:
        color = (0, 255, 0)
    elif idx == 2:
        color = (0, 0, 255)
    else:
        raise NotImplementedError
    return color


def col_to_idx(color: tuple) -> int:
    idx = None
    if color == (255, 0, 0):
        idx = 0
    elif color == (0, 255, 0):
        idx = 1
    elif color == (0, 0, 255):
        idx = 2
    else:
        raise NotImplementedError
    return idx


def main() -> None:
    pygame.init()

    # set resolution
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    running: bool = True
    while running:

        random.seed(1)

        # Did the user click the window close button?
        for event in pygame.event.get():  # user input
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # background
        line_ht = 2
        color_idx = 0
        y = 0
        for _ in range(SCREEN_HEIGHT // line_ht):
            line = pygame.Surface(size=(SCREEN_WIDTH, line_ht))
            line.fill(RGBColor(color_idx))
            color_idx = (color_idx + 1) % 3
            screen.blit(line, (0, y))
            y += line_ht

        # draw central circles
        circles = []
        for i in range(9):
            x = SCREEN_WIDTH * (i % 3 + 1) / 4
            y = SCREEN_HEIGHT * (i // 3 + 1) / 4
            r = min(SCREEN_HEIGHT, SCREEN_WIDTH) * 0.1
            pygame.draw.circle(
                surface=screen, color=(181, 142, 53), center=(x, y), radius=r
            )
            """draw mini circles"""
            color_idx = random.randint(a=0, b=2)  # R, G, B
            circles.append(Circle(center=(x, y), radius=r, color=RGBColor(color_idx)))

        for c in circles:
            diameter = 2 * c.radius
            y = col_to_idx(c.color) * line_ht
            for _ in range(int(diameter / (3 * line_ht))):
                line = pygame.Surface(size=(diameter, line_ht))
                line.fill(c.color)
                screen.blit(line, (c.center[0] - c.radius, c.center[1] - c.radius + y))
                y += 3 * line_ht

        pygame.display.flip()  # update display content

    # Done! Time to quit.
    pygame.quit()


if __name__ == "__main__":
    main()
