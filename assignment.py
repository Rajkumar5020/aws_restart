#1) LARGEST:

a = int(input('Enter first number  : '))
b = int(input('Enter second number : '))
c = int(input('Enter third number  : '))



if a > b and a > c :
    largest = a
elif b > c :
    largest = b
else :
    largest = c

print(largest, "is the largest of three numbers.")


#2) odd and even 

x = int(input("Enter a Number:")) 
if x % 2 == 0: 
  print("Given number is Even") 
else: 
  print("Given number is Odd")

#3) Swapping

# Python program to demonstrate
# swapping of two variables
 
x = 10
y = 50
 
# Swapping of two variables
# Using third variable

temp = x
x = y
y = temp
 
print("Value of x:", x)
print("Value of y:", y)

#4) Prime

# Program to check if a number is prime or not
# Input from the user
num = int(input("Enter a number: "))

# If number is greater than 1
if num > 1:
   # Check if factor exist  
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           break
   else:
       print(num,"is a prime number")
       
# Else if the input number is less than or equal to 1
else:
   print(num,"is not a prime number")


#5) Factorial

def factorial(n):
     
    # single line to find factorial
    return 1 if (n==1 or n==0) else n * factorial(n - 1);
 

num = 5;
print("Factorial of",num,"is",
factorial(num))


#6) print string

string_name = "rajkumar"
 
# Iterate over the string
for element in string_name:
    print(element, end=' ')
print("\n")
 
 
string_name = "rajkumar"
 
# Iterate over index
for element in range(0, len(string_name)):
    print(string_name[element])


    
    this_string = "Hey I am rajkumar"

for character_index in this_string:
   print(character_index) # print each character at a time from string



#7) ierate

# Python3 code to iterate over a list
list = [1, 3, 5, 7, 9]
  
# Using for loop
for i in list:
    print(i)


#8) Multiplication

number = int(input ("Enter the number of which the user wants to print the multiplication table: "))      
# We are using "for loop" to iterate the multiplication 10 times       
print ("The Multiplication Table of: ", number)    
for count in range(1, 11):      
   print (number, 'x', count, '=', number * count)    


#9) while

n=input("Enter Number");
n=int(n)
i = 1
while (i <= n):
   print (i)
   i = i+ 1


#10) fibnoacii

n = int(input("Enter the value of 'n': "))
a = 0
b = 1
sum = 0
count = 1
print("Fibonacci Series: ", end = " ")
while(count <= n):
  print(sum, end = " ")
  count += 1
  a = b
  b = sum
  sum = a + b