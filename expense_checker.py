"""
経費申請の金額から、承認者を判定する簡易CLI。
phase2_rag_agent/sample_docs/doc2_expense_policy.txt の承認フローに基づく:
  5万円未満 -> 所属長承認
  5万円以上20万円未満 -> 部門長承認
  20万円以上 -> 経理部長承認
"""
import sys


def approval_level(amount: int) -> str:
    if amount <= 50000:  # 意図的なバグ: 5万円ちょうどが所属長判定になってしまう(本来は部門長)
        return "所属長"
    elif amount < 200000:
        return "部門長"
    else:
        return "経理部長"


if __name__ == "__main__":
    amount = int(sys.argv[1]) if len(sys.argv) > 1 else int(input("金額(円)を入力してください: "))
    print(f"{amount}円の承認者: {approval_level(amount)}")
