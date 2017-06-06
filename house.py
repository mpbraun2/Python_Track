class House(object):
    def __init__(self, listing_price, square_ft):
        self.listing_price = listing_price
        self.square_ft = square_ft
        self.bedrooms = 1

    def display_info(self):
        print self.listing_price, self.square_ft, self.bedrooms

        return self

    def set_bdrm(self, amount):
        self.bedrooms = amount

        return self