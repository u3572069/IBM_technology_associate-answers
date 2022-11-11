def isValid(record):
    k = record.split()
    if(k[1] == "false"):
        return False
    else:
        return True

x = int(input())
l = []
for x in range(0,x):
    l.append(input())
allValid = True
errorCodes = []
for record in l:
    if(allValid == True):
        if (isValid(record) == False):
            allValid = False
    if isValid(record) == False:
        errorCodes.append(record.split()[-1])

if allValid == True:
    print("Yes")
else:
    print("No")
    print(*errorCodes)
