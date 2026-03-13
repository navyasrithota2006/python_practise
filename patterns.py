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


def right_triangle_oand_1(n):
    start =1
    for i in range(n):
        if i%2==0: start = 1
        else: start =0
        for j in range(i+1):
            print(start,end=' ')
            start = 1-start
        print()

def w_building(n):
    for i in range(1,n+1):
        for j in range(i):
            print(j+1,end=' ')
        for j in range((2*(n-i))):
            print(' ',end=' ')
        for j in range(i,0,-1):
            print(j,end=' ')
        print()

def right_angle_triangle_continuous_numbers(n):
    num = 1
    for i in range(1,n+1):
        for j in range(i):
            print(num, end=' ')
            num += 1
        print()

def right_angle_triangle_alphabet(n):
    for i in range(1,n+1):
        for j in range(i):
            print(chr(64+j+1),end=' ')
        print()

def inverted_right_angle_alphabet(n):
    for i in range(1,n+1):
        for j in range(n-i+1):
            print(chr(64+j+1),end = " ")
        print()

def right_angle_continuous_alphabet(n):
    for i in range(1,n+1):
        for j in range(i):
            print(chr(64+i),end=' ')
        print()

def pyramid_of_aplhabet(n):
    for i in range(n):
        for j in range(n-i-1):
            print(' ',end=' ')
        bp = (2 * i +1)//2
        ch = ord('A')
        for j in range(2*i+1):
            print(chr(ch),end = ' ')
            if j<bp: ch += 1
            else: ch -= 1
        for j in range(n-i-1):
            print(' ',end=' ')
        print()

def reverse_alphabet_triangle(n):
    for i in range(n):
        for ch in range(ord('A')+n-1-i,ord('A')+n):
            print(chr(ch),end=' ')
        print()

def empty_diamond_shape(n):
    for i in range(1,n+1):
        for j in range(n-i+1):
            print('*',end=' ')
        for j in range((2*i)-2):
            print(' ',end=' ')
        for j in range(n-i+1):
            print('*',end=' ')
        print()
    for i in range(n-1,0,-1):
        for j in range(n-i+1):
            print('*',end=' ')
        for j in range((2*i)-2):
            print(' ',end=' ')
        for j in range(n-i+1):
            print('*',end=' ')
        print()

def anonymous(n):
    spaces = 2*n - 2
    for i in range(1,2*n - 1):
        stars = i
        if i>n: stars = 2*n -i
        for j in range(1,stars+1):
            print('*',end=' ')
        for j in range(1,spaces+1):
            print(' ',end=' ')
        for j in range(1,stars+1):
            print('*',end=' ')
        print()
        if i<n: spaces -= 2
        else: spaces += 2


def square(n):
    for i in range(n):
        for j in range(n):
            if i==0 or i==n-1 or j==0 or j==n-1:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

def squaresofnumbers(n):
    for i in range(2*n - 1):
        for j in range(2*n -1):
            top = i
            left =j
            right = (2*n - 2) - j
            bottom = (2*n -2) - i
            print((n - min(min(top,bottom),min(left,right))),end=' ')
        print() 

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
    print('Right Triangle of 0 and 1:')
    right_triangle_oand_1(n)
    print('W Building:')
    w_building(n)
    print('Right Angle Triangle of Continuous Numbers:')
    right_angle_triangle_continuous_numbers(n)
    print('Right Angle Triangle of Alphabet:')
    right_angle_triangle_alphabet(n)
    print('Inverted Right Angle Triangle of Alphabet:')
    inverted_right_angle_alphabet(n)
    print('Right Angle Triangle of Continuous Alphabet:')
    right_angle_continuous_alphabet(n)
    print('Pyramid of Alphabet:')
    pyramid_of_aplhabet(n)
    print('Reverse Alphabet Triangle:')
    reverse_alphabet_triangle(n)
    print('Empty Diamond Shape:')
    empty_diamond_shape(n)
    print('Anonymous Pattern:')
    anonymous(n)
    print('Square:')
    square(n)
    print('Squares of Numbers:')
    squaresofnumbers(n)