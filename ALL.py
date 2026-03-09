def printHello(name):
    return f"Hello, {name}!"

def evenorodd(num):
    result = f'{num} is {"even" if num%2==0 else "odd"}'
    return result

def factorial(n):
    if n<0:
        print("factorial is not defined for negative numbers")
    elif n==0 or n==1:
        return 1
    else:
        fact =1
        for i in range(n):
            fact *= i
        return fact
    


print(printHello("Alice"))
print(evenorodd(5))
print(evenorodd(6))
print(factorial(5))