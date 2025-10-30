n = 10
a, b = 0, 1
fib = []
for _ in range(10):
    fib.append(int(a))
    a, b = b, a+b
#print(fib)
even=[]
for i in fib:
    if i % 2 == 0:
        even.append(str(i)) #to save even no as string in the list
print(' '.join(even))  #' '.join it will remove , and give space instead




