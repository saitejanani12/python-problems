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
"""
====================================PYTHON ASSIGNMENTS=======================
0.FINDING INDEX VALUES OF LIST WITHOUT ENUMERATE FUNCTIO
------------------------------------------------------------
a = [1,10,12,13,10,19,10]
sum = 0
for x in a: 
    sum+=1
    print(sum-1) #finding index values without enumerate function()
==================================================================
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
=======================================================================
2.FIND THE SUM OF STR() NUMBER...
------------------------------------
Num = '12345'
sum = 0
for x in Num:
    sum = sum+int(x)
print(sum)
==============================
3.FIND THE PRIME NUMBER OR NOT (BY USING FOR AND WHILE LOOP)
----------------------------------
number = int(input("ENTER NUMBER :"))
for x in range(2,number):
    if(number%x==0):
        print("NOT PRIME")
        break
else:
    print('PRIME')
-----------------------
2.METHDO :---------------
========================================
n=int(input("ENTER NUMBER "))
value = "prime"
for x in range(2,n):
    if(n%x==0):
        value = "not prime"
if(value=="prime"):
    print(value)
else:
    print(value)
----------------------------------------------
number = int(input('ENTER NUMBER :'))
i=2
print('------------------------------')
while(i<number-1):
    if(number%i==0):
        print(f"{number} IS NOT A PRIME NUMBER ")
        break
    else:
        print(f"{number} IS A PRIME NUMBER ")
        break
=========================================================
4.FIND THE GIVER DATA PALINDROME OR NOT
---------------------------------------------------
value = input("ENTER NUMBER OR STRING :")
if(value==value[::-1]):
    print("IT IS PALINDROME")
else:
    print("NOT PALINDROME")
========================================
5.ADD THE USER ENTER DATA TO THE LIST BY USING FOR LOOP AND WHILE LOOP
--------------------------------------------------------------
n=input("ENTER HOW MANY NUMBER YOU WANT TO STORE IN THE LIST :")
a = []
if(len(n)<=0):
    print("USER ENTERED INVALID INPUT")
else:
    for x in range(1, int(n)+1):
        name = input(f"ENTER {x} NAME :")
        a.append(name)
print(a)
---------------------------------------------------------------------------
n=input("ENTER HOW MANY NUMBER YOU WANT TO STORE IN THE LIST :")
a = []
i=1
while(i<=int(n)):
    name = input(f"ENTER {i} NAME :")
    a.append(name)
    i+=1
print(a)
==================================================================
6.FIND THE GIVEN NUMBER FACTORIAL(EX:5!=>1*2*3*4*5)(BY USING FOR AND WHILE LOOP)
-------------------------------------------------------------
number = int(input("WHICH NUMBER FACTORIAL YOU WANT :"))
sum = 1 #temporary variable should be 1 for find the factoria or whenever we doing multiplication we should be maintain 1
for x in range(1,number+1):
    sum=sum*x
    print(x)
print("--------------")
print(f"SUM OF {number}! factorial = {sum}")
-----------------------------------------------------------
number = int(input("WHICH NUMBER FACTORIAL YOU WANT :"))
sum = 1 #temporary variable should be 1 for find the factoria or whenever we doing multiplication we should be maintain 1
i=1
while(i<=number):
    sum=sum*i
    i+=1
    print(i)
print("-------------------------------")
print(f"SUM OF {number}! FACTORIAL = {sum}")
=========================================================================
7.FIND THE ZERO IN GIVEN NUMBER.(BY USING FOR AND WHILE LOOP)
-------------------------------------
num = input("ENTER NUMBER :")
for x in num:
    if x=="0":
        print(f"WE HAVE ZERO IN GIVEN VALUE {num}")
        break
else:
    print(f"WE DON'T HAVE ANY ZERO {num}")

------------------------------------------------
num = input("ENTER NUMBER :")
i = 0
while(i<len(num)):
   b=num[i]
   i = i + 1
   if (b=="0"):
       print("WE HAVE ZERO IN GIVEN NUMBER ")
       print(type(int(b)))
       break
else:
    print(type(int(b)))
    print("WE DON'T HAVE ZERO ")
---------------------------------------------------
8.PRINT VOWELS AND CONSONANTS WORDS 
------------------------------------------
n = int(input("ENTER HOW MANY NAMES YOU WANT TO PRINT :"))
a = []
b = []
if(n<=0):
    print("ENTER VAILD INPUT")
else:
    for i in range(1,n+1):
        w=input("enter {} name :".format(i))
        if('a' in w or 'e' in w or 'i' in w or 'o' in w or 'u' in w):
            k=a.append(w)
        else:
            v=b.append(w)
print("THSE ARE VOWEL WORDS {}".format(a))
print("THSE ARE NON-VOWEL WORDS {}".format(b))
-------------------------------------------------
9.PRINT PRIME NUMBER :
----------------------------------
i  = 2
while(i<=10):
    val = 'prime'
    j=2
    while(j<i):
        if(i%j==0):
            val = 'not prime'
            break
        j+=1
    if(val=='prime'):
        print(i)
    i+=1
--------------------------------
n = int(input("ENTER NUMBER :"))
for x in range(2,n):
    val = 'prime'
    for i in range(2,x):
        if(x%i==0):
            val = 'not prime'
    if(val=="prime"):
        print(x)
--------------------------------------
****FIND THE HEIGHT LENGTH OF STRING IN A LIST :
---------------------------------------------------
a = ['saiteja','harsha','santhosh']
d={}
for x in a:
    d[x]=len(x)
print(max(d.keys()),":",max(d.values()))
----------------------------------------------------
FINDING THE FACTORIAL OF NUMBER BY USING FUNCTIONS:-
----------------------------------------------------
def numbers():
    a = list()
    for x in range(1,6):
        a.append(x)
    return a
def factorial():
    sum = 1
    for i in numbers():
        sum=sum*i
    return sum
res=factorial()
print(res)
--------------------------------------
#FIND WEEKDAY NAME WITH USER INTER THE DATE 
-----------------------------------------------
a = list()
for x in range(1,32):
    a.append(x)
user = int(input("ENTER NUMBER AND FIND THE WEEK NAME :"))
if user in a[0::7]:
    print("SUNDAY")
elif user in a[1::7]:
    print("MONDAY")
elif user in a[2::7]:
    print("TUESDAY")
elif user in a[3::7]:
    print("WEDNESSDAY")
elif user in a[4::7]:
    print("THURSEDAY")
elif user in a[5::7]:
    print("FRIDAY")
else:
    print("SATURDAY")
======================================================================
# SPLIT THE STRING SAITEJA@1234 (OUT PUT= a="saiteja",b = '1234',c = "@" 
=======================================================================
a = 'saiteja@1234 -='
alpha = ''
digits = ''
special_symbols = ''
for x in a:
    if x.isalpha(): # if x is pure alphabet word
        alpha+=x
    elif x.isdigit():  #if x is pure digits word
        digits+=x
    else:
        special_symbols+=x
print(alpha)
print(digits)
print(special_symbols)
============================================
method -2
==============================================
lst = ['saiteja','saite123','1234','harsha']
alpha = list(filter(lambda x:x.isalpha(),lst))
print(alpha)
====================================================
# GENARATE THE FAKE DATA AND FAKE PHONE NUMBER :
======================================================
from faker import Faker
from random import *
f= Faker()
def phoneNumber():
    num = randint(6,9)
    number = ''+str(num)
    for x in range(9):
        number =number+str(randint(1,9))
    return number
def fakedata():
    n = int(input('HOW MANY FAKE DATA YOU WANT :'))
    print('========================')
    for x in range(n):
        name = f.name()
        age = f.random_element([20, 21, 22])
        email = f.email()
        phone = phoneNumber()
        print("NAME:", name)
        print("AGE:", age)
        print("EMAIL:", email)
        print("PHONE_NUMBER:", phone)
        print('========================')
fakedata()
print('========================')
=========================================================
# separate the int data type values and str data type values in a list
---------------------------------------------------------------------------
lst = ['sai',12,'teja',14]
numbers_list = list()
string_list=[]

for x in lst:
    if type(x)==int:
        numbers_list.append(x)
    else:
        string_list.append(x)
print(numbers_list)
print(string_list)
================================================
#check the perfect number or not
a = int(input("ENTER A NUMBER :"))
lst = list()
for x in range(1,a):
    if a%x==0:
        print(x)
        lst.append(x)
if a==sum(lst):
    print("THE GIVEN NUMBER IS PERFECT",sum(lst))
else:
    print("THE GIVEN NUMBER IS NOT PERFECT ")
=================================================================
#CREATE THE NUMBER OF PHONE NUMBERS BY USING RANDOM MODLE
------------------------------------------------------------
from random import *
def number_genarator():
    d = randint(6, 9)
    number = '' + str(d)
    for x in range(1, 9):
        number = number + str(randint(1, 9))
    return number
def numbers():
    n = int(input("ENTER HOW MANY NUMBERS YOU WANT :"))
    for x in range(n):
        value = number_genarator()
        print(value)
numbers()
================================================================
CREATING LIST INSIDE THE LIST:-
================================================================
lst2 = list()
while(True):
    lst = [x for x in input().split()]
    lst2.append(lst)
    ch = input("Enter '@' for stop :")
    if ch == '@':
        break
print(lst2)
------------------
METHOD-2
-------------
lst = list()
#[[1,2,3,4],[5,6,7,8,9]]
i = 1
while(i<=2):
    obj = [x for x in input().split()]
    lst.append(list(obj))
    i+=1
print(lst)
=============================
===================================
FINDING THE FACTORIAL OF GIVEN NUMBER BY USING RECURSION:-
----------------------------------------------------------------
def sum(n):
    if n == 0:
        ans = 1
    else:
        ans = n*sum(n-1)
    return ans
n = int(input("Enter Number :"))
ans = sum(n)
print(ans)
-----------------------------------------
SUM OF NUMBERS BY USING RECURSION
------------------------------------
def sum(n):
    if n == 0:
        ans = 0
    else:
        ans = n+sum(n-1)
    return ans
f1 = sum(10)
print(f1)
===========================

"""
old_list = [int(x) for x in range(1,21) if x%2==0]
new_list = list(map(lambda x:x*2,old_list))
print(new_list)
# By using Normal Function
old_list = [int(x) for x in range(1,21) if x%2==0]
def mapping(value):
    return value*2
new_list = list(map(mapping,old_list))
print(new_list)
#****************Problems On Filter **********************

old_list = [int(x) for x in range(1,21)]
#Filtering by using Normal Function
def filtering(value):
    if value%2==0:
        return True

new_list = list(filter(filtering,old_list))
print(new_list)

#By Using Lambda Function 
old_list = [int(x) for x in range(1,21)]
new_list = set(filter(lambda x:x%2,old_list))
print(new_list)


#Reduce Function 
from functools import reduce
old_list = [int(x) for x in range(1,12)]
def values(x,y):
    return x+y
new = reduce(values,old_list)
print(new)

#By Using Lambda Function
old_list = [int(x) for x in range(1,12)]
new = reduce(lambda x,y:x+y,old_list)

print(new)

#Exception Handling 
class LengthError(BaseException):pass

def Password():
    password = input("Enter Your passsword :")
    if len(password)!=8:
        raise LengthError 
    else:
        return password
    
try:
    value = Password()
except LengthError:
    print("Password Length Must Be 8 charectors Above ")
else:
    print(value)