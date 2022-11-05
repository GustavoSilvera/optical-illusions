import pygame
import random
import math


class Circle:
    def __init__(self, x: float, y: float, color: tuple, radius: float):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.vel_x = random.random() - 0.5  # random [-0.5, 0.5]
        self.vel_y = random.random() - 0.5  # random [-0.5, 0.5]

    def tick(self, dt, ht, wt):
        self.x += dt * self.vel_x
        self.y += dt * self.vel_y
        if self.x > wt - self.radius or self.x < self.radius:
            self.vel_x *= -1
        if self.y > ht - self.radius or self.y < self.radius:
            self.vel_y *= -1
        self.x = max(min(self.x, wt - self.radius), self.radius)
        self.y = max(min(self.y, ht - self.radius), self.radius)


class Game:
    idx2rgb = {0: (255, 0, 0), 1: (0, 255, 0), 2: (0, 0, 255)}
    rgb2idx = {value: key for key, value in idx2rgb.items()}
    circle_color = (181, 142, 53)  # the actual (background colour background)

    def __init__(self, h, w, line_ht=2):
        self.SCREEN_HEIGHT = h
        self.SCREEN_WIDTH = w

        self.line_ht = line_ht
        self.screen = pygame.display.set_mode(
            [self.SCREEN_WIDTH, self.SCREEN_HEIGHT], pygame.RESIZABLE, vsync=60
        )
        pygame.display.set_caption("gsilvera's E/A/C Illusion game")
        self.clock = pygame.time.Clock()

        self.line_ht = 2
        self.circles = [
            Circle(
                x=self.SCREEN_WIDTH * ((i % 9) % 3 + 1) / 4,
                y=self.SCREEN_HEIGHT * ((i % 9) // 3 + 1) / 4,
                radius=min(self.SCREEN_HEIGHT, self.SCREEN_WIDTH) * 0.1,
                color=Game.idx2rgb[random.randint(a=0, b=2)],
            )
            for i in range(100)
        ]

        # inputs
        self.clicked = False

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

    def draw_circles(self, dt):
        """draw mini circles"""
        for circle in self.circles:
            pygame.draw.circle(
                surface=self.screen,
                color=Game.circle_color,
                center=(circle.x, circle.y),
                radius=circle.radius,
            )
            circle.tick(dt, self.SCREEN_HEIGHT, self.SCREEN_WIDTH)

        if not self.clicked:
            # draw lines over the circles
            for c in self.circles:
                diameter = 2 * c.radius
                y = Game.rgb2idx[c.color] * self.line_ht
                for _ in range(int(diameter // (3 * self.line_ht))):
                    width_radius_at_y = math.sqrt(c.radius**2 - ((c.radius - y) ** 2))
                    line = pygame.Surface(size=(2 * width_radius_at_y, self.line_ht))
                    line.fill(c.color)
                    self.screen.blit(
                        line, (c.x - width_radius_at_y, c.y - c.radius + y)
                    )
                    y += 3 * self.line_ht

    def tick(self) -> bool:
        dt = self.clock.tick()

        running: bool = True
        for event in pygame.event.get():  # user input
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.clicked = True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.clicked = False
            if event.type == pygame.VIDEORESIZE:
                self.SCREEN_HEIGHT = event.h
                self.SCREEN_WIDTH = event.w
                self.screen = pygame.display.set_mode(
                    (self.SCREEN_WIDTH, self.SCREEN_HEIGHT), pygame.RESIZABLE
                )

        self.draw_background()

        self.draw_circles(dt)

        return running


def main() -> None:
    pygame.init()

    # set resolution
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    running: bool = True

    game = Game(SCREEN_HEIGHT, SCREEN_WIDTH)

    while running:

        running = game.tick()

        pygame.display.flip()  # update display content

    pygame.quit()


if __name__ == "__main__":
    main()
