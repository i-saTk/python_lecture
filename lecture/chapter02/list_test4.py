nums1 = [1,3,5,7]
nums2 = [2,4,6,8]
# リストの連結
n =  nums1 + nums2
print(n)
# 昇順にソート
n.sort()
print(n)
# 逆順にソート(結果、降順となる)
n.reverse()
print(n)

nums3 = ["a","b","c"]
# イテラブルと結合
n.extend(nums3)
print(n)
# エラー
# n.sort()
n.reverse()
print(n)
# print(n)

n.remove("a")
print(n)
# n.remove("a")
# print(n)

print(type(n))
print(type(n[0]))
print(type(n[8]))

# print(help(list))
print(help(print))