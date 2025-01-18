import pygame

from assets.bullet import Bullet


class Character:
    def __init__(self) -> None:
        self.image = pygame.image.load("./content/player.png")
        self.x = 350
        self.y = 700
        self.change = 0
        self.movement = 5
        self.bullet = Bullet()

    def show(self, screen):
        if self.bullet.state:
            self.bullet.move()
            self.bullet.show(screen)
        screen.blit(self.image, (self.x, self.y))

    def move(self, score):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                score.save()
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.change = -self.movement
                elif event.key == pygame.K_RIGHT:
                    self.change = self.movement
                elif event.key == pygame.K_SPACE:
                    if not self.bullet.state:
                        self.bullet.aim(self)
            elif event.type == pygame.KEYUP:
                self.change = 0

        self.x += self.change
        if self.x < 0:
            self.x = 0
        elif self.x > 700:
            self.x = 700
        return True

