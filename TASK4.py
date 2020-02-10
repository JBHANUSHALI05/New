'''4.1'''

def reverse(s): 
  str = "" 
  
  for i in s: 
    str = i + str
  return str

s = "1234abcd"

print ("The original string is : ",end="") 
print (s) 

print ("The reversed string(using loops) is : ",end="") 
print (reverse(s)) 


'''4.2'''

def up_low(s):      
    u = sum(1 for i in s if i.isupper())
    l = sum(1 for i in s if i.islower())
    print( "No. of Upper case characters : %s, No. of Lower case characters : %s" % (u,l))

up_low("My Name is Jigar Bhanushali and I am Getting Trained in Python")


'''4.3'''

def list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(list([45,85,98,78,5,8,85,8,5]))


'''4.4'''




'''4.5'''



'''4.6'''

def sum(a,b):
  x = int(a) + int(b)
  return x

num1 = 20
num2 = 30

a = sum(num1, num2)
print("a = ", a)


'''4.7'''



'''4.8'''

def printDict():
    dict = {i: i**2 for i in range(1, 21)}
    print(dict.keys())      # print keys of a dictionary

printDict()


'''4.9'''

limit = int(input("Give me a number. "))


for i in range(0,limit +1):

	if i % 2 == 0:

		print(str(i) + ":" +'EVEN')


	else:

		print(str(i) + ":"+ 'ODD')



'''4.10'''

def even(x):
    return x%2==0

evenNumbers = filter(even, range(1,21))
print(list(evenNumbers))


'''4.11'''

def even(x):
    return x%2==0

def squer(x):
    return x*x

li = [1,2,3,4,5,6,7,8,9,10]
li = map(squer,filter(even,li))
print(list(li))


'''4.12'''


def divide():
    return 5/0
try:
    divide()
except ZeroDivisionError as zero:
    print("you cannot divide a number by ZERO")
except:
    print("Any other exception")
	
'''4.14'''

def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)

# The above code prints '2' as we are using the function finally in the second block of code.


def a():
    try:
        f(x, 4)
    finally:
        print('after f')
    print('after f?')
a()

# The above code does not run and return an error as f is not defined.








