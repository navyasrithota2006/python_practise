def print_square(n):
    for i in range(n):
        for j in range(n):
            print('* ',end='')
        print()

def triangleprint(n):
    for i in range(1,n+1):
        for j in range(i):
            print('*',end=' ')
        print()

def triangle_numbers(n):
    for i in range(1,n+1):
        for j in range(i):
            print(j+1,end=' ')
        print()

def triangle_numers2(n):
    for i in range(1,n+1):
        for j in range(i):
            print(i,end=' ')
        print()

def reverse_triangle_print(n):
    for i in range(1,n+1):
        for j in range(n-i+1):
            print('*',end=' ')
        print()

def reverse_triangle_numbers(n):
    for i in range(1,n+1):
        for j in range(n-i+1):
            print(j+1,end=' ')
        print()

def pyramid(n):
    for i in range(n):
        for j in range(n-i-1):
            print(' ',end=' ')
        for j in range(2*i+1):
            print('*',end=' ')
        for j in range(n-i-1):
            print(' ',end=' ')
        print()

def reverse_pyramid(n):
    for i in range(n):
        for j in range(i):
            print(' ',end=' ')
        for j in range(2*(n-i)-1):
            print('*',end=' ')
        for j in range(i):
            print(' ',end=' ')
        print()

def diamond(n):
    for i in range(n):
        for j in range(n-i-1):
            print(' ',end=' ')
        for j in range(2*i+1):
            print('*',end=' ')
        for j in range(n-i-1):
            print(' ',end=' ')
        print()
    for i in range(n):
        for j in range(i):
            print(' ',end=' ')
        for j in range(2*(n-i)-1):
            print('*',end=' ')
        for j in range(i):
            print(' ',end=' ')
        print()

        #or call the functions or pyramid and reverse pyramid functions to print the diamond pattern
        # pyramid(n)
        # reverse_pyramid(n)

def left_triangle(n):
    for i in range(1,2*n):
        stars =i
        if i>n: stars = 2*n-i
        for j in range(stars):
            print('*',end=' ')
        print()


'''def triangle_numbers_0or1(n):
    for i in range(n):'''




t=int(input())
for _ in range(t):
    n=int(input())
    print('Square Pattern:')
    print_square(n)
    print('Triangle Pattern:')
    triangleprint(n)
    print('Triangle Numbers:')
    triangle_numbers(n)
    print('Triangle Numbers 2:')
    triangle_numers2(n)
    print('Reverse Triangle:')
    reverse_triangle_print(n)
    print('Reverse pyramid:')
    reverse_pyramid(n)
    print('Reverse Triangle Numbers:')
    reverse_triangle_numbers(n)
    print('Pyramid:')
    pyramid(n)
    print('Diamond:')
    diamond(n)
    print('Left Triangle:')
    left_triangle(n)