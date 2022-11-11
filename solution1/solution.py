x = int(input())
y = input()
z = int(input())
a = input()

if(z>a)
print("no")

a = a.split(" ")
y = y.split(" ")
s = []
for i in range(1000,-1):
    s.append(i*"X"+"S")
s.append("M")
for i in range(0,1001):
    s.append(i*"X"+"L")
pos = 1
for i in a:
    gt = True
    for j in y:
        if(s.index(i)>s.index(j)):
            pass
        else:
            gt = False
    if(gt == True):
        pos = -1

if(pos == -1):
    print("no")
else:
    print("yes")

