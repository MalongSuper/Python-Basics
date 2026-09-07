import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))

player = pygame.Rect(50, 50, 50, 50)
goal = pygame.Rect(500, 300, 60, 60)

font = pygame.font.SysFont(None, 50)

won = False
running = True

while running:
    screen.fill((255, 255, 255))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.x -= 5

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.x += 5

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.y -= 5

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.y += 5

    pygame.draw.rect(screen, (0, 0, 255), player)
    pygame.draw.rect(screen, (255, 215, 0), goal)

    if player.colliderect(goal):
        won = True
    if won:
        text = font.render("YOU WIN!", True,(0, 150, 0))
        screen.blit(text, (180,150))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
