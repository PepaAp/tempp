import pygame
from core.constants import *
from states.play import PlayState

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Escape THE Goblin")
        self.clock = pygame.time.Clock()
        self.running = True

        self.state = PlayState(self.screen, self)

    def run(self):
        while self.running:
            dt = self.clock.tick(FPS) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.state.update(dt)

            self.screen.fill(BG_COLOR)
            self.state.draw()
            self.handle_controlls_information()
            pygame.display.flip()

        pygame.quit()
        
    def handle_controlls_information(self):
        font = pygame.font.SysFont(None, 35)
        text = font.render("Move with mouse while holding left button.", True, (255, 255, 255))
        text2 = font.render("Use \"R\" or \"SPACE\" to restart.", True, (255, 255, 255))
        rect = text.get_rect(center=(WIDTH // 2, 45))
        rect2 = text2.get_rect(center=(WIDTH // 2, 70))
        self.screen.blit(text, rect)
        self.screen.blit(text2, rect2)

    def restart(self):
        self.state = PlayState(self.screen, self)
        
    def handle_controlls(self):
        if (pygame.key.get_pressed()[pygame.K_r] or 
            pygame.key.get_pressed()[pygame.K_SPACE]):
            self.restart()