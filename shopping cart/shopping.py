class Product:

  def __init__(self, name, price):
    self.name = name
    self.price = price

  def __str__(self):
    return self.name

class CartItem:
  
  def __init__(self, product, quantity):
    self.product = product
    self.quantity = quantity

  def value(self):
    return self.product.price * self.quantity

  def __str__(self):
    return "{}: {} x {} = {}".format(self.product.name, self.product.price, self.quantity, self.value())

class Cart:
  def __init__(self):
    self.cart = {}

  def add(self, product, quantity=1):
    if product in self.cart:
      self.cart[product].quantity + quantity
    else:
      self.cart[product] = CartItem(product, quantity)

  def remove(self, product, quantity=1):
    if product not in self.cart:
      return
    self.cart[product].quantity -= quantity
    if self.cart[product].quantity <= 0:
      del self.cart[product]

  def __str__(self):
    res = ""
    total = 0
    for x in self.cart:
      total += self.cart[x].value()
      res += str("{}\n".format(self.cart[x]))
    return "CART | total = {}\n".format(total) + res

if __name__ == "__main__":
  pizza = Product("Pizza", 10)
  wing = Product("Chicken Wing", 2)
  pasta = Product("Pasta", 5)

  cart = Cart()
  cart.add(pizza, 5)
  cart.add(pasta, 3)
  cart.add(wing, 12)
  print(cart)
  cart.remove(pizza, 4)
  print(cart)
  cart.remove(pizza, 1)
  print(cart)

