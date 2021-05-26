class Basket:
    def __init__(self, id):
        self.id = id
        global titlePrice
        global total
        self.titlePrice = {}
        self.total = 0
        self.price = 0

    def add(self, title, price):
        self.total = self.total + price
        self.titlePrice[title] = price

    def delete(self, title):
        self.total = self.total - int(self.titlePrice[title])
        del self.titlePrice[title]

    def showBasket(self):
        print("****************************************")
        for key, val in self.titlePrice.items():
            print("Title: %s, Price: KRW %s" %(key, val))
        print("----------------------------------------")
        print("Total price = KRW %s" %(self.total))
        print("****************************************")
        print("")

leeBasket = Basket('Lee')
leeBasket.add("Momo", 6500)
leeBasket.showBasket()
leeBasket.add('Little Prince', 5000)
leeBasket.showBasket()
leeBasket.add('Harry Potter', 8500)
leeBasket.showBasket()
leeBasket.delete('Little Prince')
leeBasket.showBasket()