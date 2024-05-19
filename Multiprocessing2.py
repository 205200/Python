import multiprocessing


def sender(conn, msgs):
    """
    Function to send messages to other end of pipe.

    Args:
    - conn: The connection endpoint to send messages.
    - msgs: List of messages to be sent.
    """
    for msg in msgs:
        conn.send(msg)  # Send message through the connection
        print("Sent the message: {}".format(msg))
    conn.close()  # Close the connection after sending all messages


def receiver(conn):
    """
    Function to print the messages received from the other end of pipe.

    Args:
    - conn: The connection endpoint to receive messages.
    """
    while True:
        msg = conn.recv()  # Receive message from the connection
        if msg == "END":  # Break the loop if "END" message is received
            break
        print("Received the message: {}".format(msg))


if __name__ == "__main__":
    # Messages to be sent
    msgs = ["hello", "hey", "hru?", "END"]

    # Creating a pipe
    parent_conn, child_conn = multiprocessing.Pipe()  # Pipe returns two connection objects

    # Creating new processes
    p1 = multiprocessing.Process(target=sender, args=(parent_conn, msgs))
    p2 = multiprocessing.Process(target=receiver, args=(child_conn,))

    # Starting processes
    p1.start()  # Start the sender process
    p2.start()  # Start the receiver process

    # Wait until processes finish
    p1.join()  # Wait for the sender process to finish
    p2.join()  # Wait for the receiver process to finish
