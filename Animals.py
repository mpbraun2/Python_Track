class animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = 100
    def walk(self):
        self.health = self.health - 1
        print self.health
    def run(self):
        self.health = self.health - 5
        print self.health
    def displayHealth(self):
        print self.name, self.health
class dog(animal):
    def pet(self):
        self.health = self.health + 5
class dragon(animal):
    def fly(self):
        self.health = self.health - 10

Dragon = dragon("Drew", 170)
Dog = dog("Norbert", 150)

Dragon.walk()
Dragon.walk()
Dragon.walk()
Dragon.run()
Dragon.run()
Dragon.displayHealth()
Dog.walk()
Dog.walk()
Dog.walk()
Dog.run()
Dog.run()
Dog.pet()
Dog.displayHealth()
Dragon.walk()
Dragon.walk()
Dragon.walk()
Dragon.run()
Dragon.run()
Dragon.fly()
Dragon.fly()
Dragon.displayHealth()
