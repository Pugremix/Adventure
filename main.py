# Import and initialize libraries
import pygame
pygame.init()
import game_library

# Window
screen = pygame.display.set_mode([800, 960])
pygame.display.set_caption("Adventure")

# Objects
# All
color = (255, 255, 255)
vel = 5
# Character (Retrieves information about Character from the game library)
player = game_library.Character()
# Items (Holds all information about in-game items)
class Item:
    def __init__(self, image_name, item_room, item_x, item_y, item_old_x, item_old_y):
        self.image = pygame.image.load(image_name)
        self.item_room = item_room
        self.item_x = item_x
        self.item_y = item_y
        self.item_old_x = item_old_x
        self.item_old_y = item_old_y
    # Define
    def draw_items(self):
        screen.blit(self.image, (self.item_x, self.item_y))
    # Update
    def update_items(self):
        self.item_old_x = self.item_x
        self.item_old_y = self.item_y
    def move_back_item(self):
        self.item_x = self.item_old_x
        self.item_y = self.item_old_y
# Load images
key_yellow = Item('yellow_key.png', 1, 100, 175, 100, 175)
# Walls
# General
vertical_width = 40
vertical_height = 850
horizontal_height = 50
# Coordinates
# Opening walls
south_left = pygame.Rect(0, 800, 325, horizontal_height)
south_right = pygame.Rect(460, 800, 340, horizontal_height)
north_left = pygame.Rect(0, 0, 325, horizontal_height)
north_right = pygame.Rect(460, 0, 340, horizontal_height)
# Full walls
left_wall = pygame.Rect(0, 0, vertical_width, vertical_height)
right_wall = pygame.Rect(760, 0, vertical_width, vertical_height)
south = pygame.Rect(0, 800, 800, horizontal_height)
north = pygame.Rect(0, 0, 800, horizontal_height)
# Rooms
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

    # Update Character position
    player.update_character()
    # Yellow Key
    draw_yellow = pygame.Rect(key_yellow.item_x, key_yellow.item_y, 40, 15)
    key_yellow.update_items()

    if keys[pygame.K_LEFT]:
        player.x -= vel
        if player.item_held == key_yellow:
            key_yellow.item_x -= vel
    if keys[pygame.K_RIGHT]:
        player.x += vel
        if player.item_held == key_yellow:
            key_yellow.item_x += vel
    if keys[pygame.K_UP]:
        player.y -= vel
        if player.item_held == key_yellow:
            key_yellow.item_y -= vel
    if keys[pygame.K_DOWN]:
        player.y += vel
        if player.item_held == key_yellow:
            key_yellow.item_y += vel
    if keys[pygame.K_SPACE]:
        player.item_held = None

    # Collisions
    player.item_held
    player.hitdetect(rooms)

    # New room
    if (player.y > 825) and (player.room_number == 1):
        player.y = 20
        player.room_number = 2
        if player.item_held == key_yellow:
            key_yellow.item_y -= 810
            key_yellow.item_room = 2
    if (player.y < 0) and (player.room_number == 2):
        player.y = 800
        player.room_number = 1
        if player.item_held == key_yellow:
            key_yellow.item_y += 805
            key_yellow.item_room = 1
    if (player.x > 780) and (player.room_number == 2):
        player.x = 20
        player.room_number = 3
        if player.item_held == key_yellow:
            key_yellow.item_x -= 765
            key_yellow.item_room = 3
    if (player.x < 0) and (player.room_number == 3):
        player.x = 760
        player.room_number = 2
        if player.item_held == key_yellow:
            key_yellow.item_x += 765
            key_yellow.item_room = 2
    if (player.x < 0) and (player.room_number == 2):
        player.x = 760
        player.room_number = 4
        if player.item_held == key_yellow:
            key_yellow.item_x += 765
            key_yellow.item_room = 4
    if (player.x > 780) and (player.room_number == 4):
        player.x = 20
        player.room_number = 2
        if player.item_held == key_yellow:
            key_yellow.item_x -= 765
            key_yellow.item_room = 2

    # Room properties
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
        pygame.draw.rect(screen, color, walls)
    # Draw Character
    player.draw_character(screen, color)

    if (player.room_number == key_yellow.item_room):
        key_yellow.draw_items()
    if (player.room_number == key_yellow.item_room) and pygame.Rect.colliderect(draw_yellow, player.character):
        player.item_held = key_yellow
        key_yellow.item_x += player.x - player.old_x
        key_yellow.item_y += player.y - player.old_y

    pygame.display.flip()

# Quit
pygame.quit()
