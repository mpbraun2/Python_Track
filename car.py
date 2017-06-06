class Car(object):
    def __init__(self, price, speed, fuel, mileage, tax):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = tax
    def display_all(self):
        print "Price:",
        print self.price
        print "Speed:",
        print self.speed
        print "Fuel:",
        print self.fuel
        print "Mileage:",
        print self.mileage
        print "Tax:",
        print self.tax

Car1 = Car(10000, "55 mph", "full", 95000, .15)
Car2 = Car(12000, "65 mph", "full", 65000, .15)
Car3 = Car(18000, "85 mph", "half-full", 35000, .15)
Car4 = Car(6000, "45 mph", "empty", 100000, .12)
Car5 = Car(22000, "105 mph", "full", 28000, .15)
Car6 = Car(45000, "200 mph", "empty", 10000, .15)

print "Car 1" 
str(Car1.display_all())
print "Car 2"
str(Car2.display_all())
print "Car 3"
str(Car3.display_all())
print "Car 4"
str(Car4.display_all())
print "Car 5"
str(Car5.display_all())
print "Car 6"
str(Car6.display_all())
