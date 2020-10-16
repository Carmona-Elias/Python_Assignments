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
        if self.TripsSinceMaintenance > 100:
            self.NeedsMaintenance = True
            return self.NeedsMaintenance
        else:
            return False

    def getTripsSinceMaintenance(self):
        return self.TripsSinceMaintenance




class Cars(Vehicle):
    def __init__(self, make, model, year, weight):
        Vehicle.__init__(self, make, model, year, weight)
        self.isDriving = False

    def Drive(self):

        self.isDriving = True

    def Stop(self):

        self.isDriving = False


    def getDrive(self):

        if self.isDriving == False:
            self.TripsSinceMaintenance += 1
            return self.TripsSinceMaintenance



    def repair(self):
        self.TripsSinceMaintenance = 0
        self.NeedsMaintenance = False


class Planes(Vehicle):
    def __init__(self, make, model, year, weight):
        Vehicle.__init__(self, make, model, year, weight)
        self.isFlying = False
    def fly(self):

        self.isFlying = True


    def land(self):

        self.isFlying = False


    def Maintenance(self):
        if self.isFlying == False:
            self.TripsSinceMaintenance += 1


    def flyingAttempt(self):

        if self.NeedsMaintenance == True:
            print('The plane cannot fly, it needs to be repaired')
            return False


car1 = Cars('Mercedes', 'Compressor', 1992, 3500)
car2 = Cars('BMW', 'X5', 2012, 4300)
car3 = Cars('Toyota', 'Mark X', 2015, 3500)

Trips = car1.getDrive()
Trips = car1.getDrive()

print('----- Car 1  Data -----')
print(car1.getMake())
print(car1.getModel())
print(car1.getYear())
print(car1.getWeight())
print(car1.getNeedsMaintenance())
print(car1.getTripsSinceMaintenance())

Trips = car2.getDrive()
Trips = car2.getDrive()
Trips = car2.getDrive()

print('----- Car 2  Data -----')
print(car2.getMake())
print(car2.getModel())
print(car2.getYear())
print(car2.getWeight())
print(car2.getNeedsMaintenance())
print(car2.getTripsSinceMaintenance())

Trips = car3.getDrive()
Trips = car3.getDrive()
Trips = car3.getDrive()
Trips = car3.getDrive()
Trips = car3.getDrive()
Trips = car3.getDrive()

print('----- Car 3  Data -----')
print(car3.getMake())
print(car3.getModel())
print(car3.getYear())
print(car3.getWeight())
print(car3.getNeedsMaintenance())
print(car3.getTripsSinceMaintenance())


