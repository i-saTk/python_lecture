try:
    f = open("test.txt", "r")
    print(f.readline())
finally:   
    f.close()