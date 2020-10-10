#!/usr/bin/env python
# coding: utf-8

# # Lambda Functions

# ### Lambda function in python
# - A lambda function is a small anonymous function.
# 
# - A lambda function can take any number of arguments, but can only have one expression.
# 
# #### Syntax
# 
# lambda arguments : expression
# 
# The expression is executed and the result is returned:
# 

# In[2]:


def addition(a,b):
    c = a + b
    return c
addition(2, 3)


# In[3]:


def add(a,b):
    return a+b
add(3,5)


# In[4]:


def addtn(a,b):return a+b
addtn(3,9)


# In[5]:


add_lambda = lambda a,b : return a+b
add_lambda(2,7)


# In[6]:


add_lam = lambda a,b: a+b
add_lam(2,3)


# In[9]:


sub_lam = lambda a,b: a-b
sub_lam(2,1)


# In[2]:


# Create a function to find even numbers.
def CheckEven(a):
    if a%2 == 0:
        return 'Even Numer'
    else:
        return 'Not Even Number'
CheckEven(4)


# In[3]:


# Create a lambda function to identify whether a number is even or not.
find_even = lambda x : x%2 == 0
find_even(4)


# In[12]:


# Create a function to find odd numbers.
def CheckOdd(a):
    if a%2 != 0:
        return 'Odd Numer'
    else:
        return 'Not Odd Number'
CheckEven(5)


# In[11]:


# Create a lambda function to identify whether a number is odd or not.
find_odd = lambda y: y%2 != 0
find_odd(5)


# Lambda functions can take any number of arguments:
# 
# ##### Why Use Lambda Functions?
# - The power of lambda is better shown when you use them as an anonymous function inside another function.
# - Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
# - An anonymous function is a function with out a name
# - While normal functions are defined using the def keyword in python ,anonymous functions are defined using lambda keyword.
# - We use lambda functions when we require a nameless function for a short period of time.
# - Lambda functions are used aong with built-in functions like filter(),map()
# 

# In[15]:


def myfunc(n):
    return lambda a : a * n


# - Use that function definition to make function that always doubles number you send it.

# In[17]:


def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))


# In[19]:


def myfunc(n):
    return lambda a : a * n
print(myfunc(2))


# In[20]:


def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
mydoubler(12)


# In[21]:


def myfunc(n):
    return lambda a : a * n
my_doubler = myfunc(2)
my_tripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))


# In[24]:


def myfunc(n):
    return lambda a : a * n
# Print(myfunction(5))
n = int(input("Enter n value: "))
mydoubler = myfunc(n)
print(mydoubler(11))


# In[25]:


# Create a list from 300 to 700 with a step of 3
List1 = list(range(300,700,3))
print(List1)


# In[26]:


List1 = list(range(300,700,3))
type(List1)


# # Without lambda function using for and if looping to identify even numbers.

# In[27]:


List2 =[]  # Create an empty list.
for i in List1:
    if i%2 == 0:
        List2.append(i)  # Appending the even numbers to the empty list.
print(List2)  


# In[29]:


List2 = []  # Create an empty list.
for i in List1:
    if find_even(i):
        List2.append(i)  # Appending the even numbers to the empty list.
print(List2)  


# In[32]:


find_even = lambda x : x%2 == 0
find_even(4)


# In[33]:


find_even = lambda x : x%2 == 0
find_even(13)


# In[34]:


add_lamb = lambda a,b : a+b
add_lamb(5,3)


# # Filter
# 

# Here filter is a function that can be used to filter the elements from the list of elements based on a criteria
# Syntax is filter(function_name,data) 
# Here function_name refers to the function using which you want to set up the criterea and filter the lements 
# And data is the object on which you want to apply the filter.
# 
# In our case, I want to filter the even numbers from List1 which contains the elements from 300 to 600 with step 3
# Now the function that I want to use here is find_even because I want to filter the even numbers from list1
# 

# In[36]:


List2 = []  # Create an empty list.
for i in List1:
    if find_even(i):
        List2.append(i)  # Appending the even numbers to the empty list.
print(List2) 


# In[39]:


List2 = list(filter(find_even,List1))
print(List2)


# In[41]:


even_find = lambda x : x%2 == 0
List3 = list(filter(even_find,List1))
print(List3)


# Create a lambda function to find the numbers that are divisible by 5 and also filter that numbers from List1 which are divisible by 5

# In[44]:


check_div_5 = lambda a : a%5 == 0
listDivisibleBy5 = list(filter(check_div_5,List1))
print(listDivisibleBy5)


# In[46]:


# User defined functions without lambda
def find_div_5(num):
    return num%5 == 0
find_div_5(30)


# In[48]:


find_div_5_lam = lambda num : num%5 ==0 


# In[69]:


List3 = list(filter(find_div_5,List1)) # Filtering using a non lambda function.
print(List3)


# In[70]:


List4 =list(filter(lambda num : num%5 != 0,List1)) # Filtering with a lambda function
print(List4)


# In[54]:


List4 = filter(lambda num : num%5 != 0,List1)
print(list(List4))


# In[ ]:





# # Subtract 300 from each and every element of List1.

# In[58]:


# Method 1 without map
List1 = list(range(300,700,3))
List5 = []
for i in List1:
    List5.append(i-300)
print(List5)


# # Map
# 
# **map(func,iterables)**
# 
# - Making an iterable computes the function using arguments with each iterables
# 
# ### In list1 subtract all values with 300
# 

# In[59]:


# Method2 to subtract all values
sub_lam = lambda x : x - 300


# In[60]:


List6 = map(sub_lam,List1)
print(list(List6))


# In[66]:


power = lambda x : x**2


# In[67]:


List7 = map(power,List1)


# In[68]:


print(list(List7))


# In[ ]:




