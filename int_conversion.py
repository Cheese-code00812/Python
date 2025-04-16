from num2words import num2words

def num2word_conversion(x):   
    y = num2words(x)
    return y

print(num2word_conversion(input("Enter a number: ").strip().lower()))