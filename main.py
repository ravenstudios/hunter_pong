from constants import *
import pygame

import ball
import player
import cpu

clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

pygame.init()


ball = ball.Ball(100, 100)

player = player.Player(0, GAME_HEIGHT // 2 - BLOCK_SIZE * 4)
cpu = cpu.CPU(GAME_WIDTH - BLOCK_SIZE, GAME_HEIGHT // 2 - BLOCK_SIZE * 4)



def main():
    running = True

    while running:
        clock.tick(TICK_RATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if event.key == pygame.K_r:
                    pass
                if event.key == pygame.K_q:
                    running = False
        update()
        draw()


    pygame.quit()



def draw():
    surface.fill((0, 0, 0))#background
    ball.draw(surface)
    player.draw(surface)
    cpu.draw(surface)
    pygame.display.flip()



def update():
    ball.update(player, cpu)
    player.update()
    cpu.update(ball)

if __name__ == "__main__":
    main()
