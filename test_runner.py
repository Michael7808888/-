"""
測試結果觀察腳本
此腳本演示綠燈和紅燈的測試結果
"""

import os
import subprocess
import sys


def run_green_light_test():
    """執行綠燈測試（使用完整的 safe_division）"""
    print("=" * 70)
    print("🟢 綠燈測試（Green Light Test）- 使用正確的 safe_division")
    print("=" * 70)
    print()
    
    result = subprocess.run(
        [sys.executable, "-m", "unittest", "test_safe_division.py", "-v"],
        cwd=os.path.dirname(os.path.abspath(__file__)),
        capture_output=True,
        text=True
    )
    
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
    
    print()
    if result.returncode == 0:
        print("✅ 結果: 所有測試通過（綠燈）")
        print("說明: safe_division 函式正確處理了各種情境，包括除以零的狀況")
    else:
        print("❌ 結果: 測試失敗")
    
    print()
    return result.returncode == 0


def run_red_light_test():
    """執行紅燈測試（使用無處理的版本）"""
    print("=" * 70)
    print("🔴 紅燈測試（Red Light Test）- 移除除以零處理")
    print("=" * 70)
    print()
    print("將 safe_division.py 替換為無處理版本...")
    print()
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 備份原始文件並替換
    subprocess.run(
        ["cp", "safe_division.py", "safe_division_backup.py"],
        cwd=script_dir
    )
    subprocess.run(
        ["cp", "safe_division_without_handling.py", "safe_division.py"],
        cwd=script_dir
    )
    
    result = subprocess.run(
        [sys.executable, "-m", "unittest", "test_safe_division.py", "-v"],
        cwd=script_dir,
        capture_output=True,
        text=True
    )
    
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
    
    print()
    if result.returncode != 0:
        print("❌ 結果: 測試失敗（紅燈）")
        print("說明: 除以零的測試失敗，因為程式直接丟出 ZeroDivisionError，未被妥善處理")
    else:
        print("✅ 結果: 測試通過")
    
    # 恢復原始文件
    subprocess.run(
        ["cp", "safe_division_backup.py", "safe_division.py"],
        cwd=script_dir
    )
    subprocess.run(
        ["rm", "safe_division_backup.py"],
        cwd=script_dir
    )
    
    print()
    return result.returncode != 0


def main():
    """主函式"""
    print("\n" + "=" * 70)
    print("任務三：執行測試，觀察綠燈與紅燈結果")
    print("=" * 70)
    print()
    
    # 執行綠燈測試
    green_passed = run_green_light_test()
    
    # 執行紅燈測試
    red_failed = run_red_light_test()
    
    # 總結
    print("=" * 70)
    print("📊 測試總結")
    print("=" * 70)
    print()
    print(f"綠燈測試: {'✅ 通過' if green_passed else '❌ 失敗'}")
    print(f"紅燈測試: {'✅ 如預期失敗' if red_failed else '❌ 未如預期'}")
    print()
    print("結論:")
    print("- 當 safe_division 函式包含除以零的處理時，所有測試通過（綠燈）")
    print("- 當移除除以零的處理時，相關測試失敗（紅燈）")
    print("- 這證明了單元測試能有效檢測程式碼的正確性")
    print()


if __name__ == "__main__":
    main()
