import sys
import pygame


def run_game():
    pygame.init()
    screen = pygame.display.set_mide((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.Quit:
                sys.exit()

        pygame.display.flip()


run_game()
