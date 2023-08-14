import pygame
from utils.constants import BLOCK_SIZE, SW, SH

class Snake:
    def __init__(self):
        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE  # Initial position of the snake
        self.xdir = 1  # Initial movement direction (x-axis)
        self.ydir = 0  # Initial movement direction (y-axis)
        self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)  # Snake's head rectangle
        self.body = [pygame.Rect(self.x - BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]  # Snake's body segments
        self.lives = 6
        self.dead = False  # Flag indicating whether the snake is dead (hit itself or boundaries)

    def update(self):
        #global numbers
        for square in self.body:
            if self.head.x == square.x and self.head.y == square.y:
                self.dead = True  # Check if snake collided with itself
                self.lives -= 1
                print(self.lives)

        if self.head.x not in range(0, SW) or self.head.y not in range(BLOCK_SIZE, SH):
            self.dead = True  # Check if snake hit the game boundaries
            self.lives -= 1
            print(self.lives)
        
        if self.dead:
            return

        # Move the snake's body and head
        self.body.append(self.head)
        for i in range(len(self.body) - 1):
            self.body[i].x, self.body[i].y = self.body[i + 1].x, self.body[i + 1].y
        self.head.x += self.xdir * BLOCK_SIZE
        self.head.y += self.ydir * BLOCK_SIZE
        self.body.remove(self.head)

    def reset_snake(self):
        # Reset snake's position and attributes
        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        self.body = [pygame.Rect(self.x - BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
        self.xdir = 1
        self.ydir = 0
        self.dead = False

