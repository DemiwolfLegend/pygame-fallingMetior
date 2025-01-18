import random
import pygame


class Boulder:
    def __init__(self) -> None:
        self.image = pygame.image.load("./content/enemy.png")
        self.x = random.randint(0, 700)
        self.y = random.randint(-500, -100)
        self.change = 2
        self.num = 0

    def reset(self):
        self.x = random.randint(0, 700)
        self.y = random.randint(-500, -100)

    def fall(self):
        self.y += self.change
        if self.y > 800:
            self.reset()

    def isColide(self, player, score):
        collison1 = self.y >= 600 and player.y > 0 and (self.x > (player.x-100) and self.x < (player.x+100))
        bullet = player.bullet
        collison2 = (bullet.y <= self.y+100) and (bullet.x >(self.x-10) and bullet.x < (self.x+110))
        if collison1:
            player.y = -600
            score.addon = False
            return True
        elif collison2:
            player.bullet.reset()
            score.plus()
            self.reset()
            return True
        else:
            return False

    def show(self, screen):
        screen.blit(self.image, (self.x, self.y))
