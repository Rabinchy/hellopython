
#Condition

if True:
    print("this is true")
else:
    print("this is false")

if(1==2):
    print(("this is 1==1"))
else:
    print("this is false condition")


n=5
if(n%2==0):
    print("this is even",n)
else:
    print("This is odd",n)


n=7
if(n%2==0):
    print(f'number{n}is even')
else:
    print(f'number{n} is odd')

day = "SUnday"
day = day.lower()
if(day=="sunday"):
    print("Sunny day")
    print(day)


day = "SUnday"
temp = 30
day = day.lower()
if(day=="sunday" or temp==30):
    print("Sunny day")
    print(day)
    print(temp)


day = "tuesday"
day = day.lower()
if(day=="sunday"):
    print("Sunny day")
elif(day=="monday"):
    print("Working Day")
elif(day=="tuesday"):
    print("Happy day")
else:
    print("Boaring Day")



a=input("Ënter a word:")
print("entered word is", a)

a=input("enter a number")
b=input("enter a second number")
print(int(a)+int(b))


day = input("Enter a Day")
day = day.lower()
if(day=="sunday"):
    print("Sunny day")
elif(day=="monday"):
    print("Working Day")
elif(day=="tuesday"):
    print("Happy day")
else:
    print("Boaring Day")

#nested if
#singleline if condition


a= 50
if(a==50):
    print("number is 50")
    if(a%2==0):
        print("Number is even")
    else:
        print("Number is odd")
else:
    print("Number is not 50")


n= int(input("Enter any Number"))
if(n%2==0):
    print(f'number{n}is even')
else:
    print(f'number{n} is odd')

