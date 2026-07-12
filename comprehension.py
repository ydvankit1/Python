# list comprehensions    (for memory optimization and clean one line code)

# [expression for item in iterable if condition]

itm = ["fruit apple", "fruit banana", "vege tomato"]

fruits = [frt for frt in itm if "fruit" in frt]
print(fruits)

# set comprehensions

items={"apple", "mango", "oranges", "papaya"}
itm={frt for frt in items if len(frt)>5}
print(itm)

# dictionary comprehensions

price_inr={
    "apple": 50,
    "banana": 60,
    "mango": 70
}
price_usd={i: price/80 for i, price in price_inr.items()}
print(price_usd)
