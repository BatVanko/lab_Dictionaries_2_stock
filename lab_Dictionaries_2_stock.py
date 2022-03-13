products = input().split(" ")
stock = {}

for i in range(0, len(products), 2):
    product = products[i]
    quantities = products[i + 1]
    if product not in stock.keys():
        stock[product] = quantities

searched_products = input().split(" ")
for product in searched_products:
    if product in stock.keys():
        print(f"We have {stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
