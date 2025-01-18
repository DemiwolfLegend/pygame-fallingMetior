import pygame


class Bullet:
    def __init__(self) -> None:
        self.image = pygame.image.load("./content/bullet.png")
        self.x = 800
        self.y = 700
        self.change = 10
        self.state = False

    def aim(self,player):
        self.x = player.x
        self.y = player.y
        self.state = True

    def show(self,screen):
        screen.blit(self.image, (self.x, self.y))
        # print(self.x, self.y)

    def reset(self):
        self.state = False
        self.y = 700
        self.x = 800

    def move(self):
        self.y -= self.change
        if self.y < -10:
            self.reset()

