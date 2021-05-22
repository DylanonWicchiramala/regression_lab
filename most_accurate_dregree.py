import numpy as np
import polynomial_regression as reg

# find the most accurate dregree by least squre method

# determine P^n(x) is polynomial regression dregree n
# formula -> E(x) = sum(yi - P^deg(xi))^2
# least squre formula -> minEx = min(sum(yi - P^deg(xi))^2 for deg [1-50])


def get(X1 ,Y , deg_rang:tuple = (1,25)):
    
    minEx = float('inf')
    # loop through degree.
    for current_degree in range(deg_rang[0],deg_rang[1]):
        sum = 0
        # Iterating over data.
        for i in range(len(X1)):
            #pxi = P^current_degree(X[i])
            pxi = reg.regrassion_predict(
                X1[i], X1, Y, degree=current_degree)
            #(yi - P^deg(xi))^2
            sum += (pxi - Y[i])**2

        #print(" dregree " + str(current_degree) + " : " + str(sum))
        if sum < minEx:
            minEx = sum
            mindrg = current_degree

    #print("most accurate dregree is " + str(mindrg))
    #print(" Ex : " + str(minEx))
    
    return mindrg, minEx


def present(X1 ,Y , deg_rang:tuple = (1,25)):
    
    minEx = float('inf')
    # loop through degree.
    for current_degree in range(deg_rang[0],deg_rang[1]):
        sum = 0
        # Iterating over data.
        for i in range(len(X1)):
            #pxi = P^current_degree(X[i])
            pxi = reg.regrassion_predict(
                X1[i], X1, Y, degree=current_degree)
            #(yi - P^deg(xi))^2
            sum += (pxi - Y[i])**2

        print(" dregree " + str(current_degree) + " : " + str(sum))
        if sum < minEx:
            minEx = sum
            mindrg = current_degree

    print("most accurate dregree is " + str(mindrg))
    print(" sum(Yi - f(Xi))^2 : " + str(minEx))
    