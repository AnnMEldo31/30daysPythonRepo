# A snake trying to gather food. Every time the snake's head passes through a square containing food, you get a point,
# and the snake also grows by a certain amount.
#
# If you hit your own body, or the walls of the play area, you die, and the game ends.
#
# Aim: Score max points
#
# For this implementation, the game should be controlled by keyboard keys (arrow keys).
# Pressing these different keys should set a new course for the snake.
#
# A single piece of food should be in the play area at a time, and when the snake eats a piece of food,
# another piece should be randomly placed within the play area.
# This should not occupy the same space as any of the snake's segments.
#
# Finally, a running total of the user's score should be displayed in the top left of the screen.

import pygame
import colors
from random import randint

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 840
WINDOW_DIMENSIONS = WINDOW_WIDTH, WINDOW_HEIGHT

SEGMENT_SIZE = 20

KEY_MAP = {
    82: "Up",
    81: "Down",
    80: "Left",
    79: "Right"
}

pygame.init()
pygame.display.set_caption("Snake!")

clock = pygame.time.Clock()
screen = pygame.display.set_mode(WINDOW_DIMENSIONS)


def check_food_collected(snake_positions, food_position):
    if snake_positions[0] == food_position:
        snake_positions.append(snake_positions[-1])

        return True


def check_collisions(snake_positions):
    head_x_position, head_y_position = snake_positions[0]

    return (
        head_x_position in (-20, WINDOW_WIDTH)
        or head_y_position in (20, WINDOW_HEIGHT)
        or (head_x_position, head_y_position) in snake_positions[1:]
    )   # true for collision detected, false for no collision


def on_key_press(event, current_direction):
    key = event.__dict__["scancode"]
    new_direction = KEY_MAP.get(key)

    all_directions = ("Up", "Down", "Left", "Right")
    opposite_directions = ({"Up", "Down"}, {"Left", "Right"})

    if new_direction in all_directions and {new_direction, current_direction} not in opposite_directions:
        return new_direction

    return current_direction


def move_snake(snake_positions, direction):
    head_x_position, head_y_position = snake_positions[0]

    new_head_position = snake_positions[0]

    if direction == "Left":
        new_head_position = (head_x_position - SEGMENT_SIZE, head_y_position)
    elif direction == "Right":
        new_head_position = (head_x_position + SEGMENT_SIZE, head_y_position)
    elif direction == "Up":
        new_head_position = (head_x_position, head_y_position - SEGMENT_SIZE)
    elif direction == "Down":
        new_head_position = (head_x_position, head_y_position + SEGMENT_SIZE)

    snake_positions.insert(0, new_head_position)
    del snake_positions[-1]


def set_new_food_position(snake_positions):
    boundary_x = (WINDOW_WIDTH // SEGMENT_SIZE) - 1
    boundary_y = (WINDOW_HEIGHT // SEGMENT_SIZE) - 1

    while True:
        new_x_position = randint(0, boundary_x) * SEGMENT_SIZE
        new_y_position = randint(2, boundary_y) * SEGMENT_SIZE
        new_food_position = (new_x_position, new_y_position)

        if new_food_position not in snake_positions:
            return new_food_position


def draw_objects(snake_positions, food_position):
    pygame.draw.rect(screen, colors.FOOD, [food_position, (SEGMENT_SIZE, SEGMENT_SIZE)])

    for pos in snake_positions:
        pygame.draw.rect(screen, colors.SNAKE, [pos, (SEGMENT_SIZE, SEGMENT_SIZE)])


def play_game():
    score = 0

    current_direction = "Right"
    snake_positions = [(100, 100), (80, 100), (60, 100)]
    food_position = set_new_food_position(snake_positions)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                current_direction = on_key_press(event, current_direction)

        screen.fill(colors.BACKGROUND)
        draw_objects(snake_positions, food_position)

        font = pygame.font.Font(None, 28)
        score_text = font.render(f"Score: {score}", True, colors.TEXT)
        screen.blit(score_text, (10, 10))

        pygame.display.update()

        move_snake(snake_positions, current_direction)
        if check_collisions(snake_positions):
            return
        elif check_food_collected(snake_positions, food_position):
            score += 1
            set_new_food_position(snake_positions)

        clock.tick(15)


play_game()
