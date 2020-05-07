def secant():
    x0 = int(input("Please enter first guess: "))
    x1 = int(input("Please enter second guess: "))
    tolerance = 0.00001
    while(abs(x1-x0) > tolerance):
        x2 = x1 - (func_1(x1)*(x1 - x0))/(func_1(x1)-func_1(x0))
        x0 = x1
        x1 = x2
    print("Final guess: " + str(round(x2, 6)))
    return x2
def func_1(x):
    return (x**3) - (2*x) - 2
