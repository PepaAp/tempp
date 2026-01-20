import pygame

class Entity:
    def __init__(self, pos, radius, color):
        self.pos = pygame.Vector2(pos)
        self.radius = radius
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)

    def collides_with(self, other):
        distance = self.pos.distance_to(other.pos)
        return distance < (self.radius + other.radius - 7)