class Vehicle():
    vIdNum = int(10)
    vRented = []

    def __init__(self, newMake, newModel, newYear, newRego, newCost, newOdo):
        self.vID = Vehicle.vIdNum
        Vehicle.vIdNum += 5
        self.vMake = newMake
        self.vModel = newModel
        self.vYear = newYear
        self.vRego = newRego
        self.vCost = newCost    #cost to rent per day
        self.vOdo = newOdo
        self.vRenter = None     # rental client
        self.vStatus = True     # True = In, False = Out

    def getVMoney(self):
        print("${:,.2f".format(self.vCost))