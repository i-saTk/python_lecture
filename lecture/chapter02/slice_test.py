# リストを準備
ls = [1,3,5,7,9,11,13,17]
# 2～4番目の要素を取得
print(ls[2:5])
# 先頭から2番目までの要素を取得
print(ls[:3])
# 3番目から末尾までの要素を取得
print(ls[3:])

# 逆(刻み値-2）
print(ls[-1 : -7 : -2])
print(ls[7 :: -1])

# 文字列を準備
s = "Hello Python!"
# Helloの部分を抽出
print(s[:5])
# Pythonの部分を抽出
start = 6   
length = 6
print(s[start:start+length])

print(s[-1:-9:-1])