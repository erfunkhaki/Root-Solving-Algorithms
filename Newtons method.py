def newtons_method():
    x0 = int(input("Please enter a guess: "))
    user_input = input("Please enter polynomial coefficients (spaces between numbers): ")
    previous_x0 = 0
    tolerance = 0.0001
    x1 = x0 - (polynomial(x0,user_input)/polynomial_der(x0,user_input))
    previous_distance = abs(x0-previous_x0) 
    while(abs(x0-previous_x0) > tolerance):
        if(previous_distance < abs(x0-previous_x0)):
            print("x0 does not converge")
            exit(0)
        x1 = x0 - (polynomial(x0,user_input)/polynomial_der(x0,user_input))
        previous_distance = abs(x0-previous_x0) 
        previous_x0 = x0
        x0 = x1

    print("Final guess: " + str(round(x1, 6)))
    return x1


def polynomial(x1, values):
    new_values = values.split()
    total = 0
    exp = len(new_values)
    for x in range(len(new_values)):
        coeff = new_values[x]
        total += int(coeff) * (pow(x1, exp))
        exp += -1
    return total

def polynomial_der(x1, values):
    new_values = values.split()
    total = 0
    exp = len(new_values)
    for x in range(len(new_values)):
        coeff = new_values[x]
        total += (len(new_values)-x)*int(coeff)*(pow(x1,exp))
        exp += -1
    return total
    


