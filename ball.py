from constants import *
import pygame

class Ball():


    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = BLOCK_SIZE // 2
        self.x_speed = 10
        self.y_speed = 10
        self.rect = pygame.Rect(self.x, self.y, self.radius, self.radius)



    def update(self, player, cpu):



        if self.rect.x < 0 or self.rect.right > GAME_WIDTH:
            self.rect.x = GAME_WIDTH // 2 - self.radius


        if self.rect.colliderect(player.rect):
            self.x_speed = -self.x_speed

        if self.rect.colliderect(cpu.rect):
            self.x_speed = -self.x_speed

        self.rect.x += self.x_speed
        self.rect.y += self.y_speed






        if self.rect.y > GAME_HEIGHT - self.radius:
            self.y_speed = -self.y_speed
        if self.rect.y < self.radius:
            self.y_speed = -self.y_speed




    def draw(self, surface):
        pygame.draw.circle(surface, WHITE, (self.rect.x, self.rect.y), self.radius)
