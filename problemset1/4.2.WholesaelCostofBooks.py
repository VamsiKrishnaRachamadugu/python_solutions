"""4.b) Suppose the cover price of a book is Rs.24.95, but bookstores get a 40% discount. Shipping costs
Rs.3 for the first copy and 0.75p for each additional copy. What is the total wholesale cost for
60 copies?"""
cover_price = 24.95
copies = 60
shipping_cost = 0.75
discount = 40
total_cost = cover_price * (3 + copies - 1 * shipping_cost)
after_discount = (discount / total_cost) * 100
print(after_discount)
