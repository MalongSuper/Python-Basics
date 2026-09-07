# Working with Text
import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
font = pygame.font.SysFont("Arial", 36)

running = True

while running:
    screen.fill((255, 255, 255))

    text = font.render("Welcome to PyGame!", True,(0, 0, 255))
    screen.blit(text, (150, 180))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
