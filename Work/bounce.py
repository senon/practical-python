# bounce.py
#
# Exercise 1.5

height = 100 # meters
num_bounce = 0

while num_bounce < 10:
    num_bounce = num_bounce + 1
    height = height * (3/5)
    print(num_bounce, round(height, ndigits=4))

