# 繰り返し処理の開始
loop_flag = 1
while loop_flag:
    s = input("文字列を入力してください：")
    print(s + "が入力されました。")
    if s == "End":
        print("終わります")
        loop_flag = 0