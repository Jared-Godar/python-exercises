#!/usr/bin/env python
# coding: utf-8

# # 17 list comprehension problems in python
# - Define initial lists
# 

# In[3]:


fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']


# In[4]:


numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]


# ---

# ## Example for loop solution to add 1 to each number in the list
# 

# In[5]:


numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)


# In[6]:


numbers_plus_one


# ## Example of using a list comprehension to create a list of the numbers plus one.

# In[7]:


numbers_plus_one2 = [number + 1 for number in numbers]


# In[8]:


numbers_plus_one2


# ## Example code that creates a list of all of the list of strings in fruits and uppercases every string

# In[10]:


output = []
for fruit in fruits:
    output.append(fruit.upper())


# In[12]:


output


# ### Exercise 1 
# - Rewrite the above example code using list comprehension syntax. 
# - Make a variable named `uppercased_fruits` to hold the output of the list comprehension. 
# - Output should be ['MANGO', 'KIWI', etc...]

# In[13]:


uppercased_fruits = []
for fruit in fruits:
    uppercased_fruits.append(fruit.upper())


# In[14]:


uppercased_fruits


# ## Exercise 2 
# - Create a variable named `capitalized_fruits` and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]

# In[15]:


capitalized_fruits = []
for fruit in fruits:
    capitalized_fruits.append(fruit.title())


# In[16]:


print(capitalized_fruits)


# ## Exercise 3 
# - Use a list comprehension to make a variable named `fruits_with_more_than_two_vowels` 
# - Hint: You'll need a way to check if something is a vowel.

# In[17]:


str(fruits[0])


# In[23]:


'mango'.count('a') + 'mango'.count('e') + 'mango'.count('i') + 'mango'.count('o') + 'mango'.count('u')


# In[30]:


fruits[1].count('a') + fruits[1].count('e') + fruits[1].count('i') + fruits[1].count('o') + fruits[1].count('u')


# In[32]:


fruits[3].count('a') + fruits[3].count('e') + fruits[3].count('i') + fruits[3].count('o') + fruits[3].count('u')


# In[35]:


len(fruits)


# In[57]:


#Count the vowels in each fruit

for fruit in fruits:
    i = 0
    vowels = []
    while i < len(fruits):
        vowels.append (fruits[i].count('a') + fruits[i].count('e') + fruits[i].count('i') +         fruits[i].count('o')+ fruits[i].count('u'))
        i += 1    


# In[58]:


print(vowels)


# In[53]:


fruits_with_more_than_two_vowels = []
i = 0
while i < len(fruits):
    if (fruits[i].count('a') + fruits[i].count('e') + fruits[i].count('i') +     fruits[i].count('o')+ fruits[i].count('u')) >2:
        fruits_with_more_than_two_vowels.append(fruits[i])            
    i += 1    


# In[55]:


print(fruits_with_more_than_two_vowels)


# ## Exercise 4 
# - make a variable named fruits_with_only_two_vowels
# - The result should be ['mango', 'kiwi', 'strawberry']

# In[60]:


fruits_with_only_two_vowels = []
i = 0
while i < len(fruits):
    if (fruits[i].count('a') + fruits[i].count('e') + fruits[i].count('i') +     fruits[i].count('o')+ fruits[i].count('u')) == 2:
        fruits_with_only_two_vowels.append(fruits[i])            
    i += 1  


# In[61]:


print(fruits_with_only_two_vowels)


# # Exercise 5 
# - Make a list that contains each fruit with more than 5 characters

# In[64]:


longfruits = []
i = 0
while i < len(fruits):
    if len(fruits[i]) > 5:
        longfruits.append(fruits[i])            
    i += 1  


# In[65]:


print(longfruits)


# # Exercise 6 
# - Make a list that contains each fruit with exactly 5 characters

# In[66]:


five_fruit = []
i = 0
while i < len(fruits):
    if len(fruits[i]) == 5:
        five_fruit.append(fruits[i])            
    i += 1  


# In[67]:


print(five_fruit)


# # Exercise 7 
# - Make a list that contains fruits that have less than 5 characters

# In[68]:


less_five = []
i = 0
while i < len(fruits):
    if len(fruits[i]) < 5:
        less_five.append(fruits[i])            
    i += 1  


# In[69]:


print(less_five)


# # Exercise 8 
# - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]

# In[71]:


for fruit in fruits:
    i = 0
    length = []
    while i < len(fruits):
        length.append (len(fruits[i]))
        i += 1    


# In[72]:


print(length)


# # Exercise 9 
# - Make a variable named `fruits_with_letter_a` that contains a list of only the fruits that contain the letter "a"

# In[74]:


fruits_with_letter_a = []
i = 0
while i < len(fruits):
    if (fruits[i].count('a')) > 0:
        fruits_with_letter_a.append(fruits[i])            
    i += 1    


# In[75]:


print(fruits_with_letter_a)


# # Exercise 10
# - Make a variable named even_numbers that holds only the even numbers

# In[77]:


even_numbers = []
i = 0
while i < len(numbers):
    if (numbers[i] % 2) == 0:
        even_numbers.append(numbers[i])            
    i += 1    


# In[78]:


print(even_numbers)


# # Exercise 11 
# - Make a variable named `odd_numbers` that holds only the odd numbers

# In[79]:


odd_numbers = []
i = 0
while i < len(numbers):
    if (numbers[i] % 2) != 0:
        odd_numbers.append(numbers[i])            
    i += 1    


# In[80]:


print(odd_numbers)


# # Exercise 12 
# - Make a variable named positive_numbers that holds only the positive numbers

# In[81]:


positive_numbers  = []
i = 0
while i < len(numbers):
    if numbers[i] > 0:
        positive_numbers.append(numbers[i])            
    i += 1    


# In[82]:


print(positive_numbers)


# ## Exercise 13 
# - Make a variable named `negative_numbers` that holds only the negative numbers

# In[83]:


negative_numbers  = []
i = 0
while i < len(numbers):
    if numbers[i] < 0:
        negative_numbers.append(numbers[i])            
    i += 1    


# In[84]:


print(negative_numbers)


# ## Exercise 14 
# - Use a `list comprehension` w/ a conditional in order to produce a list of numbers with 2 or more numerals
# 
# - Unsure how to call index in length comprenension can do this with an i count, but need syntax for list comprehension

# In[112]:


more_two = []
for number in numbers:
    i = 0
    if len (str(numbers[i])) > 2:
        more_two.append(number+1)
        i += 1


# In[103]:


print(more_two)


# In[122]:


more_two = []
for number in numbers:
    if len(str(number) > 2:
        more_two.append(number)


# ## Exercise 14 WRONG - fix syntax

# In[105]:


more_two = []
i = 0
while i < len(numbers):
    if len (str(numbers[i])) > 2:
        more_two.append(numbers[i])
    i += 1    


# In[106]:


more_two


# ## Exercise 15 
# - Make a variable named `numbers_squared` that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]

# In[113]:


numbers_squared = [number ** 2 for number in numbers]


# In[114]:


print(numbers_squared)


# ## Exercise 16 
# - Make a variable named `odd_negative_numbers` that contains only the numbers that are both odd and negative.

# In[123]:


odd_negative_numbers  = []
i = 0
while i < len(numbers):
    if (numbers[i] < 0) and ((numbers[i] % 2) != 0):
        odd_negative_numbers.append(numbers[i])            
    i += 1    


# In[124]:


print(odd_negative_numbers)


# ## Exercise 17 
# - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 

# In[125]:


numbers_plus_5 = [number + 5 for number in numbers]


# In[126]:


print(numbers_plus_5)


# # BONUS 
# - Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.

# In[127]:


pip install sympy


# In[129]:


sympy.isprime(2)


# In[ ]:




