v = 2   # グローバル変数の定義
print(v)
def calc():
    global v #宣言
    v = 10  # ローカル変数の定義 
    ans = 3 * v
    print(ans)
    print(v)
    print("↑↑↑関数内---------")

def main():
    calc()
    print(v)
    print("↑↑↑グローバル---------")


if __name__ == "__main__":
    main()