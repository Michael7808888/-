# 防呆裝置 - Safe Division Function

這個專案實現了一個防呆 (fool-proof) 的除法函式，能夠防止除以零的錯誤。

This project implements a fool-proof division function that prevents division by zero errors.

## 📋 專案內容 - Project Contents

### 任務一：safe_division 函式 - Task 1: safe_division Function

檔案：`safe_division.py`

實現了 `safe_division(a, b)` 函式，具有以下特性：
- ✅ 防止除以零錯誤
- ✅ 當除數為零時拋出 `ValueError` 異常
- ✅ 正確處理正數、負數、浮點數
- ✅ 處理邊界值情況

```python
def safe_division(a, b):
    """安全地進行除法運算，防止除以零"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

### 任務二：單元測試 - Task 2: Unit Tests

檔案：`test_safe_division.py`

使用 Python 的 `unittest` 框架生成的全面單元測試，包含：

**測試案例 Test Cases:**
1. ✅ 正常的數值相除 (Normal division)
2. ✅ 負數相除 (Division with negative numbers)
3. ✅ 浮點數相除 (Division with floating point numbers)
4. ✅ 邊界值相除 (Division with boundary values)
5. ✅ 除以零錯誤處理 (Division by zero error handling)
6. ✅ 零除以零錯誤處理 (Zero divided by zero error handling)
7. ✅ 大數值相除 (Division with large numbers)
8. ✅ 小數值相除 (Division with small numbers)

### 任務三：測試結果 - Task 3: Test Results

#### 🟢 綠燈情境 (Green Light Scenario)

當 `safe_division` 函式包含除以零保護機制時，所有測試通過：

```bash
python3 test_safe_division.py
```

**結果 Result:**
```
Ran 9 tests in 0.001s
OK
✓ 所有測試通過！(綠燈) - All tests passed! (Green light)
```

#### 🔴 紅燈情境 (Red Light Scenario)

檔案：`demo_red_light.py`

當移除或註解掉除以零保護機制（`if b == 0` 的判斷）時：

```python
# 移除這段保護程式碼 - Remove this protection code
# if b == 0:
#     raise ValueError("Cannot divide by zero")
```

**會發生什麼 What Happens:**
- ❌ 程式直接拋出 `ZeroDivisionError`
- ❌ 單元測試失敗（紅燈）
- ❌ 程式沒有妥善處理除以零的狀況

執行紅燈演示：
```bash
python3 demo_red_light.py
```

## 🚀 如何使用 - How to Use

### 1. 執行單元測試 - Run Unit Tests

```bash
python3 test_safe_division.py
```

### 2. 使用 safe_division 函式 - Use safe_division Function

```python
from safe_division import safe_division

# 正常使用 - Normal usage
result = safe_division(10, 2)  # Returns: 5.0

# 處理除以零 - Handle division by zero
try:
    result = safe_division(10, 0)
except ValueError as e:
    print(f"錯誤 Error: {e}")  # Prints: Cannot divide by zero
```

### 3. 查看紅燈演示 - View Red Light Demonstration

```bash
python3 demo_red_light.py
```

## 📊 測試覆蓋範圍 - Test Coverage

- ✅ 正常情境測試 (Normal scenarios)
- ✅ 邊界值測試 (Boundary value testing)
- ✅ 異常處理測試 (Exception handling)
- ✅ 負數測試 (Negative number testing)
- ✅ 浮點數測試 (Floating point testing)
- ✅ 零值測試 (Zero value testing)

## 🎯 學習重點 - Key Learning Points

1. **防呆設計 Fool-proof Design**: 預防性地處理錯誤，而不是讓程式崩潰
2. **單元測試 Unit Testing**: 自動化測試確保程式碼品質
3. **綠燈/紅燈 Green/Red Light**: 測試驅動開發的重要概念
4. **異常處理 Exception Handling**: 適當地處理和拋出異常

## 📝 結論 - Conclusion

此專案成功實現了：
- ✅ 任務一：撰寫防呆 safe_division 函式
- ✅ 任務二：生成單元測試程式碼
- ✅ 任務三：執行測試並觀察綠燈與紅燈結果

這個實作展示了如何編寫健壯的程式碼，並透過單元測試驗證其正確性。