import pygame
import random


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


class Game:
    def __init__(self, h, w, line_ht=2):
        self.SCREEN_HEIGHT = h
        self.SCREEN_WIDTH = w

        self.init_game()
        self.line_ht = line_ht

    def init_game(self):
        self.screen = pygame.display.set_mode([self.SCREEN_WIDTH, self.SCREEN_HEIGHT])
        self.line_ht = 2
        self.colors = [random.randint(a=0, b=2) for _ in range(9)]

    def draw_background(self):
        self.screen.fill((0, 0, 0))  # background
        color_idx = 0
        y = 0
        for _ in range(self.SCREEN_HEIGHT // self.line_ht):
            line = pygame.Surface(size=(self.SCREEN_WIDTH, self.line_ht))
            line.fill(RGBColor(color_idx))
            color_idx = (color_idx + 1) % 3
            self.screen.blit(line, (0, y))
            y += self.line_ht

    def draw_circles(self, clicked: bool):
        circles = []
        for i in range(9):
            x = self.SCREEN_WIDTH * (i % 3 + 1) / 4
            y = self.SCREEN_HEIGHT * (i // 3 + 1) / 4
            r = min(self.SCREEN_HEIGHT, self.SCREEN_WIDTH) * 0.1
            pygame.draw.circle(
                surface=self.screen, color=(181, 142, 53), center=(x, y), radius=r
            )
            """draw mini circles"""
            color_idx = self.colors[i]
            circles.append(Circle(center=(x, y), radius=r, color=RGBColor(color_idx)))

        if not clicked:
            for c in circles:
                diameter = 2 * c.radius
                y = col_to_idx(c.color) * self.line_ht
                for _ in range(int(diameter / (3 * self.line_ht))):
                    line = pygame.Surface(size=(diameter, self.line_ht))
                    line.fill(c.color)
                    self.screen.blit(
                        line, (c.center[0] - c.radius, c.center[1] - c.radius + y)
                    )
                    y += 3 * self.line_ht


def main() -> None:
    pygame.init()

    # set resolution
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    running: bool = True
    clicked = False

    game = Game(SCREEN_HEIGHT, SCREEN_WIDTH)

    while running:

        for event in pygame.event.get():  # user input
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True

        game.draw_background()

        game.draw_circles(clicked)

        pygame.display.flip()  # update display content

    pygame.quit()


if __name__ == "__main__":
    main()
