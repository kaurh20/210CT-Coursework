#task 3- perfect square


def perfectSquare(n):

    x = n
    while True :
        if x**2 <= n :
            print ("The highest perfect square of %s  is %s" % (n,x**2))

            return x**2
        else:
            x -= 1

highest_sqr = perfectSquare(5)




