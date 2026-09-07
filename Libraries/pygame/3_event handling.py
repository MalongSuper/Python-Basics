# Event Handling
import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))

x = 250
y = 150
speed = 5

running = True

while running:
    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x -= speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x += speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y -= speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y += speed

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
