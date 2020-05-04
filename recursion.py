def factorial(n):
    if n==1:
        print(n)
        return 1
    else:
        return n*factorial(n-1)
a=factorial(5)
print(a)
i=2
v=1
e=5
while i<=e:
    v=v*i
    i+=1
print(v)