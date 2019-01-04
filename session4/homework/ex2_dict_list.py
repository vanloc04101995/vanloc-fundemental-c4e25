prices = {
    "banana" : 4,
    "apple"  : 2,
    "orange" : 1.5,
    "pear"   : 3
}
stock = {
    "banana" : 6,
    "apple"  : 0,
    "orange" : 32,
    "pear"   : 15
}
total = 0

for key,val in prices.items():
    print(key)
    print("price :",val)
    print("stock :",stock[key])
    total += float(val * stock[key])
print("Money earned from buying fruits:")
print(total)
     