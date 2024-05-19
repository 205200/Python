import time
import multiprocessing


# Function to calculate squares of numbers in a list
def calc_square(numbers):
    for n in numbers:
        print('square ' + str(n * n))
        time.sleep(3)  # Simulate a time-consuming task


# Function to calculate cubes of numbers in a list
def calc_cube(numbers):
    for n in numbers:
        print('cube ' + str(n * n * n))
        time.sleep(3)  # Simulate a time-consuming task


# Entry point of the script
if __name__ == "__main__":
    arr = [2, 3, 8]  # List of numbers to process

    t = time.time()  # Record start time

    # Create two processes that will run calc_square and calc_cube respectively
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))

    p1.start()  # Start process p1
    p2.start()  # Start process p2

    p1.join()  # Wait for p1 to finish
    p2.join()  # Wait for p2 to finish

    # Print total time taken to execute both processes
    print("done in : ", time.time() - t)

    # Output the number of CPUs available on this machine
    print("The number of CPU currently working in system : ", multiprocessing.cpu_count())
