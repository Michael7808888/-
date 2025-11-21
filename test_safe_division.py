"""
safe_division 函式的單元測試
測試各種情境包括正常數值相除、負數相除、邊界值相除和除以零
"""

import unittest
from safe_division import safe_division


class TestSafeDivision(unittest.TestCase):
    """safe_division 函式的測試類別"""
    
    def test_normal_division(self):
        """測試正常的數值相除"""
        self.assertEqual(safe_division(10, 2), 5.0)
        self.assertEqual(safe_division(100, 10), 10.0)
        self.assertEqual(safe_division(7, 2), 3.5)
    
    def test_negative_division(self):
        """測試負數相除"""
        self.assertEqual(safe_division(-10, 2), -5.0)
        self.assertEqual(safe_division(10, -2), -5.0)
        self.assertEqual(safe_division(-10, -2), 5.0)
    
    def test_zero_dividend(self):
        """測試被除數為零"""
        self.assertEqual(safe_division(0, 5), 0.0)
        self.assertEqual(safe_division(0, -5), 0.0)
    
    def test_division_by_zero(self):
        """測試除以零的情況"""
        self.assertIsNone(safe_division(10, 0))
        self.assertIsNone(safe_division(-10, 0))
        self.assertIsNone(safe_division(0, 0))
    
    def test_float_division(self):
        """測試浮點數相除"""
        self.assertAlmostEqual(safe_division(10.5, 2.5), 10.5/2.5)
        self.assertAlmostEqual(safe_division(1.0, 3.0), 1.0/3.0, places=5)
    
    def test_boundary_values(self):
        """測試邊界值"""
        self.assertEqual(safe_division(1, 1), 1.0)
        self.assertAlmostEqual(safe_division(0.001, 0.001), 1.0)


if __name__ == '__main__':
    unittest.main()
