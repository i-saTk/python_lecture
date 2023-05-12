try:
    a = int(input("a="))
    b = int(input("b="))
    y = a / b
    print(a, "/", b, "=", y)
except ValueError:
    print("整数に変換できませんでした。")
except Exception:
    print("その他の例外")
print("処理終了")