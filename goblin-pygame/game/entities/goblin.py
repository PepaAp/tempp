import pygame, math
from entities.entity import Entity
from core.constants import WIDTH, HEIGHT, GOBLIN_COLOR, GOBLIN_RADIUS, GOBLIN_SPEED

class Goblin(Entity):
    def __init__(self, world):
        self.speed = GOBLIN_SPEED
        self.world = world
        self.angle = 0.0
        
        pos = world.center + pygame.Vector2(world.radius, 0)
        super().__init__(pos=pos, radius=GOBLIN_RADIUS, color=GOBLIN_COLOR)

    def update(self, dt, player_pos):
        goblin_angle = self.angle
        target_angle = self.world.angle_to_point(player_pos)

        diff = target_angle - goblin_angle

        if diff > math.pi:
            diff -= 2*math.pi
        elif diff < -math.pi:
            diff += 2*math.pi

        max_turn = self.speed * dt

        if diff > max_turn:
            diff = max_turn
        elif diff < -max_turn:
            diff = -max_turn

        self.angle += diff

        self.pos = self.world.center + pygame.Vector2(
            self.world.radius * math.cos(self.angle),
            self.world.radius * math.sin(self.angle)
        )
            
        if self.angle > math.pi:
            self.angle -= 2 * math.pi
        elif self.angle < -math.pi:
            self.angle += 2 * math.pi

