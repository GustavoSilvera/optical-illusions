import pygame
import random


class Circle:
    def __init__(self, center, color, radius):
        self.center = center
        self.color = color
        self.radius = radius


class Game:
    idx2rgb = {0: (255, 0, 0), 1: (0, 255, 0), 2: (0, 0, 255)}
    rgb2idx = {value: key for key, value in idx2rgb.items()}

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
            line.fill(Game.idx2rgb[color_idx])
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
            circles.append(
                Circle(center=(x, y), radius=r, color=Game.idx2rgb[color_idx])
            )

        if not clicked:
            for c in circles:
                diameter = 2 * c.radius
                y = Game.rgb2idx[c.color] * self.line_ht
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
            elif event.type == pygame.MOUSEBUTTONUP:
                clicked = False

        game.draw_background()

        game.draw_circles(clicked)

        pygame.display.flip()  # update display content

    pygame.quit()


if __name__ == "__main__":
    main()
