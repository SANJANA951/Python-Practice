from random import randint

class Train:

    def __init__(self, trainno):
        self.trainno = trainno


    def book(self,  fro , to):
        print(f"Ticket is booked in train no :{self.trainno} from {fro} to {to}")
        

    def getStatus(self ):
        print(f"Train no: {self.trainno} is running on time")
        

    def getFare(self,  fro, to):
        print(f"Ticket fare in train no: {self.trainno} form {fro} to {to} is {randint(222, 5555)}")


t = Train(123389)
t.book("Rampur", "Delhi")
t.getStatus()
t.getFare( "Rampur", "Delhi")