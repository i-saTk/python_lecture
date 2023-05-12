# 入力したものを保存する
text = []
c = 1
while True:
    s = input(f"{c}:")
    # EOF終了
    if s == "EOF":
        break
    s += "\n"
    text.append(s)
    c += 1

print(text)

# ファイル名の作成
import datetime
now = datetime.datetime.now()
d = f"{now:%Y%m%d_%H%M}.txt"
print(d, "テキストファイルを作成します。")

# テキストファイルの保存
with open(d, "w") as f:
    f.writelines(text)
