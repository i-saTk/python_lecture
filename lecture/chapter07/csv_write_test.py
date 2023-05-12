from os import makedirs as mk
# フォルダ作成
file = "C:/pywork/chapter07/csv"
mk(file, exist_ok=True)
# 2次元データの作成
dt1 = [1, "12:34", 65]
dt2 = [2, "12:40", 70]
dt3 = [3, "12:45", 80]
data = [dt1, dt2, dt3]

print("2次元データ")
print(data)
print()
# データを1行ずつCSVの形式に変換
data2 = []
for d in data:
    print(d)
    s = str(d[0]) + ","     # 1列目の値 数値を文字列へ変換し、カンマを付ける
    print(s)
    s += '"' + d[1] + '",'  # 2列目の値 前後に「"」を付けて、カンマを付ける
    print(s)
    s += str(d[2]) + "\n"   # 3列目の値 数値を文字列へ変換し、カンマを付ける
    print(s)
    data2.append(s)
    print(data2)
    print()

print("ファイル書込み前のデータ")
print(data2)
print()
# CSVファイルへ書込み 
with open(file + "/" + "test.csv", "w") as f:
    f.writelines(data2)
    f.flush()
    print("書込み完了")