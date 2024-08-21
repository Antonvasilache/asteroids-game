import pygame
import player
import asteroid
import asteroidfield
import shot
import UIManager
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    dt = 0
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    player.Player.containers = (updatable, drawable)
    new_player = player.Player(x, y)
    
    asteroids = pygame.sprite.Group()
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = updatable
    asteroid_field = asteroidfield.AsteroidField()
    
    shots = pygame.sprite.Group()
    shot.Shot.containers = (updatable, drawable, shots)
    
    UIManager.UIManager.containers = drawable
    ui_manager = UIManager.UIManager()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0,0,0))
        for item in updatable:
            item.update(dt)
            
        for new_asteroid in asteroids:
            for new_shot in shots:
                if new_shot.check_collision(new_asteroid):
                    new_shot.kill()
                    new_asteroid.split()
                    ui_manager.score += 1                    
                    
            if (
                new_asteroid.check_collision(new_player) 
                and new_player.immunity_timer <= 0 
                and new_asteroid.radius >= ASTEROID_MIN_RADIUS
                ):
                if ui_manager.lives > 1:
                    ui_manager.lives -= 1
                    new_player.respawn()
                else:                                    
                    print("Game over!")
                    return
                
        for item in drawable:
            item.draw(screen)
            
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
    
    
if __name__ == "__main__":
    main()

