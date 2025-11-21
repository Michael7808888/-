"""
此版本的 safe_division 函式移除了除以零的處理
用於演示紅燈（測試失敗）的情況
"""


def safe_division(a, b):
    """
    除法函式（無安全處理）
    
    參數:
        a (float/int): 被除數
        b (float/int): 除數
    
    返回:
        float: 除法結果
    
    注意: 此版本未處理除以零的情況，會導致 ZeroDivisionError
    """
    # 處理除以零的程式碼已被註解/移除
    # if b == 0:
    #     return None
    return a / b
