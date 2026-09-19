from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(slf, fro, to):
        print(f"The train {slf.trainNo} is booked from {fro} to {to}")

    def status(saad):
        print(f"The train {saad.trainNo} is running on time")

    def getFair(self, fro, to):
        print(f"The train fair for {self.trainNo} from {fro} to {to} is {randint(500, 1500)}")

t = Train(78676)
t.book("lahore", "RawalPindi")
t.status()
t.getFair("lahore", "RawalPindi")
