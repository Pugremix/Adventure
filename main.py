# Import and initialize pygame library
import pygame
pygame.init()

# Window
screen = pygame.display.set_mode([800, 960])
pygame.display.set_caption("Adventure")

# Draw
color = (255, 255, 255)
x = 375
y = 500
width = 20
height = 25
vel = 5
# Walls
vertical_width = 40
vertical_height = 850
horizontal_width = 700
horizontal_height = 50
left_wall = (0, 0, vertical_width, vertical_height)
right_wall = (760, 0, vertical_width, vertical_height)

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
    pygame.draw.rect(screen, color, left_wall)
    pygame.draw.rect(screen, color, right_wall)
    pygame.draw.rect(screen, color, (x, y, width, height))
    pygame.display.flip()

# Quit
pygame.quit()
