# キー入力
s = input("「平日」は1を、「休日」は0を入力してください：")

# 平日の場合のメッセージを表示
if s == "1":
    print("今日は仕事があります。")
elif s == "0":
    print("今日は遊びに行きましょう。")
else:
    print("今日は家でおとなしくしていましょう。")