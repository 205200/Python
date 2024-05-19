
import time  # Import necessary module for timing and sleeping

# Function to calculate and print squares of numbers
def calc_square(numbers):
    print("Calculating square numbers")
    for n in numbers:
        print('square:', n * n)
        time.sleep(0.2)  # Simulate time delay

# Function to calculate and print cubes of numbers
def calc_cube(numbers):
    print("Calculating cube of numbers")
    for n in numbers:
        print('cube:', n * n * n)
        time.sleep(0.2)  # Simulate time delay

# List of numbers
arr = [2, 3, 8, 9]

# Start timing the operations
t = time.time()

# Perform calculations
calc_square(arr)
calc_cube(arr)

# Print total time taken
print("done in : ", time.time() - t)
print("Hah... I am done with all my work now!")
