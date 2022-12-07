import pygame

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


player = character()
run = True
while run:
    screen.blit(backgroundImage, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    player.show()
    pygame.display.update()
