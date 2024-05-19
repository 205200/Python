import threading

# Global variable x
x = 0

def increment():
    """ Increment the global variable x """
    global x
    x += 1

def thread_task(lock):
    """
    Thread task: calls increment function 100,000 times,
    ensuring exclusive access via lock.
    """
    for _ in range(100000):
        lock.acquire()  # Acquire lock before accessing x
        increment()
        lock.release()  # Release lock after updating x

def main_task():
    global x
    x = 0  # Reset x to zero

    # Create a lock object
    lock = threading.Lock()

    # Initialize threads with the lock
    t1 = threading.Thread(target=thread_task, args=(lock,))
    t2 = threading.Thread(target=thread_task, args=(lock,))

    # Start threads
    t1.start()
    t2.start()

    # Wait for threads to complete
    t1.join()
    t2.join()

if __name__ == "__main__":
    for i in range(10):  # Run the main task 10 times
        main_task()
        print(f"Iteration {i}: x = {x}")
