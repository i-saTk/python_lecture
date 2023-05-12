
sum = 0

while True:
    # 数値入力
    num = int(input("数値を入力："))
    # 0が入力されたら終了
    if num == 0:
        break
    # 合計を求める
    sum += num
    
print("合計：", sum)
