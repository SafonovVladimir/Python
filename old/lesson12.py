prices = {'apple': 0.75, 'egg': 0.50}
cart = {
  'apple': 1,
  'egg': 6
}

bill = sum(prices[item] * cart[item]
           for item in cart)

print(f'I have to pay {bill:.2f}')