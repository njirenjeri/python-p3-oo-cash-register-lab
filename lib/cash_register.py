#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount = 0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = 0
    
    def add_item(self, item, price, quantity = 1):
        '''Adds item to the register with its price and quantity'''
        self.total += (price * quantity)
        self.items.extend([item] * quantity)
        self.last_transaction = price * quantity #saves last transaction
        
    def apply_discount(self):
        '''Applies the discount to the total price'''
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            print(f'After the discount, the total comes to ${self.total:.0f}.')
        else:
            print('There is no discount to apply.')

    def void_last_transaction(self):
        '''Removes last added transaction from total'''
        self.total -= self.last_transaction
        self.last_transaction = 0 #reset last transaction

  # def __init__(self, item_name, quantity, price):
  #   self.item_name = item_name
  #   self.quantity = quantity
  #   self.price = price
  #   self.items = []
