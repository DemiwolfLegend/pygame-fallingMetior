import pygame
import random

pygame.display.set_caption("firstGame")

screen = pygame.display.set_mode((800, 800))
backgroundImage = pygame.image.load("./content/background.png")


class character:
    def __init__(self) -> None:
        self.image = pygame.image.load("./content/player.png")
        self.x = 350
        self.y = 700
        self.change = 0

    def show(self):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.x += self.change
        if self.x < 0:
            self.x = 0
        elif self.x > 700:
            self.x = 700


class boulder:
    def __init__(self) -> None:
        self.image = pygame.image.load("./content/enemy.png")
        self.x = random.randint(0, 700)
        self.y = random.randint(-500, -100)
        self.change = 5

    def fall(self):
        self.y += self.change
        if self.y > 800:
            self.x = random.randint(0, 700)
            self.y = -100

    def show(self):
        screen.blit(self.image, (self.x, self.y))


player = character()
enemy = []
numFall = 10
for i in range(numFall):
    enemy.append(boulder())

run = True
while run:
    screen.blit(backgroundImage, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.change = -10
            elif event.key == pygame.K_RIGHT:
                player.change = 10
        elif event.type == pygame.KEYUP:
            player.change = 0

    player.move()
    for i in range(numFall):
        enemy[i].fall()
        enemy[i].show()

    player.show()
    pygame.display.update()
