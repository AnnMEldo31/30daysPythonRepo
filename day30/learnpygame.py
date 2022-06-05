import pygame
import project_snek.colors as pc
from collections import namedtuple
from random import randint

# Colour = namedtuple("Colour", ["red", "green", "blue"])

# BACKGROUND = Colour(red=36, green=188, blue=168)
# SECONDARY_RED = Colour(red=219, green=47, blue=67)
# SECONDARY_GREEN = Colour(red=0, green=153, blue=57)
# BALL_COLOR = Colour(red=255, green=255, blue=0)

BALL_RADIUS = 50

pygame.init()

pygame.display.set_caption("Bouncing Ball")

clock = pygame.time.Clock()
screen = pygame.display.set_mode([640, 480])

# pygame.draw.rect(screen, SECONDARY_COLOR_WRONG, [382, 190, 134, 100])
# pygame.draw.circle(screen, (255, 255, 255), (95, 95), 80)
# pygame.draw.circle(screen, (255, 255, 0), (320, 240), 50)


def main():
    ball_position = [screen.get_width() // 2, screen.get_height() // 2]
    ball_velocity = [randint(-5, 5), randint(-5, 5)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(pc.BACKGROUND)
        pygame.draw.circle(screen, pc.SNAKE, ball_position, BALL_RADIUS)
        pygame.draw.rect(screen, pc.FOOD, [124, 190, 134, 100])

        font = pygame.font.Font(None, 28)
        text = font.render("Woo! This is some text!", True, pc.TEXT)
        screen.blit(text, (350, 20))

        pygame.display.update()

        # check for left and right collisions
        if ball_position[0] - BALL_RADIUS < 0:
            ball_velocity[0] = -ball_velocity[0]
        elif ball_position[0] + BALL_RADIUS > screen.get_width():
            ball_velocity[0] = -ball_velocity[0]

        # check for top and bottom collisions
        if ball_position[1] - BALL_RADIUS < 0:
            ball_velocity[1] = -ball_velocity[1]
        elif ball_position[1] + BALL_RADIUS > screen.get_height():
            ball_velocity[1] = -ball_velocity[1]

        # ball_position[0] += 5
        ball_position[0] += ball_velocity[0]
        ball_position[1] += ball_velocity[1]

        clock.tick(60)


main()
