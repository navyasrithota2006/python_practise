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
        for i in range(1,n+1):
            fact *= i
        return fact
    
def fibonnacci(n):
    if n<0:
        print("Fibonacci is not defined for negative numbers")
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        a,b=0,1
        for _ in range(2,n+1):
            a,b=b,a+b
        return b

def prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
        break
    return True


def palindrome(s):
    s=s.replace(" ","").lower()
    return s==s[::-1]


print(printHello("Alice"))
print(evenorodd(5))
print(evenorodd(6))
print(factorial(5))
print(fibonnacci(5))
print(prime(7))
print(prime(10))
print(palindrome("raZar"))