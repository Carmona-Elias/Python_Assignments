class Vehicle:
    def __init__(self, make, model, year, weight, needsMaintenance = False, tripsSinceMaintenance = 0):
        self.Make = make
        self.Model = model
        self.Year = year
        self.Weight = weight
        self.NeedsMaintenance = needsMaintenance
        self.TripsSinceMaintenance = tripsSinceMaintenance


    # Setters
    def setMake(self, make):

        self.Make = make

    def setModel(self, model):

        self.Model = model

    def setYear(self, year):

        self.Year = year

    def setWeight(self, weight):

        self.weight = weight

    def setNeedM(self, needMaintenance):

        self.NeedsMaintenance = needMaintenance

    def setTripsM(self, tripsMaintenance):

        self.TripsSinceMaintenance = tripsMaintenance


class Cars(Vehicle):
    def __init__(self, make, model, year, weight, needsMaintenance = False , tripsSinceMaintenance = 0):
        Vehicle.__init__(self, make, model, year, weight, needsMaintenance, tripsSinceMaintenance)


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
    def __init__(self, make, model, year, weight, needsMaintenance = False, tripsSinceMaintenance = 0):
        Vehicle.__init__(self, make, model, year, weight, needsMaintenance, tripsSinceMaintenance)

    def fly(self):

        self.isFlying = True

    def land(self):

        self.isFlying = False


    def flyingAttempt(self):

        if self.NeedsMaintenance == True:
            return False

    def __str__(self):
        return ('The Plane cannot fly until its is repaired')


car1 = Cars('Mercedes', 'Compressor', 2002, 3500)
car1.Drive()
car1.Drive()
car1.Drive()
car1.Drive()
car1.Drive()
print(car1.Make)
print(car1.Model)
print(car1.Year)
print(car1.Weight)
print(car1.NeedsMaintenance)
print(car1.TripsSinceMaintenance)
car2 = Cars('BMW', 'X5', 2012, 7450)
car2.Drive()
car2.Drive()
car2.Drive()

print(car2.Make)
print(car2.Model)
print(car2.Year)
print(car2.Weight)
print(car2.NeedsMaintenance)
print(car2.TripsSinceMaintenance)

car3 = Cars('Ford', 'Wild Track', 2015, 8900)
car3.Drive()
car3.Drive()
car3.Drive()
car3.Drive()

print(car3.Make)
print(car3.Model)
print(car3.Year)
print(car3.Weight)
print(car3.NeedsMaintenance)
print(car3.TripsSinceMaintenance)



