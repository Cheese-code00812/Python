import math
import random

def systematic_encrypter(x):
  
    x = x.replace(" ", "")
    x = x.lower()
    
    missmatched_letters = {"a":"b", "b":"c", "c":"d", "d":"e", "e":"f", "f":"g", "g":"h", "h":"i", "i":"j", "j":"k", "k":"l", "l":"m", "m":"n", "n":"o", "o":"p", "p":"q", "q":"r", "r":"s", "s":"t", "t":"u", "u":"v", "v":"w", "w":"x", "x":"y", "y":"z", "z":"a"}
    
    secondary_password = ""
    xroot = math.ceil(math.sqrt(len(x)))
    line = ""
    fline = []
    special_line = ""
    num = 0
  
    for i in x:
        if i not in missmatched_letters:
            special_line += i
        else:
            i = missmatched_letters[i]
            secondary_password += i
   
    
    for i in secondary_password:
        num += 1
        line += i
        if num >= xroot:
            fline.append(line)
            num = 0
            line = ""
      
                    
    if line:
        fline.append(line)
       
    x_num = 0
    
    for a in special_line:
        idx = random.randint(x_num, len(fline))
        fline.insert(idx, a)
        x_num = idx + 1
    
    return fline
   
x = input("Enter a message: ")

result = systematic_encrypter(x)

for i in result:
    chars = ["%5","7:","/a","k-"]
    if i != result[-1]:
        print(i, end=f"{random.choice(chars)}")
    else:
        print(i)