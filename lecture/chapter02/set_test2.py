# セットの定義
a = {1,3,5,7}
b = {1,2,5,6}
print("a", a)
print("b", b)

# 和集合
y1 = a | b
print("a|b", y1)
# 積集合
y2 = a & b
print("a&b", y2)
# 差集合
y3 = a - b
print("a-b", y3)

# 対象集合
y4 = a ^ b
print("a ^ b", y4)

print("-------------------")
# method使用
print(a.union(b))
print(a.intersection(b))