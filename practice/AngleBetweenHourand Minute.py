h, m = input('Enter time: ').split(':')
angle = abs(30 * int(h) - 5.5 * int(m))
print(min(angle, 360 - angle))


min1 = int(h) * 60 + int(m)
min1 = min1 / 2
min_degree=int(m)*6
print(abs(min1-min_degree))