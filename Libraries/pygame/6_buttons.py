import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))

x = 250
y = 250

button = pygame.Rect(230, 50, 140, 50)

running = True

while running:
    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))
    pygame.draw.rect(screen, (0, 200, 0), button)

    font = pygame.font.SysFont(None, 30)

    text = font.render("Jump", True, (255, 255, 255))
    screen.blit(text, (270, 65))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(event.pos):
                y -= 100

    pygame.display.update()

pygame.quit()
