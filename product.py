class Product(object):
    def __init__(self, price, item_name, weight, brand, cost, return_reason):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"
        self.return_reason = return_reason

    def sell(self, status):
        self.status = "sold"
    def add_tax(self):
        self.price = self.price*1.18
    def returns(self, defective, opened):
        return add_tax(self)
        self.defective = defective
        self.opened = opened
    #takes reason for return as a parameter and returns the price of
    #the item + sales tax. Change status to defective and change price to 0.
    #if item is returned in box, mark for sale. If box is open, mark at 20% discount
    def display_info(self):
        print self.price, self.item_name, self.weight, self.brand, self.cost, self.status

product1 = Product(18.99, "Ham", 10, "Honeyhills", 10.99)
product2 = Product(14.99, "Steak", 12, "Angus", 10.99)
product3 = Product(10.99, "Turkey", 8, "Thanksgiving Day", 7.99)
product4 = Product(8.99, "Salami", 1, "Italian Homes", 6.99)
product5 = Product(30.99, "Beef", 3, "Wagyu", 20.99)
product6 = Product(1.99, "Chicken", 9, "Bwack", .99)
product7 = Product(4.99, "Venison", 4, "Deer Hunter", 2.99)
product8 = Product(6.99, "Fish", 10, "Franks Fish Farm", 4.99)

product1.add_tax()
product1.display_info()
product2.display_info()
product3.display_info()
product4.display_info()
product5.display_info()
product6.display_info()
product7.display_info()
product8.display_info()
