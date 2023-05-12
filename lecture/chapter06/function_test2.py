def func(x,y):
    print("回数：", x)
    for i in range(x):
        print(i)
    print(y**2)

def main():
    func(y=3,x=3)
    # func()  # デフォルト値を用いて呼び出し

if __name__ == "__main__":
    main()