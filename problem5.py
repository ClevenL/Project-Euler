
for i in range(0, 2000000000, 20):
    for i2 in range(1, 20):
        if i % i2 == 0:
            pass
        else:
            break
        if i2 == 19:
            print(i)

'''
for i in range(0, 3000, 10):
    for i2 in range(1, 10):
        if i % i2 == 0:
            pass
        else:
            break
        if i2 == 9:
            print(i)
'''
