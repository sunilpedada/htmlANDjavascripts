import matplotlib.pyplot as pt
x=[1,2,3,4]
y=[10,20,303,40]
# pt.plot(x,y)
# pt.show()
# labels=["january","february","march","april"]
# pt.xticks(x,labels)
#pt.plot(x,y)
pt.xlabel("no of shares")
pt.ylabel("prices")
pt.bar(x,y)
pt.show()