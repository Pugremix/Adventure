# Import and initialize libraries
import pygame
import game_library
import sys

pygame.init()

#Greg Pringle - needed to add this function to build .exe for Mr. Manning
if getattr(sys, 'frozen', False):  #change directory to temp unpack folder if run from single compressed application
    os.chdir(sys._MEIPASS)


# Window
screen = pygame.display.set_mode([800, 750])
pygame.display.set_caption("Adventure")

# Objects
# All
color = (255, 255, 255)
vel = 5
# Character (Retrieves information about Character from the game library)
player = game_library.Character()
# Load images
key_yellow = game_library.Item('yellow_key.png', 1, 120, 205, 120, 205)
yellow_castle = game_library.Castle('yellow_castle.png', 'Gate.png', 1)
# Walls
# General
vertical_width = 40
vertical_height = 750
horizontal_height = 50
full_length = 700
# Coordinates
# Opening walls
south_left = pygame.Rect(0, full_length, 300, horizontal_height)
south_right = pygame.Rect(465, full_length, 340, horizontal_height)
north_left = pygame.Rect(0, 0, 300, horizontal_height)
north_right = pygame.Rect(465, 0, 340, horizontal_height)
# Full walls
left_wall = pygame.Rect(0, 0, vertical_width, vertical_height)
right_wall = pygame.Rect(760, 0, vertical_width, vertical_height)
south = pygame.Rect(0, full_length, 800, horizontal_height)
north = pygame.Rect(0, 0, 800, horizontal_height)
# Castle walls
towers = pygame.Rect(185, 25, 400, 185)
castle_left = pygame.Rect(225, 210, 120, 160)
castle_right = pygame.Rect(425, 210, 120, 160)
gate = pygame.Rect(345, 290, 80, 80)
# Rooms
room_0 = [left_wall, right_wall, north, south_left, south_right]
room_1 = [left_wall, right_wall, south_left, south_right, north_left, north_right, towers, castle_left, castle_right, gate]
room_2 = [south, north_left, north_right]
room_3 = [north, south_left, south_right]
room_4 = [south, north_left, north_right]
rooms = [room_0, room_1, room_2, room_3, room_4]


# Run until user asks to quit loop
running = True
while running:
    pygame.time.delay(25)

    # Did user click the close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Update Character position
    player.update_character()
    # Yellow Key
    draw_yellow = pygame.Rect(key_yellow.item_x, key_yellow.item_y, 40, 15)
    key_yellow.update_items()

    if keys[pygame.K_LEFT]:
        player.x -= vel
        if player.item_held != None:
            player.item_held.item_x -= vel
    if keys[pygame.K_RIGHT]:
        player.x += vel
        if player.item_held != None:
            player.item_held.item_x += vel
    if keys[pygame.K_UP]:
        player.y -= vel
        if player.item_held != None:
            player.item_held.item_y -= vel
    if keys[pygame.K_DOWN]:
        player.y += vel
        if player.item_held != None:
            player.item_held.item_y += vel
    if keys[pygame.K_SPACE]:
        player.item_held = None

    # Collisions
    player.hitdetect(rooms)

    # New room
    # Yellow Castle
    if (player.y < 300) and (345 < player.x < 425) and (player.room_number == 1):
        player.y = 705
        player.room_number = 0
        if player.item_held != None:
            player.item_held.item_y += 410
            player.item_held.item_room = 0
    if (player.y > 725) and (player.room_number == 0):
        player.y = 320
        player.x = 375
        player.room_number = 1
        if player.item_held != None:
            player.item_held.item_y -= 410
            player.item_held.item_x += player.x - player.old_x
            player.item_held.item_room = 1

    if (player.y > 725) and (player.room_number == 1):
        player.y = 20
        player.room_number = 2
        if player.item_held != None:
            player.item_held.item_y -= 710
            player.item_held.item_room = 2
    if (player.y < 0) and (player.room_number == 2):
        player.y = 705
        player.room_number = 1
        if player.item_held != None:
            player.item_held.item_y += 710
            player.item_held.item_room = 1
    if (player.x > 780) and (player.room_number == 2):
        player.x = 20
        player.room_number = 3
        if player.item_held != None:
            player.item_held.item_x -= 765
            player.item_held.item_room = 3
    if (player.x < 0) and (player.room_number == 3):
        player.x = 760
        player.room_number = 2
        if player.item_held != None:
            player.item_held.item_x += 765
            player.item_held.item_room = 2
    if (player.x < 0) and (player.room_number == 2):
        player.x = 760
        player.room_number = 4
        if player.item_held != None:
            player.item_held.item_x += 765
            player.item_held.item_room = 4
    if (player.x > 780) and (player.room_number == 4):
        player.x = 20
        player.room_number = 2
        if player.item_held != None:
            player.item_held.item_x -= 765
            player.item_held.item_room = 2

    # Room properties
    if (player.room_number == 0):
        color = (200, 200, 0)
    if (player.room_number == 1):
        color = (200, 200, 0)
    if (player.room_number == 2):
        color = (0, 210, 70)
    if (player.room_number == 3):
        color = (130, 150, 50)
    if (player.room_number == 4):
        color = (100, 175, 50)

    # Draw
    # Background
    screen.fill((150, 150, 150))
    # Draw room loop
    for walls in rooms[player.room_number]:
        if (walls != gate):
            pygame.draw.rect(screen, color, walls)

    # Draw Character
    player.draw_character(screen, color)

    # Foreground
    # Draw Castles
    if (player.room_number == 1):
        yellow_castle.draw_castle(screen)

    # Draw Items
    if (player.room_number == key_yellow.item_room):
        key_yellow.draw_items(screen)
    if (player.room_number == key_yellow.item_room) and pygame.Rect.colliderect(draw_yellow, player.character):
        player.item_held = key_yellow
        key_yellow.item_x += player.x - player.old_x
        key_yellow.item_y += player.y - player.old_y

    pygame.display.flip()

# Quit
pygame.quit()
