
#should have used [::-1] to check for palindrome
def check_palindrome(num):
    if int(str(num)[0]) == int(str(num)[5]) and int(str(num)[1]) == int(str(num)[4]) and int(str(num)[2]) == int(str(num)[3]):
        return True

for i1 in range(1000, 900, -1):
    for i2 in range(1000, 900, -1):
        product = i1 * i2
        if check_palindrome(product):
            print(product)

