# test_primeswap.py
"""
Tests for PrimeSwap module.
"""

import unittest
from primeswap import PrimeSwap

class TestPrimeSwap(unittest.TestCase):
    """Test cases for PrimeSwap class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PrimeSwap()
        self.assertIsInstance(instance, PrimeSwap)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PrimeSwap()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
