import pygame
from score import Score
import unittest
from unittest import mock
from unittest import TestCase, main
import utils.constants



class TestScore(unittest.TestCase):

    def setUp(self):
        self.score = Score()

    def test_initial_value(self):
        self.assertEqual(self.score.value, 0, "Initial score value should be 0")

    def test_increase(self):
        initial_value = self.score.value
        self.score.increase()
        self.assertEqual(self.score.value, initial_value + 1, "Score value should increase by 1")


if __name__ == "__main__":
    unittest.main()