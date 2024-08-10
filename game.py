import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

class Player:
    y = 0
    x = 150
    def draw(self):
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, 50, 50))

player = Player()

class Enemy:
    def __init__(self):
        random.randint(0, int((pygame.display.get_window_size()[1]*14)/15))
        self.w = pygame.display.get_window_size()[1]/15 
        self.h = pygame.display.get_window_size()[1]/15
        self.x = pygame.display.get_window_size()[0]
        self.y = pygame.display.get_window_size()[1]/2

    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.w, self.h))
enemies = [Enemy()]

def update(black_count):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return


    screen.fill("white")

    player.y = black_count/1000.0
    player.draw()

    for enemy in enemies:
        enemy.draw()
        enemy.x -= int(pygame.display.get_window_size()[0]/250)
        if enemy.x < pygame.display.get_window_size()[0]/15:
            enemies.remove(enemy)
            enemies.append(Enemy())
            enemies.append(Enemy())
            break

    pygame.display.flip()

    clock.tick(60)

