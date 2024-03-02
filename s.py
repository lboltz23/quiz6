class Customer:
    def __init__(self,name, address, email):
        self.name = name
        self.address = address
        self.email = email

class Item:
    def __init__(self, name, quantity, price):
       self.name = name
       self.price = price
       self.quantity = quantity
       
        
class Stock:
    def __init__(self, stock):
        self.stock = stock
    def update_stock(self, quantity):
        self.stock += quantity   

class Cart:
    def __init__(self):
        self.items = []
    def addItem(self, item):
        self.items.append(item)
    def removeItem(self, item):
        self.items.remove(item)
    def getItems(self):
        return self.items
    
class Cost:
    def __init__(self, tax, discount):
        self.tax = tax
        self.discount = discount
    def calculatePrice(self):
        price = self.quantity * self.price
        tax = price * self.tax
        total = (price + tax) * self.discount
        return total
    
class ConfirmationEmails:
    def __init__(self, email_service):
        self.email_service = email_service
    def send_confirmation(self, order, email):
        self.email_service.send_email(email, "Order confirmed")

class OrderData(Stock, Item):
    def __init__(self, tax, discount, email_service):
        self.cart = Cart()
        self.priceCalculate = Cost(tax, discount)
        self.sendemail = ConfirmationEmails(email_service)

    def addCart(self, item, quantity):

        if self.stock>= quantity:
            self.update_stock(-quantity)
            self.cart.addItem(self, item)
        else:
            print("Not enough stock")

    def getCart(self):
        return self.cart.getItems()

    def place_order(self):
        total = self.priceCalculate.calculatePrice(self.cart)
        self.sendemail.send_confirmation(self.cart, self.user.email)
        self.cart.clear()


def main():
    order = OrderData(0.05, 0.10, "randomemailservice")

    item1= Item("apple", 50, 1.00)
    item2=Item("banana", 25, 3.00)
    item3=Item("orange", 60, 1.00)
    
    order.update_stock(item1.quantity)

    customer = Customer("John Doe", "123 Street", "jdoe@email.com")

    order.addCart("apple", 2)
    order.addCart("orange", 15)
    

    print(order.getCart())
    order.place_order()
    


if __name__ == "__main__":
    main()