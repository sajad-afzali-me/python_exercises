import math

r = float(input("'Enter the radius of the circle'\nr: "))
if r <= 0:
    print("ERROR: radius must be a positive number!")
else:
    area = math.pi * (r**2)
    circumference = 2 * math.pi * r
    print(f"Circle Area:{area:.2f}")
    print(f"Circle Circumference:{circumference:.2f}")
