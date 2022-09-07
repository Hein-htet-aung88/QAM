

num_1 = input("Enter a number: ")
num_2 = input("Enter a second number: ")
result = float(pow(float(num_2),float(num_1)))
print(result)

#better calculator
no1 = float(input("Enter first number:"))
no2 = float(input("Enter second number:"))
op = input("Enter operator:")

if op == "+":
    print((no1 + no2))
elif    op =="-":
    print(no1-no2)
elif op == "*":
    print(no1*no2)
elif op ==("/"):
    print(no1/no2)
elif op == "^":
    print(pow(no1,no2))

else:
    print("Error")