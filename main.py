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
old_x = 385
old_y = 620
width = 20
height = 25
character = pygame.Rect(x, y, width, height)
vel = 5
# Items
key_yellow = pygame.image.load('yellow_key.png')
# Walls
vertical_width = 40
vertical_height = 850
horizontal_height = 50
# Coordinates
left_wall = pygame.Rect(0, 0, vertical_width, vertical_height)
right_wall = pygame.Rect(760, 0, vertical_width, vertical_height)
south_left = pygame.Rect(0, 800, 325, horizontal_height)
south_right = pygame.Rect(460, 800, 340, horizontal_height)
north_left = pygame.Rect(0, 0, 165, horizontal_height)
north_right = pygame.Rect(620, 0, 180, horizontal_height)
south = pygame.Rect(0, 800, 800, horizontal_height)
north = pygame.Rect(0, 0, 800, horizontal_height)
# Room
room_number = 1
room_1 = [left_wall, right_wall, south_left, south_right, north_left, north_right]
room_2 = [south, north_left, north_right]
rooms = [0, room_1, room_2]


# Run until user asks to quit
running = True
while running:
    pygame.time.delay(30)

    # Did user click the close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    old_x = x
    old_y = y

    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    # Collisions
    character = pygame.Rect(x, y, width, height)
    for wall in rooms[room_number]:
        if pygame.Rect.colliderect(wall, character):
            x = old_x
            y = old_y

    # New room
    if (y > 825) and (room_number == 1):
        y = 20
        room_number = 2
    if (y < 5) and (room_number == 2):
        y = 800
        room_number = 1

    # Room properties
    if (room_number == 1):
        color = (200, 200, 0)
    if (room_number == 2):
        color = (0, 210, 70)

    # Draw
    screen.fill((150, 150, 150))

    if (room_number == 1):
        pygame.draw.rect(screen, color, left_wall)
        pygame.draw.rect(screen, color, right_wall)
    if (room_number == 1):
        pygame.draw.rect(screen, color, south_left)
        pygame.draw.rect(screen, color, south_right)
    pygame.draw.rect(screen, color, north_left)
    pygame.draw.rect(screen, color, north_right)
    if (room_number == 2):
        pygame.draw.rect(screen, color, south)

    pygame.draw.rect(screen, color, character)
    character = pygame.Rect(x, y, width, height)
    def yellow_key():
        screen.blit(key_yellow, (50, 50))
    pygame.display.flip()

# Quit
pygame.quit()
