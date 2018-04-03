# test cases:
# excludingVatPrice(230) --> 200.00
# excludingVatPrice(123) --> 106.96

def excluding_vat_price(price):
    if price == None:
        return -1 
    else:
        return round(price / 1.15,2)
