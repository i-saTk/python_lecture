# #for文で記述
# resultFor = []
# for i in range(0 , 11):
#     if i % 2 == 0:
#         resultFor.append(i)
# print(resultFor)
# #リスト内包表記
# result = [i for i in range(0,11) if i % 2 == 0]
# print(result)

# # リストの値を倍にしたリストを作成
# nums = [1,2,3,4,5,6]
# nums_double = []
# for num in nums :
#     nums_double.append(num * 2)
# print(nums_double)

# nums_double = [num * 2 for num in nums]
# print(nums_double)


# nums_double2 = []
# for num in range(101) :
#     if num % 5 == 0:
#         nums_double2.append(num)
# print(nums_double2) 

# nums_double2 = [num for num in range(101) if num % 5 == 0]
# print(nums_double2)

# # loop_num = int(input("入力回数を指定してください。："))
nums2 = list(range(1,int(input("入力回数を指定してください。：")) + 1))
print(nums2)
words = [input("名前を登録：") for n in nums2]
print(words)
dic1 = dict(zip(nums2,words))
print(dic1)
[print(f"出席番号:{key}番：{value}")for key, value in dict(zip(nums2,words)).items()]


