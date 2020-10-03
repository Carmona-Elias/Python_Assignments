class Vehicle:
    def __init__(self, make, model, year, weight):
        self.Make = make
        self.Model = model
        self.Year = year
        self.Weight = weight
        self.NeedsMaintenance = False
        self.TripsSinceMaintenance = 0


    # Setters
    def setMake(self, make):

        self.Make = make

    def setModel(self, model):

        self.Model = model

    def setYear(self, year):

        self.Year = year

    def setWeight(self, weight):

        self.Weight = weight


    # Getters
    def getMake(self):
        return self.Make

    def getModel(self):
        return self.Model

    def getYear(self):
        return self.Year

    def getWeight(self):
        return self.Weight

    def getNeedsMaintenance(self):
        return self.NeedsMaintenance

    def getTripsSinceMaintenance(self):
        return self.TripsSinceMaintenance




class Cars(Vehicle):
    def __init__(self, make, model, year, weight):
        Vehicle.__init__(self, make, model, year, weight)

    def Drive(self):

        self.isDriving = True

    def Stop(self):

        self.isDriving = False

    def MaintenanceNeed(self):

        if self.isDriving == False:
            self.TripsSinceMaintenance += 1


    def maintenance(self):

        if self.TripsSinceMaintenance > 100:
            self.NeedsMaintenance = True

    def repair(self):
        self.TripsSinceMaintenance = 0
        self.NeedsMaintenance = False

class Planes(Vehicle):
    def __init__(self, make, model, year, weight):
        Vehicle.__init__(self, make, model, year, weight)

    def fly(self):

        self.isFlying = True

    def land(self):

        self.isFlying = False


    def flyingAttempt(self):

        if self.NeedsMaintenance == True:
            return False

    def __str__(self):
        return ('The Plane cannot fly until its is repaired')
