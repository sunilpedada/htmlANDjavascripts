import functools
def sum_of_n(a,b):
   o=a+b
   return o
result=functools.reduce(sum_of_n,range(0,10))
print(result)
sum=0
for q in range(11):
    sum=sum+q
print(sum)