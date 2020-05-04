import time
import matplotlib.pyplot as pt
validating=0
seconds=[]
while(len(seconds)<5):
    print(len(seconds))
    start=time.time()
    a=input("type")
    end=time.time()
    time_lape=end-start
    seconds.append(round(time_lape))
    if a!="words":
        validating+=1
print("no of mistake",validating)
print(len(seconds))
x=[1,2,3,4,5]
labels=['1','2','3','4','5']
pt.xticks(x,labels)
pt.plot(x,seconds)
pt.show()