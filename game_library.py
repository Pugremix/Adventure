# Import and initialize pygame library
import pygame
pygame.init()


# Classes

# Character (Holds all information about Character)
class Character:
    def __init__(self, x=375, y=420, old_x=375, old_y=420, width=20, height=25, room_number=1, item_held=None):
        self.x = x
        self.y = y
        self.old_x = old_x
        self.old_y = old_y
        self.width = width
        self.height = height
        self.room_number = room_number
        self.item_held = item_held
    def draw_character(self, screen, color):
        pygame.draw.rect(screen, color, pygame.Rect(self.x, self.y, self.width, self.height))
    def update_character(self):
        self.old_x = self.x
        self.old_y = self.y
    def hitdetect(self, rooms):
        self.character = pygame.Rect(self.x, self.y, self.width, self.height)
        for wall in rooms[self.room_number]:
            if pygame.Rect.colliderect(wall, self.character):
                self.move_back_character()
                if self.item_held != None:
                    self.item_held.move_back_item()
    def move_back_character(self):
        self.x = self.old_x
        self.y = self.old_y

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
    def draw_items(self, screen):
        screen.blit(self.image, (self.item_x, self.item_y))
    # Update
    def update_items(self):
        self.item_old_x = self.item_x
        self.item_old_y = self.item_y
    def move_back_item(self):
        self.item_x = self.item_old_x
        self.item_y = self.item_old_y

# Castles
class Castle:
    def __init__(self, image_name, gate_image):
        self.image = pygame.image.load(image_name)
        self.gate = pygame.image.load(gate_image)
    # Define
    def draw_castle(self, screen):
        screen.blit(self.gate, (365, 290))
        screen.blit(self.image, (185, 0))