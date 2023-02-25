# Potrzebne importy
import pygame

from pygame.constants import *
from pygame.locals import *

# Odpalenie modułów pygame
pygame.init()

# Parametry Screena
screen = pygame.display.set_mode((1280, 720))


def main():
    # Zegar kontrolujący FPS-y
    clock = pygame.time.Clock()

    # Pętla gry
    running = True
    while running:
        # LOGIKA GRY (w przyszłości):


        # RYSOWANIE GRAFIKI:

        # Wypełnienie okienka kolorem
        screen.fill((255, 255, 255))

        # Rysowanie kształtów w PyGame
        pygame.draw.rect(screen, (255, 255, 0), Rect(100, 100, 50, 50))
        pygame.draw.ellipse(screen, (255, 255, 0), Rect(100, 300, 50, 50))
        pygame.draw.aaline(screen, (255, 0, 0), (50, 50), (1000, 1000))
        pygame.draw.circle(screen, (128, 0, 0), (400, 400), 30)


        # Czekanie na kolejną klatkę
        clock.tick(60)

        #Aktualizacja gry
        pygame.display.flip()

        # Te cztery linijki pozwalają nam normalnie zamknąć program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

    pygame.quit()

main()