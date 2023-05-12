def moning():
    print("おはようございます")

def noon():
    print("こんにちは")

def proc(name, msg):
    print(name, "さん")
    msg()

def main():
    n = input("名前を入力してください>>>")
    t = input("0:朝\t1:昼>>>")
    
    if t == "0":
        f = moning
    elif t == "1":
        f = noon
    proc(n, f)

if __name__ == "__main__":
    # main()
    dic = {1:moning, 2:noon}
    x = int(input("数値入力："))
    if x in dic:
        f = dic[x]
        f()
