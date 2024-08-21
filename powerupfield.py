import pygame
import random
from powerup import PowerUp
from constants import *

class PowerUpField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-POWER_UP_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + POWER_UP_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -POWER_UP_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + POWER_UP_RADIUS
            ),
        ],
    ]
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0
    
    def spawn(self, position, velocity, type):        
        powerup = PowerUp(position.x, position.y, POWER_UP_RADIUS)
        powerup.velocity = velocity
        powerup.power_up_type = type
        
    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > POWER_UP_SPAWN_RATE:
            self.spawn_timer = 0
            
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0,1))
            type = random.choice(['speed', 'shield'])
            self.spawn(position, velocity, type)
        
        