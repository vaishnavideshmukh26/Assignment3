def factorial(num):
    if num==1:
        return 1
    else:
        fact_val=num*factorial(num-1)
        return fact_val

num=int(input("Enter a number "))
print(f"Factorial of {num} is: {factorial(num)}")