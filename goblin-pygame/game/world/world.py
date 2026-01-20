import pygame, math
from core.constants import WIDTH,HEIGHT,WATER_COLOR

class World:
    def __init__(self):
        self.center = pygame.Vector2(WIDTH//2, HEIGHT//2)
        self.radius = 300
    
    def draw(self, screen):
        pygame.draw.circle(
            screen,
            WATER_COLOR,
            self.center,
            self.radius
            )
        
    def lake_stuck_position(self, pos, buffer=0):
        direction = pos - self.center
        distance = direction.length()

        if distance > self.radius - buffer:
            direction.scale_to_length(self.radius - buffer)
            return self.center + direction
        return pos
    
    def has_escaped_lake(self, pos, buffer=0):
        direction = pos - self.center
        distance = direction.length()
        return distance > self.radius - buffer
    
    def angle_to_point(self, pos):
        direction = pos-self.center
        return math.atan2(direction.y, direction.x)