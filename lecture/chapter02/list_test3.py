nums = [1,3,5,7]
# 要素の追加
nums.append(30)
print(nums)
# 指定の位置に要素を追加
nums.insert(1, 40)
print(nums)
# 指定の位置にある要素を削除
n = nums.pop(0)
print(n)
print(nums)

# テキスト外(引数省略）
a = nums.pop()
print(a)
print(nums)

# 要素外insert
nums.insert(-10, 100)
print(nums)
print(nums[4])
