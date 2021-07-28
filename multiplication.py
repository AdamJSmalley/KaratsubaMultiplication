import math

def multiply(x, y):
    xLen = len(str(x))
    #xLenHalf = math.floor(xLen/2)
    yLen = len(str(y))
    #yLenHalf = math.floor(yLen/2)
    m = max(xLen, yLen)
    m2 = m//2

    if xLen == 1 or yLen == 1:
        return x*y

    else:

        a = x // 10**(m2)
        b = x % 10**(m2)
        c = y // 10**(m2)
        d = y % 10**(m2)
    
        print(a)
        print(b)
        print(c)
        print(d)

        step1 = multiply( a, c )
        step2 = multiply( b, d )
        step3 = multiply(( a + b ), ( c + d ))
        step4 = step3 - step2 - step1
    
        step5 = (step1 * 10**(2*m2)) + step2 + (step4 * 10**m2)
    
        return step5

x = 5678
y = 1234

kat = multiply( x, y )

print ( "kat is " + str(kat))
print(x*y)
