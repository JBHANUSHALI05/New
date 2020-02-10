'''Task 1'''


#1.1 

x,y,z = [10, 20.5, "jigar"]
print(z)

#####################################

#1.2

x=20
y=40

x = y
y = x

print(x)
print(y)


#############################################

#1.3




##############################################

#1.4

#python 3
x = eval(input("Enter two number between 1 - 10))
print(x)

#python 2.7
x = eval(raw_input("Enter two number between 1 - 10))
print(x)



###############################################

#1.5

x , y = eval(input("Enter two number between 1 - 10: "))

z = 30 + x + y

print(z)


################################################

#1.6

x = 25
type(x)
print('The input value data type is", type(x))

################################################

#1.7



################################################

#1.8

'' Yes. Since python automatically takes the updated value. 






''''TASK 2'''''


''2.1''

x = eval(input("Enter a Number divisible by 3 and 5: "))
if x % 3 == 0:
  print("c")
elif x % 5 == 0:
  print("Consultadd")
elif x % 3 and x % 5 == 0:
  print ("Consultadd Python Training")
  
  
  
  
'''2.2'''
  
# This function adds two numbers
def add(x, y):
   return x + y
# This function subtracts two numbers 
def subtract(x, y):
   return x - y
# This function multiplies two numbers
def multiply(x, y):
   return x * y
# This function divides two numbers
def divide(x, y):
   return x / y
# This function takes average of two numbers
def average(x, y):
  return x + y / 2

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.average")
# Take input from the user 
choice = input("Enter choice(1/2/3/4/5): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
elif choice == '5':
   print(num1,"+",num2,"/ 2", average(num1,num2))
elif choice
   print("")


'''2.3'''



'''2.4'''

x = int(input("enter a number: "))
for elements in x:
  if elements <=0:
    print("its over")
  elif elements >= 0:
      print("Good Going")



'''2.5'''

Numbers=[]
for x in range(2000, 3200):
    if (x%7==0) and (x%5!=0):
        Numbers.append(str(x))
print (','.join(Numbers))



'''2.6'''

x=123 
for i in x:
	print(i)
	
'''the above code gives an error because int object is not iterable. ''''

i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print("error")
	
''' The Above Code runs and print 0 1 2 and then stops since on the code it says if i ==3 the code should break''''



count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

'''' The Above code print 0 1 2 3 4 and then breaks as the code says the moment count goes above 5 it should break the code'''''


'''2.7'''


for x in range(6):
    if (x == 3 or x==6):
        continue
    print(x,end=' ')
print("\n")


'''2.8'''

string=input("Enter a string:")
count1=0
count2=0
for i in string:
      if(i.isdigit()):
            count1=count1+1
      count2=count2+1
print("The number of digits is:", count1)
print("The number of characters is:", count2)


'''2.9.1'''


 number = input("Guess the lucky number ")
while number != 5:
  print ("That is not the lucky number")
  number = input("Guess the lucky number ")
  

''''2.9.2''''

number = -1
again = "yes"
while number != 5 and again != "no":
  number = input("Guess the lucky number: ")
  if number != 5:
    print ("That is not the lucky number")
    again = input("Would you like to guess again? ")

'''2.10.1'''

x = 1
while x <= 5:
  number = input("Guess the " + str(x) + ". number ")
  if number != 5:
    print ("Try again.")
  else:
    print ("Good guess!")
    x = x + 1
else:
  print ("Game over")
  
  
''''3.1'''


a = [5, "jigar", 5.1]


''''3.4''''

a=[567,589,689,9854,78569]
max(a)
min(a)


'''3.7'''

num1 = [1, 3, 5, 7, 9, 10]
num2 = [2, 4, 6, 8]
num1[-1:] = num2
print(num1)


'''3.8'''

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3 = {}
for d in (dic1, dic2): dic3.update(d)
print(dic3)

'''3.9'''

n=int(input("Input a number "))
d = dict()
for x in range(1,n+1):
    d[x]=x*x
print(d) 

'''3.10'''


values = input("Input some comma seperated numbers : ")
list = values.split(",")
tuple = tuple(list)
print("List : ",list)
print("Tuple : ",tuple)





 

