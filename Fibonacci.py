# The Fibonacci series is a sequence of numbers where each number is the sum of the two preceding ones,
#  usually starting with 0 and 1
# The Fibonacci Sequence is the series of numbers:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# The next number is found by adding up the two numbers before it:
# the 2 is found by adding the two numbers before it (1+1),
# the 3 is found by adding the two numbers before it (1+2),
# the 5 is (2+3),
# and so on!  or Fn = Fn-1 + Fn-2


#%$$$ ....1)iterative method...........$$$

# n = 10
# a, b = 0, 1
# fibonacci_numbers = []
 
# for _ in range(n):
#     fibonacci_numbers.append(str(a))
#     a, b = b, a + b
 
# print(' '.join(fibonacci_numbers))


###%%%% 2) Using while loop ####

# n = 10
# a, b = 0, 1
# i = 0
# fib_n = []
 
# while i < n:
#     fib_n.append(str(a))
#     a, b = b, a + b
#     i += 1
 
# print(' '.join(fib_n))


#..........................3)If you want to generate the first n Fibonacci numbers .......................%%%%

def fib(n):
    a, b = 0, 1
    fib_n = []

    for _ in range(n):
        fib_n.append(str(a))
        a,b = b, a + b
        #b = a + b   
    return ' '.join(fib_n)
n= int(input("enter the range of numbers: "))
print(fib(n))


