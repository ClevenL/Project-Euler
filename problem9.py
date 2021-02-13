def checkPythagoreanTriple(tripletArray):
    a = tripletArray[0]
    b = tripletArray[1]
    c = tripletArray[2]
    if a**2 + b**2 == c**2:
        return True

def generateTriple(m,n):
    #generate the triplet with Euclid's formula
    if m > n:
        a = m**2 - n**2
        b = 2 * m * n
        c = n**2 + m **2
        return [a,b,c]
    else:
        return "m > n not satisfied"

def checkProblemCondition(tripletArray):
    a = tripletArray[0]
    b = tripletArray[1]
    c = tripletArray[2]
    if a + b + c == 1000:
        return True

for m in range(2, 30):
    for n in range(1, 29):
        if m == n:
            break
        else:
            triplet = generateTriple(m, n)
            if checkPythagoreanTriple(triplet) and checkProblemCondition(triplet):
                print(triplet)
                print(triplet[0] * triplet[1] * triplet[2])
