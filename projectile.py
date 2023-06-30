import pygame

class Projectile:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
    
    def move(self):
        self.y -= self.speed
    
    def draw(self, window):
        pygame.draw.rect(window, (0, 255, 0), (self.x, self.y, self.width, self.height))
