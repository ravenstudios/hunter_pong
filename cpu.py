from constants import *
import pygame

import ball
import player


class CPU(player.Player):
    def __init__(self, x, y):
        super().__init__(x, y)



    def update(self, ball):
        self.rect.y = max(0, min(self.rect.y, GAME_HEIGHT))
        if ball.rect.y > GAME_WIDTH // 2:
            self.rect.y += self.speed

        if ball.rect.y < GAME_WIDTH // 2:
            self.rect.y -= self.speed



        tup = (1, 2, 3)
        list = [1, 2, 4]
