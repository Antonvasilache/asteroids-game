import pygame

class UIManager(pygame.sprite.Sprite):
    def __init__(self):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
            
        self.score = 0
        self.lives = 3 
        
    def draw(self, screen):
        font = pygame.font.Font('space_invaders.ttf', 24)
        score_text = font.render(f"Score: {self.score}", True, (255,255,255))        
        screen.blit(score_text, (10, 10))
        
        lives_text = font.render(f"Lives: {self.lives}", True, (255,255,255))
        screen.blit(lives_text, (10, 50))
        
        