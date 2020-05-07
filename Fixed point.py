def fixed_point():
    guess = float(input("please enter first guess for the fixed point method: "))
    tolerance = 0.00001
    previous_guess = guess
    current_guess = func_2(guess)
    current_difference = abs(current_guess - previous_guess) 
    previous_difference = abs(current_guess - previous_guess) 
    while(abs(current_guess - previous_guess) > tolerance):
        if(current_difference > previous_difference):
            print("Numbers don't converge")
            exit(0)
        else:
            previous_guess = current_guess
            print(previous_guess)
            current_guess = func_2(previous_guess)
            previous_difference = current_difference
            current_difference = abs(current_guess - previous_guess) 
    print("Final guess: " + str(round(current_guess,5)))


def func_2(x):
    return ((2*x)+1)**1/5



