

def d2x(x10):
    x16 = hex(x10)
    # print(r16)
    x16 = x16[2:]
    x16 = x16.upper()
    if len(x16) == 1:
        x16 = "0" + x16
    # r16 = f"{r16:02s}"
    # print(r16)
    return x16

d2x = lambda x10 : hex(x10)[2:].upper().zfill(2)

r = input("R=")
g = input("G=")
b = input("B=")
r10 = int(r)
g10 = int(g)
b10 = int(b)
r16 = d2x(r10)
g16 = d2x(g10)
b16 = d2x(b10)
# print(r16)

code16 = "#" + r16 + g16 + b16

code = []
for i in ("r", "g", "b"):
    code.append(input(i + "="))
code = list(map(int, code))
code = list(map(d2x, code))
# print(code)
# print(code16)