# Import and initialize pygame library
import pygame
pygame.init()

# Window
screen = pygame.display.set_mode([800, 960])
pygame.display.set_caption("Adventure")

# Fill background
screen.fill((150, 150, 150))

# Draw character
x = 375
y = 500
width = 40
height = 50
vel = 5

# Run until user asks to quit
running = True
while running:
    pygame.time.delay(40)

    # Did user click the close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    screen.fill((150, 150, 150))
    pygame.draw.rect(screen, (255, 255, 255), (x, y, width, height))
    pygame.display.flip()

# Quit
pygame.quit()
