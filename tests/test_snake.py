import pygame
import unittest
from unittest.mock import Mock
from classes.snake import Snake
from utils.constants import BLOCK_SIZE, SW, SH

#python -m unittest discover tests

class TestSnake(unittest.TestCase):
    def setUp(self):
        pygame.init()  #Initialize pygame for testing
        self.snake = Snake()
    
    def Quit(self):
        pygame.quit()  #Quit pygame after testing
    
    def test_update_collision_with_itself(self):
        #Simulate collision with body segment at head position
        self.snake.body = [pygame.Rect(self.snake.x, self.snake.y, BLOCK_SIZE, BLOCK_SIZE)]
        self.snake.head = pygame.Rect(self.snake.x, self.snake.y, BLOCK_SIZE, BLOCK_SIZE)
        
        self.snake.update()
        self.assertTrue(self.snake.dead)  #Snake should be marked as dead
        self.assertEqual(self.snake.lives, 2)  #Lives should decrease by 1
        
    def test_update_collision_with_boundaries(self):
        #Simulate collision with right boundary
        self.snake.head.x = SW #Move head to the right boundary
        self.snake.update()
        self.assertTrue(self.snake.dead)  #Snake should be marked as dead
        self.assertEqual(self.snake.lives, 2)  #Lives should decrease by 1
        
        #Reset position
        self.snake.head.x = BLOCK_SIZE
        
        #Simulate collision with bottom boundary
        self.snake.head.y = SH #Move head to the bottom boundary
        self.snake.update()
        self.assertTrue(self.snake.dead)  #Snake should be marked as dead
        self.assertEqual(self.snake.lives, 1)  #Lives should decrease by 1
        
    def test_update_movement(self):
        initial_head_x = self.snake.head.x
        initial_head_y = self.snake.head.y
        
        self.snake.update()
        
        #Verify that the head has moved to the right
        self.assertEqual(self.snake.head.x, initial_head_x + BLOCK_SIZE)
        self.assertEqual(self.snake.head.y, initial_head_y)
        
        #Verify that the body segments have moved to follow the head
        for i in range(len(self.snake.body) - 1):
            self.assertEqual(self.snake.body[i].x, initial_head_x)
            self.assertEqual(self.snake.body[i].y, initial_head_y)
        
        #Verify that the last body segment has been removed
        self.assertNotIn(self.snake.head, self.snake.body)
    
    def test_reset_snake(self):
        self.snake.reset_snake()  #Reset the snake's attributes
        self.assertEqual(self.snake.x, BLOCK_SIZE)  #X position should reset
        self.assertEqual(self.snake.y, BLOCK_SIZE)  #Y position should reset
        self.assertEqual(self.snake.head, pygame.Rect(BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))  #Head rectangle should reset
        self.assertEqual(len(self.snake.body), 1)  #Body segments should reset
        self.assertEqual(self.snake.xdir, 1)  #X direction should reset
        self.assertEqual(self.snake.ydir, 0)  #Y direction should reset
        self.assertFalse(self.snake.dead)  #Snake should not be marked as dead
        