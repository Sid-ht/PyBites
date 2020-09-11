url = ('https://www.amazon.com/War-Art-Through-Creative-Battles/dp/1936891026/ref=sr_1_1?dchild=1&keywords=War+art+through+creative+battles&qid=1599849807&sr=8-1')

new_string = url.split('/')[2:-1]
print(new_string)

domain, *rest , asin = new_string
print(domain)
print(asin)
