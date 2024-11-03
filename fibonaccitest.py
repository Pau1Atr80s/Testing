# Fibonacci sequence generator

# Function to generate Fibonacci numbers up to n terms
def fibonacci(n):
    a, b = 0, 1
    sequence = []
    
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
        
    return sequence

# Input: how many terms to generate
terms = int(input("Enter the number of terms in the Fibonacci sequence: "))

# Ensure the input is valid
if terms <= 0:
    print("Please enter a positive integer.")
else:
    # Call the function and display the sequence
    print(f"Fibonacci sequence up to {terms} terms:")
    print(fibonacci(terms))
