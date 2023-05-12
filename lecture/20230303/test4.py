nums = []

while True:
    # 数値の入力
    n = input("数値を入力：")
    # endであれば終了
    if n == "end":
        break
    # リストに追加
    n = int(n)
    nums.append(n)

print(nums)