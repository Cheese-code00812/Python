list = [0]
already_one = False
tried = False
n = 0
y = 1
choice = "yes"

while not tried:
    
    try:
        limit = int(input("Enter a limit for the Fibonacci Sequence: "))
        tried = True
    except:
        print("Invalid answer. Try again! (Has to be an integer)")
        tried = False
        
while n+y <= limit:
    
    x = n
    
    if n == 0:
        n = 1
        list.append(n)
    elif n == 1 and not already_one:
        n = 1
        already_one = True
        list.append(n)
    else:
        n += y 
        y = x
        list.append(n)
        
        
print(list)