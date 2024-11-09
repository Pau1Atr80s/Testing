import webbrowser

# Elegant Fibonacci sequence generator and summation

def fibonacci(n):
    """
    Generates the first n Fibonacci numbers.

    Parameters:
    n (int): The number of Fibonacci numbers to generate.

    Returns:
    list: A list of the first n Fibonacci numbers.
    """
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

def add_fibonacci(fibonacci_list):
    """
    Sums all integers in the given Fibonacci list.

    Parameters:
    fibonacci_list (list): A list of Fibonacci numbers.

    Returns:
    int: The sum of all Fibonacci numbers in the list.
    """
    return sum(fibonacci_list)

if __name__ == "__main__":

    # Input: how many terms to generate
    try:
        terms = int(input("Enter the number of terms in the Fibonacci sequence: "))
        if terms <= 0:
            print("Please enter a positive integer.")
        elif terms % 2 != 0:
            # Open a GIF of Anthony Edwards dunking a basketball if the number is odd
            webbrowser.open("https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNDB3dmphdXNmN3Z0MjVodW1yOHYxNDVidTl1MXZyZDlvdXAyNnhtNSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hTjzetNUv8La6OBm0D/giphy.gif")
        else:
            # Generate and display the Fibonacci sequence
            fibonacci_list = fibonacci(terms)
            print(f"Fibonacci sequence up to {terms} terms: {fibonacci_list}")
            # Sum and display the result
            result = add_fibonacci(fibonacci_list)
            print(f"Sum of the Fibonacci sequence: {result}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
