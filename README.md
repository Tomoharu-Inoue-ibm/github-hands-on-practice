# ハンズオン実践用プロジェクト

`../05_hands_on_lab.md`の演習で使う、経費申請の承認者判定CLI。**このフォルダの内容をそのまま新しいGitHubリポジトリの初期コミットとして使う。**

- `expense_checker.py`: 金額から承認者を判定する（**意図的なバグが1つ埋め込まれている**。演習で見つけて修正する）
- `test_expense_checker.py`: 手動実行の簡易テスト（`python test_expense_checker.py`）
- `config.py`: 予算上限の設定値（コンフリクト実践演習で使う）
- `.gitignore`: `__pycache__/`等を除外する最小限の設定

詳しい手順は`../05_hands_on_lab.md`を参照。
