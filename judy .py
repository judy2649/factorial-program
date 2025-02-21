//JUDITH ANYANGO OYOO
//EB3/61531/22
import time

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

number = 10  
start_time = time.time()
result = factorial(number)
end_time = time.time()

print(f"Factorial of {number} is {result}")
print(f"Runtime: {end_time - start_time} seconds")
