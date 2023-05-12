k = ["S", "M", "L"]
v = [6, 10, 15]

# zip関数による辞書の作成
d = dict(zip(k, v))
d2 = dict(zip(v, k))
print(d)
print(d2)