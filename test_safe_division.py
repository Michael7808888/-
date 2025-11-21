"""
Unit tests for safe_division function - 單元測試

This test suite validates the safe_division function with various test cases,
including normal cases, edge cases, and error handling scenarios.
"""

import unittest
from safe_division import safe_division


class TestSafeDivision(unittest.TestCase):
    """Test cases for the safe_division function"""
    
    def test_normal_division(self):
        """測試正常的數值相除 - Test normal division"""
        self.assertEqual(safe_division(10, 2), 5.0)
        self.assertEqual(safe_division(9, 3), 3.0)
        self.assertEqual(safe_division(15, 4), 3.75)
    
    def test_negative_numbers(self):
        """測試負數相除 - Test division with negative numbers"""
        self.assertEqual(safe_division(-10, 2), -5.0)
        self.assertEqual(safe_division(10, -2), -5.0)
        self.assertEqual(safe_division(-10, -2), 5.0)
    
    def test_float_division(self):
        """測試浮點數相除 - Test division with floating point numbers"""
        self.assertAlmostEqual(safe_division(7.5, 2.5), 3.0)
        self.assertAlmostEqual(safe_division(1.0, 3.0), 0.3333333333333333)
    
    def test_boundary_values(self):
        """測試邊界值相除 - Test division with boundary values"""
        self.assertEqual(safe_division(0, 5), 0.0)
        self.assertAlmostEqual(safe_division(1, 1000000), 0.000001)
        self.assertEqual(safe_division(1000000, 1), 1000000.0)
    
    def test_division_by_zero_raises_error(self):
        """測試除以零會引發錯誤 - Test that division by zero raises ValueError"""
        with self.assertRaises(ValueError) as context:
            safe_division(10, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")
    
    def test_zero_divided_by_zero(self):
        """測試零除以零會引發錯誤 - Test that 0/0 raises ValueError"""
        with self.assertRaises(ValueError) as context:
            safe_division(0, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")
    
    def test_large_numbers(self):
        """測試大數值相除 - Test division with large numbers"""
        self.assertEqual(safe_division(1000000, 1000), 1000.0)
        self.assertAlmostEqual(safe_division(1e10, 1e5), 1e5)
    
    def test_small_numbers(self):
        """測試小數值相除 - Test division with small numbers"""
        self.assertAlmostEqual(safe_division(0.001, 0.1), 0.01)
        self.assertAlmostEqual(safe_division(1e-5, 1e-3), 0.01)


class TestSafeDivisionRedLight(unittest.TestCase):
    """
    紅燈測試情境 - Red Light Test Scenarios
    
    These tests demonstrate what happens when division by zero protection
    is removed from the safe_division function.
    
    註：當 safe_division 函式中的「處理除以零」程式碼被註解或刪除時，
    這些測試會失敗（紅燈），因為程式會直接拋出 ZeroDivisionError。
    
    Note: When the "division by zero handling" code in safe_division is
    commented out or removed, these tests will fail (red light) because
    the program will directly throw ZeroDivisionError.
    """
    
    def test_division_by_zero_protected(self):
        """
        測試除以零的保護機制
        
        綠燈情境：函式應該拋出 ValueError（我們的自定義錯誤）
        紅燈情境：如果移除保護，函式會拋出 ZeroDivisionError（Python 內建錯誤）
        
        Green: Function should raise ValueError (our custom error)
        Red: Without protection, function raises ZeroDivisionError (Python built-in error)
        """
        # This test expects ValueError (green light scenario)
        with self.assertRaises(ValueError):
            safe_division(100, 0)


def run_tests_with_output():
    """
    執行測試並輸出詳細結果 - Run tests with detailed output
    
    This function runs all tests and provides colored output to show
    green light (passing) and red light (failing) scenarios.
    """
    # Create a test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test cases
    suite.addTests(loader.loadTestsFromTestCase(TestSafeDivision))
    suite.addTests(loader.loadTestsFromTestCase(TestSafeDivisionRedLight))
    
    # Run tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 70)
    print("測試結果摘要 - Test Summary")
    print("=" * 70)
    print(f"總測試數 Total tests run: {result.testsRun}")
    print(f"成功 Passed: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"失敗 Failed: {len(result.failures)}")
    print(f"錯誤 Errors: {len(result.errors)}")
    
    if result.wasSuccessful():
        print("\n✓ 所有測試通過！(綠燈) - All tests passed! (Green light)")
    else:
        print("\n✗ 有測試失敗！(紅燈) - Some tests failed! (Red light)")
    
    return result


if __name__ == '__main__':
    # Run tests with detailed output
    run_tests_with_output()
