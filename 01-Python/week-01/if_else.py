import math

length_of_land = 100
breadth_of_land = 100
bricks_cost_per_piece = 10.5
labor_m1 = 'abc'
labor_m2 = 'xyz'
is_home = True

length_of_land = int(input("Enter length of land: "))

if length_of_land < 100:
    print("Length is not sufficient")
    if length_of_land > 80:
        print("A little less")
    else:
        print("Its done bro!")
elif length_of_land >= 500:
    print("More than enough")
else:
    print("Can Proceed")

