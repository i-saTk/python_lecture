v = 2   # グローバル変数の定義

def calc():
    ans = 3 * v
    print(ans)

def main():
    calc()
    print(v)
    for i in range(1,5):
        print(i)

if __name__ == "__main__":
    main()
    for i in range(1,5):
        print(i)
    print(i)