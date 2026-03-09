def printHello(name):
    return f"Hello, {name}!"

def evenorodd(num):
    result = f'{num} is {"even" if num%2==0 else "odd"}'
    return result

print(printHello("Alice"))
print(evenorodd(5))
print(evenorodd(6))