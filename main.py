# Import and initialize pygame library
import pygame
pygame.init()

# Window
screen = pygame.display.set_mode([800, 960])
pygame.display.set_caption("Adventure")

# Draw
color = (255, 255, 255)
x = 385
y = 620
width = 20
height = 25
character = pygame.Rect(x, y, width, height)
vel = 5
# Walls
vertical_width = 40
vertical_height = 850
horizontal_height = 50
left_wall = pygame.Rect(0, 0, vertical_width, vertical_height)
right_wall = pygame.Rect(760, 0, vertical_width, vertical_height)
south_left = pygame.Rect(0, 800, 325, horizontal_height)
south_right = pygame.Rect(460, 800, 325, horizontal_height)
north_left = pygame.Rect(0, 0, 165, horizontal_height)
north_right = pygame.Rect(620, 0, 165, horizontal_height)
# Room
room_1 = [left_wall, right_wall, south_left, south_right, north_left, north_right]
room_number = 1

# Run until user asks to quit
running = True
while running:
    pygame.time.delay(30)

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

    # Collisions
    if pygame.Rect.colliderect(left_wall, character):
        x += vel
    if pygame.Rect.colliderect(right_wall, character):
        x -= vel
    if pygame.Rect.colliderect(south_left, character) or pygame.Rect.colliderect(south_right, character):
        y -= vel
    if pygame.Rect.colliderect(north_left, character) or pygame.Rect.colliderect(north_right, character):
        y += vel

    # Draw
    screen.fill((150, 150, 150))

    pygame.draw.rect(screen, color, left_wall)
    pygame.draw.rect(screen, color, right_wall)
    pygame.draw.rect(screen, color, south_left)
    pygame.draw.rect(screen, color, south_right)
    pygame.draw.rect(screen, color, north_left)
    pygame.draw.rect(screen, color, north_right)

    pygame.draw.rect(screen, color, character)
    character = pygame.Rect(x, y, width, height)
    pygame.display.flip()

# Quit
pygame.quit()
