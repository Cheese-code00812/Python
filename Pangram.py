def is_pangram(sentence):
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for i in alphabet:
        if i not in sentence:
            return False
    return True

sentence = input("Enter a sentence: ").lower().strip()

if is_pangram(sentence):
    print(f"sentence is a pangram.")
else:
    print(f"sentence is NOT a pangram.")