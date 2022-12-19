import pygame
import random
from pygame import mixer

pygame.init()

pygame.display.set_caption("firstGame")

screen = pygame.display.set_mode((800, 800))
backgroundImage = pygame.image.load("./content/background.png")
# back_music = mixer.music.load("./content/background.wav")
# mixer.music.play(-1)


class Score:
    def __init__(self) -> None:
        self.font = pygame.font.Font("./content/Free_font.ttf", 32)
        self.current = 0
        self.x = 10
        self.y = 10
        # self.addon = False
        self.addon = True
        file = open("./content/score", 'r')
        self.high = file.read()
        file.close()

    def plus(self):
        if self.addon:
            self.current += 1
            self.check()

    def check(self):
        if int(self.high) < self.current:
            self.high = str(self.current)

    def save(self):
        file = open("./content/score", 'w')
        file.write(self.high)
        file.close()

    def show(self):
        a = self.font.render("Score :" + str(self.current), True, (255, 0, 0))
        b = self.font.render("High Score :" + self.high, True, (255, 0, 0))
        screen.blit(a, (self.x, self.y))
        screen.blit(b, (self.x, self.y+40))

    def over(self):
        a = self.font.render("Game Over", True, (255, 0, 0))
        screen.blit(a, (310, 400))


class Bullet:
    def __init__(self) -> None:
        self.image = pygame.image.load("./content/bullet.png")
        self.x = 800
        self.y = 700
        self.change = 10
        self.state = False

    def aim(self):
        self.x = player.x
        self.y = player.y
        self.state = True

    def show(self):
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


class Character:
    def __init__(self) -> None:
        self.image = pygame.image.load("./content/player.png")
        self.x = 350
        self.y = 700
        self.change = 0
        self.movement = 5
        self.bullet = Bullet()

    def show(self):
        if self.bullet.state:
            self.bullet.move()
            self.bullet.show()
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.x += self.change
        if self.x < 0:
            self.x = 0
        elif self.x > 700:
            self.x = 700


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

    def isColide(self):
        collison1 = self.y >= 600 and player.y > 0 and (
            self.x > (player.x-100) and self.x < (player.x+100))
        bullet = player.bullet
        collison2 = (bullet.y <= self.y+100) and (bullet.x >
                                                  (self.x-100) and bullet.x < (self.x+100))
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

    def show(self):
        screen.blit(self.image, (self.x, self.y))


player = Character()
score = Score()
enemy = []
numFall = 10
for i in range(numFall):
    enemy.append(Boulder())

run = True
while run:
    screen.blit(backgroundImage, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            score.save()
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.change = -player.movement
            elif event.key == pygame.K_RIGHT:
                player.change = player.movement
            elif event.key == pygame.K_SPACE:
                if not player.bullet.state:
                    player.bullet.aim()
        elif event.type == pygame.KEYUP:
            player.change = 0

    player.move()
    for i in range(numFall):
        enemy[i].fall()
        if enemy[i].isColide():
            break
        enemy[i].show()

    player.show()
    score.show()
    if not score.addon:
        score.over()
    pygame.display.update()
