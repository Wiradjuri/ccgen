import random

filename = ('bin.txt')

def get_random_prefix(filename):
    with open(filename, 'r') as file:
        numbers = [line.strip() for line in file.readlines() if len(line.strip()) >= 6]
    # Choose a random number from the list
    random_number = random.choice(numbers)
    # Return the first six digits
    return random_number[:6]

# Function to generate a random 9-digit string
def generate_random_digits(num_digits):
    return ''.join([str(random.randint(0, 9)) for _ in range(num_digits)])

# Function to generate a 16-digit credit card number and be approved by luhn's algorithm
def generate_credit_card():
    # Choose 1 six-digit prefix from the file:
    prefix = get_random_prefix('bin.txt')
    # Generate the remaining 9 digits randomly
    middle_section = generate_random_digits(9)
    # Calculate the Luhn checksum for the 15-digit number
    checksum_digit = calculate_luhn_checksum(prefix, middle_section)
    # Return the 16-digit number
    return prefix + middle_section + str(checksum_digit)

# Function to calculate Luhn's checksum digit
def calculate_luhn_checksum(prefix, middle_section):
    full_number = prefix + middle_section
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(full_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return (checksum % 10)

# Get the generated credit card number
card_number = generate_credit_card()

# Function to generate a random expiry date
def expiration_date_str():
    month = random.randint(1, 12)
    year = random.randint(2021, 2031)
    return f"{month}/{year}"

# Function to generate a random 3-digit CVC
def generate_cvc():
    # Generate a random 3-digit number
    cvc = str(random.randint(100, 999))
    return cvc

print(f"Credit Card Number: {card_number}", f"Expiry date: {expiration_date_str()}", f"CVC: {generate_cvc()}")