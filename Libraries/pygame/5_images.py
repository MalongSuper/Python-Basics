# Working with Images
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
player = pygame.image.load("player.png")

running = True

while running:
    screen.fill((255, 255, 255))
    screen.blit(player, (100, 50))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
