#judith Anyango Oyoo
# eb3/61531/22
import time

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = [0, 1]
        while len(fib_seq) < n:
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq

n = 10  
start_time = time.time()
result = fibonacci(n)
end_time = time.time()
runtime = end_time - start_time

print(f"Fibonacci sequence of length {n} is {result}")
print(f"Runtime: {runtime} seconds")

