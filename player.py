import pygame

class Player:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
    
    def move_left(self):
        self.x -= self.speed
    
    def move_right(self):
        self.x += self.speed
    
    def draw(self, window):
        pygame.draw.rect(window, (0, 0, 255), (self.x, self.y, self.width, self.height))
