try:
    import pygame
except Exception as e:
    print(f'Unable to import "pygame" that is required for this game to run! ({e})')
    print()
    print("try installing pygame (https://www.pygame.org/) with:")
    print('  "pip install pygame"')
    print("in your terminal")
    exit(1)
import random


# TODO: also include an illusion with shading and ambiguous shape reconstruction


class Circle:
    def __init__(self, x: float, y: float, color: tuple, radius: float):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.vel_x = 0.3 * (random.random() - 0.5)
        self.vel_y = 0.3 * (random.random() - 0.5)
        self.reveal = False

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
    rgb2str = {(255, 0, 0): "RED", (0, 255, 0): "GREEN", (0, 0, 255): "BLUE"}
    circle_color = (181, 142, 53)  # the actual (background colour background)

    def __init__(self, h, w, line_ht=2):
        self.SCREEN_HEIGHT = h
        self.SCREEN_WIDTH = w

        self.line_ht = line_ht
        self.screen = pygame.display.set_mode(
            [self.SCREEN_WIDTH, self.SCREEN_HEIGHT], pygame.RESIZABLE, vsync=60
        )
        pygame.display.set_caption("Gustavo's 85-211 E/A/C Illusion Game")
        self.clock = pygame.time.Clock()

        self.line_ht = 2
        self.circles = [
            Circle(
                x=self.SCREEN_WIDTH * ((i % 9) % 3 + 1) / 4,
                y=self.SCREEN_HEIGHT * ((i % 9) // 3 + 1) / 4,
                radius=random.randint(a=40, b=60),
                color=Game.idx2rgb[random.randint(a=0, b=2)],
            )
            for i in range(20)
        ]
        self.num_secrets = len(self.circles)

        # inputs
        self.clicked = None

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

    def tick_circles(self, dt):
        for circle in self.circles:
            circle.tick(dt, self.SCREEN_HEIGHT, self.SCREEN_WIDTH)
            if self.clicked is not None:
                x, y = self.clicked
                dist = ((x - circle.x) ** 2 + (y - circle.y) ** 2) ** 0.5
                if dist < circle.radius:
                    if circle.reveal == False:
                        print(
                            f'Revealed a "{self.rgb2str[circle.color]}" circle to be "BROWN"'
                            f" -- (Secret {len(self.circles) - self.num_secrets + 1}/{len(self.circles)})"
                        )
                        self.num_secrets -= 1
                        if self.num_secrets == 0:
                            self.win()
                    circle.reveal = True

    def win(self):
        print()
        print("Congratulations you found all the secrets!")
        print("As it turns out... All of these circles are actually the same colour!")
        print("This is simply an optical illusion to for perceiving colours on circles")
        print("similar to how we perceive colours on a pixel-based screen!")
        print("Illusions are fun!")
        print()
        print("Press 'R' to restart the game")

    def draw_circles(self, dt):
        """draw mini circles"""
        for c in self.circles:
            pygame.draw.circle(
                surface=self.screen,
                color=Game.circle_color,
                center=(c.x, c.y),
                radius=c.radius,
            )
            # draw lines over the circles
            if c.reveal:
                continue  # not drawing over this circle
            aligned_y = None
            i = 0
            # for i in range(int(diameter // (3 * self.line_ht))):
            while aligned_y is None or aligned_y + self.line_ht < c.y + c.radius:
                # compute where the line is drawn to align with bg
                aligned_y = Game.rgb2idx[c.color] * self.line_ht + 3 * self.line_ht * (
                    int((c.y - c.radius) / (3 * self.line_ht)) + i
                )
                i += 1
                if aligned_y > c.y + c.radius:  # no extra bars beneath circle
                    break
                if aligned_y + self.line_ht < c.y - c.radius:
                    continue  # skip drawing if not overlapping circle!
                # compute how long the bar is (minimally overlapping!)
                top_ht = c.radius**2 - (c.y - aligned_y) ** 2
                top_ht = top_ht**0.5 if top_ht > 0 else -1
                next_y = aligned_y + self.line_ht  # one line down
                bot_ht = c.radius**2 - (c.y - next_y) ** 2
                bot_ht = bot_ht**0.5 if bot_ht > 0 else -1

                width_radius_at_y = max(top_ht, bot_ht)
                if width_radius_at_y <= 0:
                    continue  # skip this one!
                line = pygame.Surface(size=(2 * width_radius_at_y, self.line_ht))
                # colour and draw the bar
                line.fill(c.color)
                self.screen.blit(line, (c.x - width_radius_at_y, aligned_y))
                # print(f"{aligned_y + self.line_ht} | {c.y + c.radius}  ||  {top_ht} {bot_ht}")

    def tick(self) -> bool:
        dt = self.clock.tick()

        running: bool = True
        self.clicked = None
        for event in pygame.event.get():  # user input
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_UP:
                    new_ht = min(10, self.line_ht + 1)
                    if new_ht != self.line_ht:
                        print(f"Increasing resolution from {self.line_ht} to {new_ht}")
                    self.line_ht = new_ht
                elif event.key == pygame.K_DOWN:
                    new_ht = max(1, self.line_ht - 1)
                    if new_ht != self.line_ht:
                        print(f"Decreasing resolution from {self.line_ht} to {new_ht}")
                    self.line_ht = new_ht
                elif event.key == pygame.K_r:
                    # reset the game
                    self.__init__(self.SCREEN_HEIGHT, self.SCREEN_WIDTH)

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.clicked = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONUP:
                self.clicked = None
            if event.type == pygame.VIDEORESIZE:
                self.SCREEN_HEIGHT = event.h
                self.SCREEN_WIDTH = event.w
                self.screen = pygame.display.set_mode(
                    (self.SCREEN_WIDTH, self.SCREEN_HEIGHT), pygame.RESIZABLE
                )

        self.draw_background()

        self.tick_circles(dt)

        self.draw_circles(dt)

        return running


def main() -> None:
    version = 1.0
    print(f"Welcome to v{version:.1f} of Gustavo's illusion game!")
    print()
    print(f"Controls:")
    print(f"Click on a circle to reveal its true colours!")
    print(f'Up/Down arrows to change the "resolution"')
    print(f"Press 'R' to reset the reveal status")
    print(f"Press ESC to quit the game")
    print()
    print(f"Have fun!")

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
