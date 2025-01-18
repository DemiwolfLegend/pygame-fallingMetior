import pygame
import random
from pygame import mixer

from assets.character import Character
from assets.score import Score
from assets.boulder import Boulder

pygame.init()

pygame.display.set_caption("firstGame")

screen = pygame.display.set_mode((800, 800))
backgroundImage = pygame.image.load("./content/background.png")
# back_music = mixer.music.load("./content/background.wav")
# mixer.music.play(-1)

player = Character()
score = Score()
enemy = []
numFall = 10
for i in range(numFall):
    enemy.append(Boulder())

run = True
while run:
    screen.blit(backgroundImage, (0, 0))

    run = player.move(score)
    for i in range(numFall):
        enemy[i].fall()
        if enemy[i].isColide(player, score):
            break
        enemy[i].show(screen)

    player.show(screen)
    score.show(screen)
    if not score.addon:
        score.over(screen)
    pygame.display.update()
