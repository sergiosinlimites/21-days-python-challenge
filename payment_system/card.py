from pay import Pay

class Card(Pay):
  # Tu código aquí 👇
  def __init__(self, card_number):
    self.card_number = card_number

  def make_pay(self, amount):
    if(len(self.card_number) == 16):
      self.amount = amount
      self.realized = True
      return {
        "quantity": self.amount,
        "realized": self.realized,
        "last_card_numbers": self.card_number[-4:]
      }
    else:
      raise Exception
    
