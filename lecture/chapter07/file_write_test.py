try:
    f = open("Test/test.txt", "a")
    l = f.write("Hello Python!!")
    print(l)
    f.flush()
finally:
    f.close()