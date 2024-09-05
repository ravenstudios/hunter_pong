from constants import *
import pygame

import ball

class Player():


    def __init__(self, x, y):
        self.width = BLOCK_SIZE
        self.height = BLOCK_SIZE * 8
        self.x = x
        self.y = y
        self.speed = 5
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        print(f"x:{self.rect.x}")
        self.rect.y = max(0, min(self.rect.y, GAME_HEIGHT))


        if self.rect.y + self.height > GAME_HEIGHT:

            self.rect.y = GAME_HEIGHT - self.height

        if pygame.key.get_pressed()[pygame.K_UP]:
            self.rect.y -= self.speed
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.rect.y += self.speed



    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.rect)
