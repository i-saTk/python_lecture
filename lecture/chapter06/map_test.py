def pow2(num):
    return (num)**2

def main():
    nums = [1,2,3,4]
    rs = list(map(pow2, nums))
    # rs = []
    # for i in nums:
    #     rs.append(pow2(i))
    print(rs)

if __name__ == "__main__":
    main()