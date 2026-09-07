from loguru import logger
import math

length_of_land = 100
breadth_of_land = 100
bricks_cost_per_piece = 10.5
labor_m1 = 'abc'
labor_m2 = 'xyz'
is_home = True

# #Floor Division
# logger.info(15//6)

# #ceil value
# logger.info(math.ceil(15/6))
# #floor value
# logger.info(math.floor(15/6))
# #abs value
# logger.info(abs(-15/6))

#Type casting
a = '25'
b = 25

print(int(a) + b)
print(a + str(b))

#Implicit Type casting
x = 1.5
y = 5  # gets casted to float
print(x+y)


# User Input
length = input("Enter Length : ")
float_length = float(input("Enter Length : "))
