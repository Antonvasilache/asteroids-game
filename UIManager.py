import pygame
from constants import *

class UIManager(pygame.sprite.Sprite):
    def __init__(self):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
            
        self.score = 0
        self.lives = 3 
        self.game_over = False
        self.font = pygame.font.Font('space_invaders.ttf', 24)
        self.large_font = pygame.font.Font('space_invaders.ttf', 48)
        
    def draw(self, screen):
        if not self.game_over:
            score_text = self.font.render(f"Score: {self.score}", True, (255,255,255))        
            screen.blit(score_text, (10, 10))
            
            lives_text = self.font.render(f"Lives: {self.lives}", True, (255,255,255))
            screen.blit(lives_text, (10, 50))
        else:
            game_over_text = self.large_font.render("GAME OVER", True, (255,255,255))
            score_text = self.font.render(f"Final score: {self.score}", True, (255,255,255))
            new_game_text = self.font.render("New Game", True, (255,255,255))
            
            screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - 100))
            screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2))
            screen.blit(new_game_text, (SCREEN_WIDTH // 2 - new_game_text.get_width() // 2, SCREEN_HEIGHT // 2 + 100))
            
            pygame.draw.rect(screen, (255,255,255), (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 95, 200, 40), 2)
            
    def check_new_game_click(self, pos):
        new_game_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 95, 200, 40)
        return new_game_rect.collidepoint(pos)
        
        