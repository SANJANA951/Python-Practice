from random import randint

class Train:

    def __init__(slf, trainno):
        slf.trainno = trainno


    def book(prince,  fro , to):
        print(f"Ticket is booked in train no :{prince.trainno} from {fro} to {to}")
        

    def getStatus(self ):
        print(f"Train no: {self.trainno} is running on time")
        

    def getFare(self,  fro, to):
        print(f"Ticket fare in train no: {self.trainno} form {fro} to {to} is {randint(222, 5555)}")


t = Train(123389)
t.book("Rampur", "Delhi")
t.getStatus()
t.getFare( "Rampur", "Delhi")