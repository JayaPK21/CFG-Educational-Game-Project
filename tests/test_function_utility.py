import unittest
from unittest.mock import Mock
import pygame

from utils.function_utility import snake_movements, is_position_occupied      # Importing function to be tested
from classes.snake import Snake
from classes.value import Value


class TestCaseSnakeMovements(unittest.TestCase):

    def test_snake_moments_K_DOWN(self):
        # Preparing the mock event
        mock_event = Mock()
        mock_event.key = pygame.K_DOWN

        snake = Snake()
        # Calling the function
        snake_movements(mock_event, snake)

        #Asserts to check if snake has changed direction to move down.
        self.assertTrue((snake.xdir == 0) and (snake.ydir == 1))
    
    def test_snake_moments_K_UP(self):
        # Preparing the mock event
        mock_event = Mock()
        mock_event.key = pygame.K_UP

        snake = Snake()
        # Calling the function
        snake_movements(mock_event, snake)

        #Asserts to check if snake has changed direction to move up.
        self.assertTrue((snake.xdir == 0) and (snake.ydir == -1))
        
    def test_snake_moments_K_RIGHT(self):
        # Preparing the mock event
        mock_event = Mock()
        mock_event.key = pygame.K_RIGHT

        snake = Snake()
        # Calling the function
        snake_movements(mock_event, snake)

        #Asserts to check if snake has changed direction to move right.
        self.assertTrue((snake.xdir == 1) and (snake.ydir == 0))

    def test_snake_moments_K_LEFT(self):
        # Preparing the mock event
        mock_event = Mock()
        mock_event.key = pygame.K_LEFT

        snake = Snake()
        # Calling the function
        snake_movements(mock_event, snake)

        #Asserts to check if snake has changed direction to move left.
        self.assertTrue((snake.xdir == -1) and (snake.ydir == 0))


class TestCaseIsPositionOccupied(unittest.TestCase):

    def test_is_position_occupied_TRUE(self):
        new_value = Value(1)
        new_value.rect.x = 1
        new_value.rect.y = 2

        values = [Value(2), Value(3), Value(4)]
        values[0].rect.x = 3
        values[0].rect.y = 4

        values[1].rect.x = 1
        values[1].rect.y = 2

        values[2].rect.x = 5
        values[2].rect.y = 6

        self.assertTrue(is_position_occupied(new_value, values))

    def test_is_position_occupied_False(self):
        new_value = Value(1)
        new_value.rect.x = 1
        new_value.rect.y = 2

        values = [Value(2), Value(3), Value(4)]
        values[0].rect.x = 3
        values[0].rect.y = 4

        values[1].rect.x = 8
        values[1].rect.y = 7

        values[2].rect.x = 5
        values[2].rect.y = 6

        self.assertFalse(is_position_occupied(new_value, values))

