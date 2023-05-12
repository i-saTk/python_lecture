# csvファイルからデータを取得
with open("C:/pywork/chapter07/csv/test.csv", "r") as f:
    data = f.readlines()

print("読み込んだCSVファイル")
print(data)
print()

# 「,」を区切りにリストにし、2次元データを作る
data2 = []
for d in data:
    d2 = d.split(",")
    print(d2)
    d2[0] = int(d2[0])          # 1列目の値 数値に変換
    d2[1] = d2[1].strip('"')    # 2列目の値 前後の「"」を取り除く
    d2[2] = int(d2[2])          # 3列目の値 数値に変換
    print(d2[2])
    data2.append(d2)
    print(d2)
print("2次元データに変換")
print(data2)