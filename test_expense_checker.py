"""
expense_checker.pyの簡易テスト（pytest等は使わず、assertのみで動作確認する）。
python test_expense_checker.py で実行する。
"""
from expense_checker import approval_level

assert approval_level(10000) == "所属長"
assert approval_level(49999) == "所属長"
assert approval_level(50000) == "部門長"  # 5万円ちょうどは部門長承認のはず
assert approval_level(100000) == "部門長"
assert approval_level(199999) == "部門長"
assert approval_level(200000) == "経理部長"
assert approval_level(500000) == "経理部長"

print("全テスト成功")
