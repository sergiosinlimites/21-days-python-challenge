from pay import Pay

class Cash(Pay):
  def make_pay(self, amount):
    return {
      "realized": True,
      "quantity": amount
    }
