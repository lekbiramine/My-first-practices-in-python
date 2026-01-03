# def dis(price, discount):
#     discount /= 100
#     return round(price - (price * discount), 2)
# print(dis(89,20))

def dis(price: float, discount: float) -> float:
    discount_rate = discount / 100
    final_price = price * (1 - discount_rate)
    return round(final_price, 2)
print(dis(89,20))

# Instead of:
# price - price * rate
# You can write:
# price * (1 - rate)