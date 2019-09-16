h, m = input('Enter time: ').split(':')
angle = abs(30 * int(h) - 5.5 * int(m))
print(min(angle, 360 - angle))
