price_of_cars_in_dollars = {"BMW" : 110000, "Merc" : 160000, "Porsche" : 200000, "Mclaren" : 140000, "Lambo" : 300000}

max_price = max(price_of_cars_in_dollars, key=price_of_cars_in_dollars.get)
print(max_price)

#Walrus operator
max_price = max((e:=price_of_cars_in_dollars), key=e.get)
print(max_price)
