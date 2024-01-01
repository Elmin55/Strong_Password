import random
import string

def generate_strong_password(first_name, last_name, keyword):
    
    combined_info = first_name + last_name + keyword
    combined_info_shuffled = ''.join(random.sample(combined_info, len(combined_info)))

    
    symbols = '!@#$%^&*()_+=-[]{}|;:,.<>?'
    random_symbols = ''.join(random.sample(symbols, 3))

    
    password = combined_info_shuffled + random_symbols

    return password


first_name = input("First Name: ")
last_name = input("Last Name: ")
keyword = input("Keyword: ")


strong_password = generate_strong_password(first_name, last_name, keyword)


print("Generated Strong Password:", strong_password)
