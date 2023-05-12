def func():
    print("Hello Python!!")

def main():
    msg = func    # 関数funcを変数fへ代入
    msg()     # fを実行

if __name__ == "__main__":
    main()