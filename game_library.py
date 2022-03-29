# Import and initialize pygame library
import pygame
pygame.init()

# Classes
# Character (Holds all information about Character)
class Character:
    def __init__(self, x=385, y=620, old_x=385, old_y=620, width=20, height=25, room_number=1, item_held=None):
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
