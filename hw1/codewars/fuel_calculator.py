# In this kata you will have to write a function that takes litres and pricePerLiter as arguments.
# Purchases of 2 or more litres get a discount of 5 cents per litre, purchases of 4
# or more litres get a discount of 10 cents per litre,
# and so on every two litres, up to a maximum discount of 25 cents per litre.
# But total discount per liter cannot be more than 25 cents. round answer to 2 decimal places.
# Also you can guess that there will not be negative or non-numeric inputs.
#

def fuel_price(litres, price_per_liter):
    total = litres * price_per_liter
    if litres >= 10:
        return total - litres * 0.25
    elif litres >= 8:
        return total - litres * 0.20
    elif litres >= 6:
        return total - litres * 0.15
    elif litres >= 4:
        return total - litres * 0.10
    elif litres >= 2:
        return total - litres * 0.05

print(fuel_price(10, 21.5))