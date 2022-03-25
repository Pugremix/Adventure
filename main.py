# Import and initialize pygame library
import pygame
pygame.init()

# Window
screen = pygame.display.set_mode([800, 960])
pygame.display.set_caption("Adventure")

# Draw
# Character
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
item_held = 0
class Item:
    def __init__(self, image_name, item_room, item_x, item_y, item_old_x, item_old_y):
        self.image = pygame.image.load(image_name)
        self.item_room = item_room
        self.item_x = item_x
        self.item_y = item_y
        self.item_old_x = item_old_x
        self.item_old_y = item_old_y
# Yellow Key
key_yellow = Item('yellow_key.png', 1, 100, 175, 100, 175)
# Walls
vertical_width = 40
vertical_height = 850
horizontal_height = 50
# Coordinates
south_left = pygame.Rect(0, 800, 325, horizontal_height)
south_right = pygame.Rect(460, 800, 340, horizontal_height)
north_left = pygame.Rect(0, 0, 325, horizontal_height)
north_right = pygame.Rect(460, 0, 340, horizontal_height)
# Barriers
left_wall = pygame.Rect(0, 0, vertical_width, vertical_height)
right_wall = pygame.Rect(760, 0, vertical_width, vertical_height)
south = pygame.Rect(0, 800, 800, horizontal_height)
north = pygame.Rect(0, 0, 800, horizontal_height)
# Room
room_number = 1
room_1 = [left_wall, right_wall, south_left, south_right, north_left, north_right]
room_2 = [south, north_left, north_right]
room_3 = [north, south_left, south_right]
room_4 = [south, north_left, north_right]
rooms = [0, room_1, room_2, room_3, room_4]


# Run until user asks to quit loop
running = True
while running:
    pygame.time.delay(30)

    # Did user click the close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Character
    old_x = x
    old_y = y
    # Yellow Key
    draw_yellow = pygame.Rect(key_yellow.item_x, key_yellow.item_y, 40, 15)
    key_yellow.item_old_x = key_yellow.item_x
    key_yellow.item_old_y = key_yellow.item_y

    if keys[pygame.K_LEFT]:
        x -= vel
        if item_held == 1:
            key_yellow.item_x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
        if item_held == 1:
            key_yellow.item_x += vel
    if keys[pygame.K_UP]:
        y -= vel
        if item_held == 1:
            key_yellow.item_y -= vel
    if keys[pygame.K_DOWN]:
        y += vel
        if item_held == 1:
            key_yellow.item_y += vel
    if keys[pygame.K_SPACE]:
        item_held = 0

    # Collisions
    character = pygame.Rect(x, y, width, height)
    for wall in rooms[room_number]:
        if pygame.Rect.colliderect(wall, character):
            x = old_x
            y = old_y
            if item_held == 1:
                key_yellow.item_x = key_yellow.item_old_x
                key_yellow.item_y = key_yellow.item_old_y

    # New room
    if (y > 825) and (room_number == 1):
        y = 20
        room_number = 2
        if item_held == 1:
            key_yellow.item_y -= 810
            key_yellow.item_room = 2
    if (y < 0) and (room_number == 2):
        y = 800
        room_number = 1
        if item_held == 1:
            key_yellow.item_y += 805
            key_yellow.item_room = 1
    if (x > 780) and (room_number == 2):
        x = 20
        room_number = 3
        if item_held == 1:
            key_yellow.item_x -= 765
            key_yellow.item_room = 3
    if (x < 0) and (room_number == 3):
        x = 760
        room_number = 2
        if item_held == 1:
            key_yellow.item_x += 765
            key_yellow.item_room = 2
    if (x < 0) and (room_number == 2):
        x = 760
        room_number = 4
        key_yellow.item_x += 765
        key_yellow.item_room = 4
    if (x > 780) and (room_number == 4):
        x = 20
        room_number = 2
        if item_held == 1:
            key_yellow.item_x -= 765
            key_yellow.item_room = 2

    # Room properties
    if (room_number == 1):
        color = (200, 200, 0)
    if (room_number == 2):
        color = (0, 210, 70)
    if (room_number == 3):
        color = (130, 150, 50)
    if (room_number == 4):
        color = (100, 175, 50)

    # Define
    def the_yellow_key(yellow_key_x, yellow_key_y):
        screen.blit(key_yellow.image, (yellow_key_x, yellow_key_y))

    # Draw
    screen.fill((150, 150, 150))

    # Draw room loop
    for walls in rooms[room_number]:
        pygame.draw.rect(screen, color, walls)

    pygame.draw.rect(screen, color, character)
    character = pygame.Rect(x, y, width, height)
    if (room_number == key_yellow.item_room):
        the_yellow_key(key_yellow.item_x, key_yellow.item_y)
    if (room_number == key_yellow.item_room) and pygame.Rect.colliderect(draw_yellow, character):
        item_held = 1
        key_yellow.item_x += x - old_x
        key_yellow.item_y += y - old_y

    pygame.display.flip()

# Quit
pygame.quit()
