import pygame


color0 = pygame.Color("#a66c46")
color1 = pygame.Color("#7ec0ee")

pygame.init()

pygame.display.set_caption("Mousetracker")

clock = pygame.time.Clock()
screen = pygame.display.set_mode([640, 480])

font = pygame.font.Font(None, 28)


def main():
    circle_position = (screen.get_width() // 2), (screen.get_height() // 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEMOTION:
                circle_position = event.__dict__["pos"]

            screen.fill(color0)
            pygame.draw.circle(screen, color1, circle_position, 20)
            text = font.render(str(circle_position), True, (255, 255, 255))
            screen.blit(text, (320, 240))

            pygame.display.update()

            clock.tick(60)


main()
