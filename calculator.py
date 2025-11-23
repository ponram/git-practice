"""
Simple calculator program
Version 1.0 - Basic operations
"""
 # Updated on GitHub directly
def add(a, b):
    """Add two numbers with logging"""
    print(f"Adding {a} and {b}")
    return a + b

def subtract(a, b):
    """Subtract two numbers"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def main():
    print("Welcome to the Calculator")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")

if __name__ == "__main__":
    main()
