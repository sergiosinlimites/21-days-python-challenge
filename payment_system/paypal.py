from pay import Pay

class PayPal(Pay):
  # Tu código aquí 👇
  def __init__(self, email):
    self.email = email

  def make_pay(self, amount):
    self.platform = "PayPal"
    self.realized = True
    self.amount = amount
    return {
      "realized": self.realized,
      "quantity": self.amount,
      "platform": self.platform,
      "email": self.email
    }