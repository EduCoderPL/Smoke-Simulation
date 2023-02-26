# Potrzebne importy
import time

import pygame

from pygame.constants import *
from pygame.locals import *

import random

class SmokeParticle:
    dragCoef = 0.98
    list = []
    def __init__(self, x, y, velX, velY, lifeTime):
        self.x = x
        self.y = y

        self.velX = velX
        self.velY = velY

        self.scale = 1
        self.angle = 0

        self.lifeTime = lifeTime
        self.startTime = time.time()
        SmokeParticle.list.append(self)

    def update(self):
        self.velX *= (SmokeParticle.dragCoef * SmokeParticle.dragCoef)
        self.velY *= (SmokeParticle.dragCoef * SmokeParticle.dragCoef)

        self.x += self.velX
        self.y += self.velY

        if time.time() - self.startTime > self.lifeTime:
            SmokeParticle.list.remove(self)
            del self


    def draw(self):
        alpha = 100 * (self.lifeTime - time.time() + self.startTime) / self.lifeTime
        draw_rect_alpha(screen, (100, 100, 100, alpha), Rect(self.x, self.y, 40, 40))

def draw_rect_alpha(surface, color, rect):
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
    surface.blit(shape_surf, rect)



# Odpalenie modułów pygame
pygame.init()

# Parametry Screena
screen = pygame.display.set_mode((1440, 800), pygame.DOUBLEBUF, 32)




def main():
    # Zegar kontrolujący FPS-y
    clock = pygame.time.Clock()


    for i in range(400):
        randX = random.uniform(10, 50)
        randY = random.uniform(-10, 10)
        randTime = random.uniform(4, 6)
        SmokeParticle(100, 500, randX, randY, randTime)

    # Pętla gry
    running = True
    while running:
        # LOGIKA GRY (w przyszłości):
        for particle in SmokeParticle.list:
            particle.update()

        # RYSOWANIE GRAFIKI:

        # Wypełnienie okienka kolorem
        screen.fill((0, 0, 0))

        # Rysowanie kształtów w PyGame
        for particle in SmokeParticle.list:
            particle.draw()


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