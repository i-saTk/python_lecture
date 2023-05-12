def func(num, count):
    print("num:", num, "count:", count)
    for i in range(count):
        print(num * i)


def main():
    func(10, 5) # 順に引数を指定した場合 
    func(count=5, num=10)   # キーワード引数を用いた場合
    # func(count=3) # キーワード引数を用いてcountのみ指定した場合

if __name__ == "__main__":
    main()