import random

def pass_guess(x):
    
    lower_letters = "abcedefghijklmnopqrstuvwxyz"
    upper_letters = lower_letters.upper()
    numbers = "0123456789"
    special_characters = "_-/!@#$%^&*()+=~`<>?|., "
    possible_combinations = lower_letters + upper_letters + numbers + special_characters
    
    guessed = False
    attempts = 0
    
    while not guessed:
        attempts += 1
        guess = ""
        for i in range(0,random.randint(0,27)):
            guess += random.choice(possible_combinations)
        if guess == x:
            return f"{x} has been guessed in {attempts} attempts!"

print(pass_guess(input("Create password: ")))