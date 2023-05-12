# main関数の定義
def main():
    max_num = func_max(25, 50)
    func_add(100,200)
    print("大きい数値は", max_num, "です。")


#大きい数値を返す関数
def func_max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
# 加算関数
def func_add(num1, num2):
    print("合計は", num1 + num2, "です。")



# main関数の呼び出し
if __name__ == "__main__":
    main()
    print(__name__)
else:
    print("モジュールですよ")
    print("func_testの処理------------")