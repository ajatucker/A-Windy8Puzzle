#windy puzzle test cases
import unittest
from Windy8Puzzle import *

class Testing(unittest.TestCase):
    def test_initialGoal(self):
        goalInit = [1, 2, 3, 8, 0, 4, 7, 6, 5]
        stringVar = aStar(goalInit, goalInit)
        self.assertEqual(stringVar, "Goal found")
    def test_notGoal(self):
        goalInit = [1, 2, 3, 8, 0, 4, 7, 6, 5]
        notInit = [2, 8, 3, 6, 7, 4, 1, 5, 0]
        stringVar = aStar(notInit, goalInit)
        self.assertNotEqual(stringVar, "Goal found")

if __name__ == '__main__':
    unittest.main()
