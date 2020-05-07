def bisection():
    a = int(input("Enter lower bound for bisection: "))
    b = int(input("Enter upper bound for bisection: "))
    c = (a+b)/2
    tolerance = 0.00001
    if(func_1(a)*func_1(b) < 0 or func_1(c) == 0):
        while(abs(a-b) > tolerance) :
            if func_1(a)*func_1(c) < 0:
                b = c
            elif func_1(b)*func_1(c) < 0:
                a = c
            c = (a+b)/2
            print("c = " + str(c))
        print("Final guess is: " + str(round(c,5)))
    else:
        print("Both numbers are either positive or negative")
        return


def func_1(x):
    return (2*x**4) + (x**3) - (4*x) - 1
