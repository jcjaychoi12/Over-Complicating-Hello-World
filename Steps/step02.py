# Step 02: Arithmetic Operations and Type Conversion

name: str = input("What's your name? --- ")

fav_num_1: int = int(input("What's your favorite number? --- "))
fav_num_2: int = int(input("What's your 2nd favorite number? --- "))

add: int = fav_num_1 + fav_num_2
subtract: int = fav_num_1 - fav_num_2
multiply: int = fav_num_1 * fav_num_2
normal_divide: float = fav_num_1 / fav_num_2
integer_divide: int = fav_num_1 // fav_num_2
modulus: int = fav_num_1 % fav_num_2
exponent: int = fav_num_1 ** fav_num_2

print("Hello, " + name + "!")

print("Here are the results from using your favorite numbers in different operations: ")
print("Addition: " + str(add))
print("Subtraction: " + str(subtract))
print("Multiplication:", multiply)
print("Division:", normal_divide)
print("Integer Division:", integer_divide)
print("Modulus:", modulus)
print("Exponent:", exponent)