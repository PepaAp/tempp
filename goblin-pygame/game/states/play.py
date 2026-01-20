import time, pygame
from world.world import World
from entities.player import Player
from entities.goblin import Goblin
from core.constants import WIDTH, HEIGHT, TIMER_COLOR, TIMER_SIZE, PLAYER_RADIUS

class PlayState:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game
        self.world = World()
        self.player = Player(self.world)
        self.goblin = Goblin(self.world)

        self.escaped = False
        self.start_time = time.time()
        self.dead = False
        self.dead_time = 0

    def update(self, dt):
        self.game.handle_controlls()
        
        if self.dead:
            if time.time() - self.dead_time > 2:
                self.game.restart()
            return
        if self.escaped:
            if time.time() - self.dead_time > 2:
                self.game.restart()
            return

        self.player.handle_input(dt)
        self.goblin.update(dt, self.player.pos)

        if self.player.collides_with(self.goblin):
            self.dead = True
            self.dead_time = time.time()

        if self.world.has_escaped_lake(self.player.pos, buffer = 0):
            self.escaped = True
            self.dead_time = time.time()

    def draw(self):
        self.world.draw(self.screen)
        self.player.draw(self.screen)
        self.goblin.draw(self.screen)

        if not self.escaped and not self.dead:
            elapsed = time.time() - self.start_time
        else:
            elapsed = self.dead_time - self.start_time

        font = pygame.font.SysFont(None, TIMER_SIZE)
        text = font.render(f"Time: {elapsed:.1f} sec.", True, TIMER_COLOR)
        self.screen.blit(text, (10, 10))
        
        if self.dead:
            font = pygame.font.SysFont(None, 60)
            text = font.render("YOU HAVE BEEN CAUGHT", True, (255, 20, 20))
            rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            self.screen.blit(text, rect)

        if self.escaped:
            font = pygame.font.SysFont(None, 60)
            text = font.render("YOU ESCAPED!", True, (255, 215, 0))
            rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            self.screen.blit(text, rect)