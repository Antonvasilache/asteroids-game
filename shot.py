import circleshape
import pygame
from constants import *

class Shot(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = SHOT_RADIUS
        #self.velocity = 0        
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 0)
    
    def update(self, dt):
        self.position += self.velocity * dt