#0.FINDING INDEX VALUES OF LIST WITHOUT ENUMERATE FUNCTIO
#------------------------------------------------------------
a = [1,10,12,13,10,19,10]
sum = 0
for x in a: 
    sum+=1
    print(sum-1) #finding index values without enumerate function()
#1.FIND THE ARMSTRONG NUMBER OR NOT 
#--------------------------------------
x = input('ENTER VALUE :')
sum = 0
for i in x:
    b=int(i)**len(x)
    sum=sum+b
if(x==str(sum)):
    print(sum)
    print("THIS IS ARMSTRONG NUMBER ")
else:
    print(sum)
    print("THIS IS NOT A ARMSTRONG NUMBER ")