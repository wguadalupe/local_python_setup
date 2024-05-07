# Function to greet the user
def hello():
    print("Hello, User!")

# Function to pack three arguments into a list
def pack(a, b, c):
    return [a, b, c]

# Function to eat lunch from a list of items
def eat_lunch(lunch_items):
    if not lunch_items:
        print("My lunchbox is empty!")
    else:
        print(f"First I eat {lunch_items[0]}")
        for item in lunch_items[1:]:
            print(f"Next I eat {item}")

# Test the functions
hello()  # Call the hello function to print a greeting

# Call the pack function and print its output
packed_items = pack('apple', 'banana', 'sandwich')
print(packed_items)  # Output should be ['apple', 'banana', 'sandwich']

# Call the eat_lunch function with a list of items
eat_lunch(['apple', 'banana', 'sandwich'])  # Outputs eating sequence

# Call the eat_lunch function with an empty list
eat_lunch([])  # Outputs "My lunchbox is empty!"
