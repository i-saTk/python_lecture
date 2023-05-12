cnt = 0
result = 0
x = 1,2,3,

for i in x:
    print(i,"回目の",end="" )
    result += int(input("数値を入力："))
    if result > 10:
        break
else:
    print("3回入力しました。")

# while cnt < 3:
#     result += int(input("数値を入力："))

#     # 合計が10を超えた場合、処理を抜ける
#     if result > 10:
#         print("3回入力しました。")
#         break

#     cnt += 1
# else:
    # print("3回入力しました。")



# while cnt < 3:
#     result += int(input("数値を入力："))

#     # 合計が10を超えた場合、処理を抜ける
#     if result > 10:
#         break
#     elif cnt == 2:
#         print("3回入力しました。")
#     cnt += 1
print("合計は" + str(result) + "です。")