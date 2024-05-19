# Facade pattern with an example of WashingMachine

class Washing:
    '''Subsystem #1'''

    def wash(self):
        print("Washing...")


class Rinsing:
    '''Subsystem #2'''

    def rinse(self):
        print("Rinsing...")


class Spinning:
    '''Subsystem #3'''

    def spin(self):
        print("Spinning...")


class WashingMachine:
    '''Facade'''

    def __init__(self):
        # Instantiate the subsystems
        self.washing = Washing()
        self.rinsing = Rinsing()
        self.spinning = Spinning()

    def startWashing(self):
        # Start the washing process by calling subsystem methods
        self.washing.wash()
        self.rinsing.rinse()
        self.spinning.spin()

    # Main method


if __name__ == "__main__":
    # Create an instance of the WashingMachine and start washing
    washingMachine = WashingMachine()
    washingMachine.startWashing()
