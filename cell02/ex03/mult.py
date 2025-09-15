num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
summ = num1*num2

if summ > 0:
    ans = "positive"
elif summ < 0:
    ans = "negative"
else:
    ans = "positive and negative"

print(f"{num1} x {num2} = {summ}")
print(f"The result is {ans}.")