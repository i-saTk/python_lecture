import os
os.makedirs("C:/pywork/chapter07/Test", exist_ok=True)


#ファイル書込
with open("C:/pywork/chapter07/Test/test.txt", "a",encoding="utf-8") as f:
    l = f.write("ナイスレッチュー！\n")
    print(l)
    f.flush()
#ファイル読込
with open("C:/pywork/chapter07/Test/test.txt", "r",encoding="utf-8") as f:
    # for r in f.readlines():
    print(f.read(25))