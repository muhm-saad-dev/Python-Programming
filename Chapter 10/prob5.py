from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"The train {self.trainNo} is booked from {fro} to {to}")

    def status(self):
        print(f"The train {self.trainNo} is running on time")

    def getFair(self, fro, to):
        print(f"The train fair for {self.trainNo} from {fro} to {to} is {randint(500, 1500)}")

t = Train(78676)
t.book("lahore", "RawalPindi")
t.status()
t.getFair("lahore", "RawalPindi")
