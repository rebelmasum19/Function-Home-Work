

# Ex-02
# Function to find the largest of two numbers
def largest(num1,num2):

    if num1>num2:
        print(f"\nThe largest number is : {num1}")
    else:
        print(f"\nThe largest number is : {num2}")
num1=int(input("Enter 1st number : "))
num2=int(input("Enter 2nd number : "))
    
largest(num1,num2)




# Ex-04
# Function to find the factorial of a number
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    print(f"\nThe factorial of {num} is : {fact}")
num=int(input("Enter a number to find its factorial : "))
if num<0:
    print("\nFactorial does not exist for negative numbers.")
elif num==0:
    print("\nThe factorial of 0 is : 1")
else:
    factorial(num)




# Ex-05
# Program to check if a number is prime or not
def prime(num):
    is_prime=True
    if num>1:
        for i in range(2,num):
            if num%i==0:
                is_prime=False
                break
        if is_prime:
            print(f"\n{num} is a prime number.")
        else:
            print(f"\n{num} is not a prime number.")
n=int(input("Enter a number to check if it is prime or not : "))
prime(n)




# Ex-09
# Function to find the sum of odd numbers from 1 to n
def odd_sum(number):
    sum=0
    for i in range(1,number+1,2):
        sum+=i
    return sum
num=int(input("Enter a number to find the sum of odd numbers : "))
if num<0:
    print("\nPlease enter a positive number.")
else:
    result=odd_sum(num)
    print(f"\nThe sum of odd numbers from 1 to {num} is : {result}")




# Ex-10
# Function to print Fibonacci sequence up to n terms
def fibbo(n):
    a=0
    b=1
    if n<=0:
        print("\nPlease enter a positive integer.")
        
    elif n==1:
        print(f"\nThe Fibonacci sequence up to {n} term is : {a}")
    else:
        print(f"\nThe Fibonacci sequence up to {n} terms is : ")
        print(a,end=" ")
        print(b,end=" ")
        for i in range(2,n):
            c=a+b
            print(c,end=" ")
            a=b
            b=c
n=int(input("Enter the number of terms for Fibonacci sequence : "))
fibbo(n)




# Ex- 12
# Function to count the number of digits in a number
def digit_count(n):
    count = 0

    if n == 0:
        return 1

    while n > 0:
        n = n // 10
        count += 1

    return count


num = int(input("Enter a number: "))
result = digit_count(abs(num))

print("Total number of digits:", result)



# Ex- 13
# Function to check if a string is a palindrome or not
def palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False
text = input("Enter a string: ")
if palindrome(text):
    print(f'"{text}" is a palindrome.') 
else:
    print(f'"{text}" is not a palindrome.')
