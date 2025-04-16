def steps(number):
    
    steps = 0
    error = "Only positive integers are allowed"
    
    try:
        number = int(number)
    except:
        return error
    
    if number < 1:
        return error
    
    while number != 1:
        
        steps += 1
        
        if number % 2 == 0:
            number = number//2
        else:
            number = number * 3 + 1
            
    return steps

print(steps(input("Enter a number: ")))