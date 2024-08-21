import circleshape
import pygame
import shot
from constants import *

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        
        self.position = pygame.Vector2(x, y)
        self.rotation = 0
        self.radius = PLAYER_RADIUS     
        self.shot_timer = 0  
        self.immunity_timer = 0        
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        if self.immunity_timer <= 0 or int(pygame.time.get_ticks() * 0.005) % 2 == 0:
            pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)
        
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        
    def update(self, dt):
        if self.immunity_timer > 0:
            self.immunity_timer -= dt
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.shot_timer <= 0:
                self.shoot()
                self.shot_timer = PLAYER_SHOT_COOLDOWN
            
        self.shot_timer -= dt
            
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        
    def shoot(self):        
        new_shot = shot.Shot(self.position.x, self.position.y, SHOT_RADIUS)
        new_shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED
        
    def respawn(self):
        self.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.immunity_timer = 2
        
        