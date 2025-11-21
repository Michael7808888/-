"""
安全除法函式模組
提供一個可以安全處理除以零的除法函式
"""


def safe_division(a, b):
    """
    安全除法函式，處理除以零的情況
    
    參數:
        a (float/int): 被除數
        b (float/int): 除數
    
    返回:
        float: 除法結果，如果除數為零則返回 None
    
    範例:
        >>> safe_division(10, 2)
        5.0
        >>> safe_division(10, 0)
        None
        >>> safe_division(-10, 2)
        -5.0
    """
    # 處理除以零的情況
    if b == 0:
        return None
    return a / b
