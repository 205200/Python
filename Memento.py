class Memento:
    def __init__(self, file, content):
        self.file = file  # Store the file path
        self.content = content  # Store the content of the file


class X:
    def __init__(self, file_path):
        self.file = file_path  # Initialize the file path
        self.content = ""  # Initialize an empty content

    def write(self, string):
        self.content += string  # Append new string to content

    def save(self):
        return Memento(self.file, self.content)  # Save the current state as a Memento

    def undo(self, memento):
        self.file = memento.file  # Restore the file path from the Memento
        self.content = memento.content  # Restore the content from the Memento


class Y:
    def save(self, x):
        self.mem = x.save()  # Save the current state of object X as a Memento

    def undo(self, x):
        x.undo(self.mem)  # Restore the state of object X from the Memento


if __name__ == '__main__':
    y = Y()  # Create object of Y
    x = X("GFG.txt")  # Create object of X with file path "GFG.txt"
    x.write("First vision of Data\n")  # Write content to file
    print(x.content + "\n\n")

    y.save(x)  # Save the state of object X
    x.write("Second vision of Data\n")  # Write additional content to file
    print(x.content + "\n\n")

    y.undo(x)  # Undo the changes made to object X
    print(x.content + "\n\n")  # Print the restored content
