try:
    a = int(input("a="))
    b = int(input("b="))
    y = a / b
    print(a, "/", b, "=", y)
except ValueError as e:
    print("整数に変換できませんでした。")
    print(e)
    print(type(e))

except Exception as e:
    print("その他の例外")
    print(e)
    print(type(e))
print("処理終了")