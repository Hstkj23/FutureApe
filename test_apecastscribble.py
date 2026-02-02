# test_apecastscribble.py
"""
Tests for ApeCastScribble module.
"""

import unittest
from apecastscribble import ApeCastScribble

class TestApeCastScribble(unittest.TestCase):
    """Test cases for ApeCastScribble class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ApeCastScribble()
        self.assertIsInstance(instance, ApeCastScribble)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ApeCastScribble()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
