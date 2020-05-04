iter_object=[1,2,3,4]
def add(n):
    return n+n
result=map(add,iter_object)
print(list(result))
str_list=["sunil","ravi","ajay"]
str_result=map(list,str_list)
print(list(str_result))
for q in str_list:
    print(list(q))
