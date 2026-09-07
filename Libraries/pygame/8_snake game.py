import pygame
import random

pygame.init()

# Window Setup
WIDTH = 600
HEIGHT = 400
BLOCK = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Fonts
font = pygame.font.SysFont("Arial", 25)
score_font = pygame.font.SysFont("Arial", 20)


def run_game():
    # Game variables reset
    x = WIDTH // 2
    y = HEIGHT // 2
    dx = BLOCK
    dy = 0
    snake = []
    length = 1

    food_x = random.randrange(0, WIDTH, BLOCK)
    food_y = random.randrange(0, HEIGHT, BLOCK)

    game_active = True
    game_over = False

    while game_active:

        # Game over loop
        while game_over:
            screen.fill(WHITE)
            text = font.render("Game Over! Press C to Play Again "
                               "or Q to Quit", True, RED)
            screen.blit(text, [WIDTH // 12, HEIGHT // 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False  # Exit completely
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        return False  # Quit the game
                    if event.key == pygame.K_c:
                        return True  # Restart the game loop

        # Event Handling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_active = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_active = False
                elif event.key in [pygame.K_LEFT, pygame.K_a]:
                    dx = -BLOCK
                    dy = 0
                elif event.key in [pygame.K_RIGHT, pygame.K_d]:
                    dx = BLOCK
                    dy = 0
                elif event.key in [pygame.K_UP, pygame.K_w]:
                    dy = -BLOCK
                    dx = 0
                elif event.key in [pygame.K_DOWN, pygame.K_s]:
                    dy = BLOCK
                    dx = 0

        # Movement updates
        x += dx
        y += dy

        # Wall Collision Checks
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            print("Game Over!!")
            game_over = True

        screen.fill(WHITE)

        # Draw Food
        pygame.draw.rect(screen, GREEN, (food_x, food_y, BLOCK, BLOCK))

        # Snake growth tracking
        head = [x, y]
        snake.append(head)
        if len(snake) > length:
            snake.pop(0)

        # Self-Collision Checks
        for part in snake[:-1]:
            if part == head:
                print("Game Over!!")
                game_over = True

        # Draw Snake
        for part in snake:
            pygame.draw.rect(screen, BLACK, (part[0], part[1], BLOCK, BLOCK))

        # Food eating check
        if x == food_x and y == food_y:
            food_x = random.randrange(0, WIDTH, BLOCK)
            food_y = random.randrange(0, HEIGHT, BLOCK)
            length += 1

        # Draw Score in Top Left
        score = length - 1
        score_text = score_font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, [10, 10])

        pygame.display.update()
        clock.tick(10)

    return False


# Main Execution Loop
running = True
while running:
    running = run_game()

pygame.quit()
