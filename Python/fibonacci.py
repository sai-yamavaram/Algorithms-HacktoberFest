def fibonacci(n):
    if n<0:
        print('Only Positive Numbers have corresponding fibonacci numbers')
    if n==1 or n==0:
        return n
    return fibonacci(n-1)+fibonacci(n-2)


# n = int(input().strip())   # Taking Input from User
for i in range(10):
    print(fibonacci(i)) # Displaying Nth Fibonacci Number