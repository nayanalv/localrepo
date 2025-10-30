n = 20
a, b = 0, 1
fib = []
for _ in range(n):
    fib.append(int(a))
    a, b = b, a+b
#print(fib)
three_digits =[]
for i in fib:
    if i>=100 and i<=999:
        three_digits.append(str(i))
print(' '.join(three_digits))
