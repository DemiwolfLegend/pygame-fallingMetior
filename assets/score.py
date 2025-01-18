import pygame


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

    def show(self,screen):
        a = self.font.render("Score :" + str(self.current), True, (255, 0, 0))
        b = self.font.render("High Score :" + self.high, True, (255, 0, 0))
        screen.blit(a, (self.x, self.y))
        screen.blit(b, (self.x, self.y+40))

    def over(self, screen):
        a = self.font.render("Game Over", True, (255, 0, 0))
        screen.blit(a, (310, 400))

