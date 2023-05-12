v = 2   # グローバル変数の定義

def calc():
    ans = 3 * v
    v = 10
    print(ans)

def main():
    calc()
    print(v)

if __name__ == "__main__":
    main()