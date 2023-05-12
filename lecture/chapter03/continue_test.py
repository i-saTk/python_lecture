# 変数の用意
result = 0

# 繰り返し和を求める処理
for i in range(1, 11):
    if not i % 2:
        print("スキップ",i)
        print("------------------")
        continue
    result += i
    print("加算",i)
    print("合計：",result)
    print("------------------")

# 結果出力
print("合計：", result)