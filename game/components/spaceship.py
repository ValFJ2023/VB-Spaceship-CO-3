import pygame
from pygame.sprite import Sprite

from game.utils.constants import SPACESHIP, SCREEN_HEIGHT, SCREEN_WIDTH


class Spaceship(Sprite):
    SHIP_WIDTH = 40
    SHIP_HEIGHT = 60
    X_POS = (SCREEN_WIDTH // 2) - SHIP_WIDTH
    Y_POS = 500
    SHIP_SPEED = 10

    def __init__(self):
        self.image= SPACESHIP
        self.image = pygame.transform.scale(SPACESHIP,(60,40))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS

    def update(self, user_input):
        if user_input[pygame.K_LEFT]:
            self.move_left()
        elif user_input[pygame.K_RIGHT]:
            self.move_right()
        
        elif user_input[pygame.K_UP]:
            self.move_up()
        
        elif user_input[pygame.K_DOWN]:
            self.move_down()

    def move_left(self):
        self.rect.x -= self.SHIP_SPEED
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH
    
    def move_right(self):
        self.rect.x += self.SHIP_SPEED
        if self.rect.left > SCREEN_WIDTH:
            self.rect.right = 0
    
    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y -= self.SHIP_SPEED
    
    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - 70:
            self.rect.y += self.SHIP_SPEED
   
            

    def draw(self,screen):
        screen.blit(self.image,(self.rect.x, self.rect.y))