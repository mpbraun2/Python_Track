class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayinfo(self):
        print self.price
        print self.max_speed
        print self.miles
    def ride(self):
        print "riding"
        self.miles += 10
    def reverse(self):
        print "reversing"
        self.miles -= 5
Bike1 = Bike(150, "40 mph")
Bike2 = Bike(200, "30 mph")
Bike3 = Bike(350, "50 mph")
Bike1.ride()
Bike1.ride()
Bike1.ride()
Bike1.reverse()
Bike1.displayinfo()

