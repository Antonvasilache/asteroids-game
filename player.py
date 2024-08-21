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
        self.thrust = 0
        self.max_thrust = 1.5
        self.acceleration_rate = 0.05
        self.deceleration_rate = 0.02        
    
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
        
    def handle_input(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.increase_thrust()
            self.move(dt)
        else:
            self.decrease_thrust()
            self.move(dt)        
        if keys[pygame.K_s]:
            self.decrease_thrust()
        if keys[pygame.K_SPACE] and self.shot_timer <= 0:           
            self.shoot()
            self.shot_timer = PLAYER_SHOT_COOLDOWN
        
    def update(self, dt):
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w: 
                    print("W key released")                      
        
        if self.immunity_timer > 0:
            self.immunity_timer -= dt    
          
        self.handle_input(dt)  
        self.shot_timer -= dt
            
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * self.thrust * dt
        
    def increase_thrust(self):
        if self.thrust < self.max_thrust:
            self.thrust += self.acceleration_rate
            
    def decrease_thrust(self):
        if self.thrust > 0:
            self.thrust -= self.deceleration_rate        
        
    def shoot(self):        
        new_shot = shot.Shot(self.position.x, self.position.y, SHOT_RADIUS)
        new_shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED
        
    def respawn(self):
        self.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.immunity_timer = 2
        
        