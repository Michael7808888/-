"""
紅燈演示 - Red Light Demonstration

This file demonstrates what happens when the division by zero protection
is removed from the safe_division function.

此檔案演示當從 safe_division 函式中移除除以零保護時會發生什麼。
"""

# Create a version of safe_division WITHOUT the protection
def safe_division_broken(a, b):
    """
    This is a BROKEN version without division by zero protection
    這是一個沒有除以零保護的錯誤版本
    """
    # The protection code is commented out / removed:
    # if b == 0:
    #     raise ValueError("Cannot divide by zero")
    return a / b


print("=" * 70)
print("紅燈演示 - Red Light Demonstration")
print("=" * 70)
print("\n當移除除以零保護時，會發生什麼？")
print("What happens when division by zero protection is removed?\n")

# Test 1: Normal division (still works)
print("測試 1 - Test 1: 正常除法 Normal division (10 / 2)")
try:
    result = safe_division_broken(10, 2)
    print(f"  ✓ 結果 Result: {result}")
except Exception as e:
    print(f"  ✗ 錯誤 Error: {type(e).__name__}: {e}")

# Test 2: Division by zero (THIS WILL FAIL - RED LIGHT!)
print("\n測試 2 - Test 2: 除以零 Division by zero (10 / 0)")
try:
    result = safe_division_broken(10, 0)
    print(f"  ✓ 結果 Result: {result}")
except ZeroDivisionError as e:
    print(f"  ✗ 錯誤 Error (紅燈 RED LIGHT!): {type(e).__name__}: {e}")
    print("     程式沒有妥善處理除以零的情況！")
    print("     The program did not properly handle division by zero!")
except ValueError as e:
    print(f"  ✓ 正確處理 Properly handled: {type(e).__name__}: {e}")

print("\n" + "=" * 70)
print("結論 - Conclusion:")
print("=" * 70)
print("當移除除以零保護機制時：")
print("When division by zero protection is removed:")
print("  • 程式會直接拋出 ZeroDivisionError（紅燈）")
print("  • The program directly throws ZeroDivisionError (RED LIGHT)")
print("  • 單元測試會失敗，因為預期的是 ValueError")
print("  • Unit tests will fail because they expect ValueError")
print("=" * 70)
