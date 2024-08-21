import circleshape
import pygame
import random
from constants import *

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = 0
        self.particle_timer = 0
        
    def draw(self, screen):
        if self.particle_timer == 0 or (self.particle_timer > 0.1 and int(pygame.time.get_ticks() * 0.005) % 2 == 0):
            pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
        if self.particle_timer > 0.1:
            self.particle_timer -= dt
        
    def split(self):
        self.explode()
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            new_vector_1 = self.velocity.rotate(angle)
            new_vector_2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_1.velocity = new_vector_1 * 1.2
            new_asteroid_2.velocity = new_vector_2 * 1.2
            
    def explode(self):        
        number_of_particles = random.randint(3, 6)
        for _ in range(number_of_particles):
            angle = random.uniform(0, 360)
            velocity_coefficient = random.uniform(0.8, 1.6)
            new_vector = self.velocity.rotate(angle)
            new_particle = Asteroid(self.position.x, self.position.y, PARTICLE_RADIUS)
            new_particle.velocity = new_vector * velocity_coefficient
            new_particle.particle_timer = random.randint(1, 2)