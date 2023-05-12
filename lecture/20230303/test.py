# a = 10
# b = 20

# n = "y"
# while n == "y":
while True:
    a = input("a=")
    b = input("b=")
    a = int(a)
    b = int(b)
    op = input("演算：")

    if op == "+":
        r = a + b
    elif op == "-":
        r = a - b
    elif op == "*":
        r = a * b
    elif op == "/":
        r = a / b

    print(a, op, b, "=", r)

    n = input("計算を続けますか？（y/n）：")

    if n != "y":
        break

# print(a, "+", b, "=", r)
# print(str(a) + " + " + str(b) + " = " + str(r))
# print(f"{a} + {b} = {r}")
# print("{} + {} = {}".format(a, b, r))

