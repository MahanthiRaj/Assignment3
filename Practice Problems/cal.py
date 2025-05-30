#create a calultor which is having a = 5, b = 6


def calculator(num1,num2,n):

    if n == '+':
        result = num_1+num_2
        return " addition",result
    elif n == '-':
        result = num_1-num_2
        return " subraction",result
    elif n == '*':
        result = num_1*num_2
        return "Multiplication",result
    elif n == '/':
        result = num_1/num_2
        return "Division",result
    elif n == '%':
        result = num_1%num_2
        return "Division",result
    else:
        return "enter a valid input"
    


#print("addition:",c,"\nsubtraction:",d,"\nMultiplication: ",e,"\nDivision:",f,"\nModulus:",g)
#print(f"addition:{c}",f"\nsubtraction:{d}",f"\nMultiplication:{e}",f"\nDivision:{f}",f"\nModulus:{g}")




