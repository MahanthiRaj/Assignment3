def calculator(operation, *args):  
    if operation == "add":  
        return sum(args)  

    elif operation == "subtract":  
        result = args[0]  
        for num in args[1:]:  
            result -= num  
        return result  

    elif operation == "multiply":  
        result = args[0]  
        for num in args[1:]:  
            result *= num  
        return result  

    elif operation == "divide":  
        result = args[0]  
        for num in args[1:]:  
            if num != 0:  
                result /= num  
            else:  
                return "Cannot divide by zero"  
        return result  

    else:  
        return "Invalid operation"  


print(calculator("add", 5, 10, 15)) 
print(calculator("subtract", 200, 50, 30)) 
print(calculator("multiply", 2, 5, 6))
print(calculator("divide", 120, 4, 2))
