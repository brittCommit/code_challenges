def add_digits(number):
  return number[0] + number[1]

def luhn10(card_number):
  """Validate if card_number is ..."""
  string_digits = list(card_number)
  string_digits.reverse()
  digits = []
  for c in string_digits:
    digits.append(int(c))
  doubled = []
  for i, d in enumerate(digits):
    if i % 2 == 1:
      val = d * 2
    else:
      val = d
    doubled.append(add_digits(val))
  
  return sum(doubled) % 10 == 0

class Account():
  def __init__(self, card_holder, card_number, limit, balance):
    self.card_holder = card_holder
    self.card_number = card_number
    self.limit = limit
    self.balance = balance

  def __repr__(self):
    return f'<cardholder: {self.card_holder}, limit: {self.limit}, balance:{self.balance}>'

  def charge(self, amount):
    """Increases the account balance by the specified amount.
    Raises ValueError if resulting balance exceeds limit."""

    if self.balance + amount > self.limit:
      raise ValueError('Limit exceeded: transaction declined.')
    self.balance += amount

  def credit(self, amount):
    """Decreases the account balance by the specified amount."""
    self.balance -= amount

class Provider:
  def __init__(self):
    self.accounts = {}
    
  def add(self, card_holder, card_number, limit):
    """Create account w/card_holder, card_number and limit, assume balance is 0,
    raises ValueError if card_number is invalid according to Luhn10 or if card_holder
    already exists."""
    if card_holder in self.accounts:
      raise ValueError(f'Account for {card_holder} already exists.')

    if not luhn10(card_number):
      raise ValueError(f'Card number {card_number} is invalid.')
    account = Account(card_holder, card_number, limit, 0)
    self.accounts[card_holder] = account

  def charge(self, card_holder, amount):
    """Increases the account balance for the given card_holder by the specified amount.
    Raises ValueError if card_holder does not have account or if resulting balance excedes limit."""
    if card_holder not in self.accounts:
      raise ValueError(f'Account for {card_holder} does not exist.')
    account = self.accounts[card_holder]
    account.charge(amount)

  def credit(self, card_holder, amount):
    """Decreases the account balance for the given card_holder by the specified amount.
    Raises ValueError if card_holder does not have account."""
    if card_holder not in self.accounts:
      raise ValueError(f'Account for {card_holder} does not exist.')
    account = self.accounts[card_holder]
    account.credit(amount)

def amount_to_int(amount):
  """Change amount from string to int"""
  return int(amount[1:])

def creditCardProvider(operations):
  provider = Provider()
  for operation in operations:
    try:
      if operation[0] == 'Add':
        card_holder = operation[1]
        card_number = operation[2]
        limit = amount_to_int(operation[3])
        provider.add(card_holder, card_number, limit)
      elif operation[0] == 'Charge':
        card_holder = operation[1]
        amount = amount_to_int(operation[2])
        provider.charge(card_holder, amount)
      elif operation[0] == 'Credit':
        card_holder = operation[1]
        amount = amount_to_int(operation[2])
        provider.credit(card_holder, amount)
    except ValueError as e:
      print(f'Operation {operation} failed with {e}')
  return provider

creditCardProvider([["Add","Tom","4111111111111111","$1000"], 
 ["Add","Lisa","5454545454545454","$3000"], 
 ["Add","Quincy","1234567890123456","$2000"], 
 ["Charge","Tom","$500"], 
 ["Charge","Tom","$800"], 
 ["Charge","Lisa","$7"], 
 ["Credit","Lisa","$100"], 
 ["Credit","Quincy","$200"]])
