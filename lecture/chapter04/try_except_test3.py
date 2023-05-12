try:
    a = int(input("a="))
    b = int(input("b="))
    y = a / b
    print(a, "/", b, "=", y)
except ValueError:
    print("整数に変換できませんでした。")
except ZeroDivisionError:
    print("0除算が行われました。")
print("処理終了")