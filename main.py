# Import and initialize the pygame library
import pygame
pygame.init()

# Window
screen = pygame.display.set_mode([900, 700])
pygame.display.set_caption("Adventure")

# Run until the user asks to quit
running = True
while running:

    # Did the user click the close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background
    screen.fill((150, 150, 150))

    # Draw
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Flip display
    pygame.display.flip()

# Quit
pygame.quit()
