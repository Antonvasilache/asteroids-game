import circleshape
import pygame
from constants import *

class PowerUp(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = 0        
        self.power_up_type = None       
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)
        font = pygame.font.Font('space_invaders.ttf', 24)
        if self.power_up_type == 'speed':
            label = 'S'
        elif self.power_up_type == 'shield':
            label = 'SH'
            
        text_surface = font.render(label, True, (255,255,255))
        text_rect = text_surface.get_rect(center=self.position)
        screen.blit(text_surface, text_rect)
        
    def update(self, dt):
        self.position += self.velocity * dt
        
        if self.position.x > SCREEN_WIDTH:
            self.position.x = 0            
        elif self.position.x < 0:
            self.position.x = SCREEN_WIDTH
            
        if self.position.y > SCREEN_HEIGHT:
            self.position.y = 0            
        elif self.position.y < 0:
            self.position.y = SCREEN_HEIGHT