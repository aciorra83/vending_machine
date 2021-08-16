'''
The VendingMachine class constructor should take on parameter:
passowrd Inside the constructor, add three fields: balance, password, and items. 
Balance should be initialized to 0, and items should be initialized to an empty list. 

Add an add_item method for the admin, that takes in a name, price and password:
-Assume the name is a string, and that the price is always positive (either int or float)
-If the password is incorrect, print the message "Incorrect Password"
-Else, create a new item object with the name and price, and add it to the list of items

Add a purchase_item method for the user, that takes in an index, and pay:
-Assume the index is positive and within range, and that pay is always a positive int/float
-If the pay is not sufficient, return a tuple (None, pay)
-Else, make the transaction by adding the item price to balance and return a tuple (item, change)

The __str__ operator should return a string to display the vending machine details in the following format:
Vending Machine Balance: (balance)
(item 1) : (price 1)
(item 2) : (price 2)

Hint: use a for loop to iterate through the items and add the newline '\n' to each line
'''


# constructor of the vending machine item class
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# returns an output of the item 'name': price
    def __str__(self):
        return self.name + ": " + str(self.price)

    def __repr__(self):
        return str(self)


class VendingMachine:
    def __init__(self, password):
        self.balance = 0
        self.password = password
        self.items = []

    def add_items(self, name, price, password):
        if self.password != password:
            print('Incorrect Password')
        else:
            item = Item(name, price)
            self.items.append(item)

    def purchase_items(self, index, pay):
        item = self.items[index]
        if (item.price > pay):
            return (None, pay)
        else:
            self.balance += item.price
            change = pay - item.price
            return (item, change)

    def __str__(self):
        info = 'Vending Machine Balance: ' + str(self.balance) + '\n'
        for item in self.items:
            info += str(item) + '\n'

        return info


# TEST CODE
my_password = 'apple'
wrong_password = 'banana'

vm = VendingMachine(my_password)

vm.add_items('Oreos', 1.25, my_password)
vm.add_items('Lays Chips', 1.5, my_password)
vm.add_items('Coke', 1.75, my_password)
vm.add_items('Milky-Way', 1.25, my_password)
vm.add_items('Cheetos', 1.5, wrong_password)  # incorrect password
vm.add_items('Gatorade', 1.5, my_password)
vm.add_items('oreos', 1.25, my_password)

# Initial vendign machine balance
print('\nBefore:')
print(vm)


# Item purchases                 # expected outputs
print(vm.purchase_items(0, 1))  # (None, 1)
print(vm.purchase_items(0, 1.5))  # (Oreos: 1.25, 0.25)
print(vm.purchase_items(4, 2.50))  # (Gatorade: 1.5, 1)
print(vm.purchase_items(1, 1.5))  # (Lays Chips: 1.5, 0)
print(vm.purchase_items(2, 50))  # (Coke: 1.75, 48.25)

# Vending machine balance after purchases
print('\nAfter:')
print(vm)
