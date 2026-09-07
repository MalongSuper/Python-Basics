# Drawing Shapes
import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Drawing Shapes")

running = True

while running:
    screen.fill((255, 255, 255))

    # Rectangle
    pygame.draw.rect(screen, (255, 0, 0), (50, 50, 100, 60))
    # Circle
    pygame.draw.circle(screen, (0, 0, 255), (300, 200), 50)
    # Line
    pygame.draw.line(screen, (0, 255, 0), (0, 0), (600, 400), 5)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
