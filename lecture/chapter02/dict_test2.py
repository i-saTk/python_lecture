# 辞書の定義
d1 = {"S":7, "M":10, "L":15}
print(d1)
# 要素の追加
d1["LL"] = 20
print(d1)
# 要素の変更
d1["S"] = 6
print(d1)
# 要素の削除
s = d1.pop("M")
print(s)
print(d1)