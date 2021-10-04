#!/usr/bin/env python
# coding: utf-8

# ## 1. Conditional Basics
# 
# - a. prompt the user for a day of the week, print out whether the day is Monday or not

# In[ ]:


user_day = input('Enter day of the week: ')

if user_day.lower() == ('monday' or 'm' or 'mon'):
    print('Today is Monday')
else:
    print('Today is not Monday')


# - b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend

# In[ ]:


user_day = input('Enter day of the week: ')
weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
            
if user_day.lower() in weekdays:
    print('Today is a weekday')
else:
    print('Today is a weekend') # Or the user entered gibberish or misspelled a weekday...


# - c. create variables and make up values for
# 
#     - the number of hours worked in one week
#     
#     - the hourly rate
#     
#     - how much the week's paycheck will be

# In[ ]:


hours_worked = 50
hourly_rate = 50

paycheck = hours_worked * hourly_rate
print(paycheck)


# - d. write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

# In[ ]:


if hours_worked > 40:
    paycheck = (hourly_rate * 40) + (1.5 * hourly_rate) * (hours_worked - 40)
else:
    paycheck = hours_worked * hourly_rate
print(paycheck)


# ---

# # 2. Loop Basics
# 
# ### - a. While
# 
# - Create an integer variable i with a value of 5.
# - Create a while loop that runs so long as i is less than or equal to 15
# - Each loop iteration, output the current value of i, then increment i by one.
#     Your output should look like this:
# 
# 
#     5
#     6
#     7
#     8
#     9
#     10
#     11
#     12
#     13
#     14
#     15

# In[ ]:


i = 5

while i <= 15:
    print(i)
    i +=1 


# - Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.

# In[ ]:


i = 0

while i <=100:
    print(i)
    i +=2


# - Alter your loop to count backwards by 5's from 100 to -10.
# 

# In[ ]:


i = 100

while i >=-10:
    print(i)
    i -= 5


# - Create a `while` loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:
# 
#      2<br/>
#      4<br/>
#      16<br/>
#      256<br/>
#      65536<br/>

# In[ ]:


i = 2

while i < 1000000:
    print(i)
    i **= 2


# - Write a loop that uses `print` to create the output shown below.
# 
# 
# 100<br/>
# 95<br/>
# 90<br/>
# 85<br/>
# 80<br/>
# 75<br/>
# 70<br/>
# 65<br/>
# 60<br/>
# 55<br/>
# 50<br/>
# 45<br/>
# 40<br/>
# 35<br/>
# 30<br/>
# 25<br/>
# 20<br/>
# 15<br/>
# 10<br/>
# 5

# In[ ]:


i = 100

while i >=5:
    print(i)
    i -= 5


# ## - b. For Loops

# - i. Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
# 
#     - For example, if the user enters 7, your program should output:
# 
# 
#     7 x 1 = 7
#     7 x 2 = 14
#     7 x 3 = 21
#     7 x 4 = 28
#     7 x 5 = 35
#     7 x 6 = 42
#     7 x 7 = 49
#     7 x 8 = 56
#     7 x 9 = 63
#     7 x 10 = 70

# In[ ]:


user_number = input('Enter a number: ')
i = 1

while i <= 10:
    print(user_number, 'x', i,  '=', int(user_number) * i)
    i += 1


# - ii. Create a `for` loop that uses `print` to create the output shown below.
# 
# 
# 1<br/>
# 22<br/>
# 333<br/>
# 4444<br/>
# 55555<br/>
# 666666<br/>
# 7777777<br/>
# 88888888<br/>
# 999999999<br/>

# In[ ]:


for num in range(1,10):
    if num == 1:
        print(num)
    else:
        print(str(num)*(num))


# ## -c. `break` and `continue`
# 
# - Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.
# 
# - Your output should look like this:
# 
# 
#     Number to skip is: 27
# 
#     Here is an odd number: 1
#     Here is an odd number: 3
#     Here is an odd number: 5
#     Here is an odd number: 7
#     Here is an odd number: 9
#     Here is an odd number: 11
#     Here is an odd number: 13
#     Here is an odd number: 15
#     Here is an odd number: 17
#     Here is an odd number: 19
#     Here is an odd number: 21
#     Here is an odd number: 23
#     Here is an odd number: 25
#     Yikes! Skipping number: 27
#     Here is an odd number: 29
#     Here is an odd number: 31
#     Here is an odd number: 33
#     Here is an odd number: 35
#     Here is an odd number: 37
#     Here is an odd number: 39
#     Here is an odd number: 41
#     Here is an odd number: 43
#     Here is an odd number: 45
#     Here is an odd number: 47
#     Here is an odd number: 49

# In[ ]:





# -d. The input function can be used to prompt for input and use that input in your python code.<br/>
#     - Prompt the user to enter a positive number and 
#     - write a loop that counts from 0 to that number. 
#     - (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)

# In[ ]:


user_number = input('Enter a positive number:')
i = 0
n = int(user_number)

if n > 0:
    while i <= n:
        print(i)
        i +=1

# Placement of break must be wrong -- never prompts me to enter number


# - e. Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.

# In[ ]:


user_number = input('Enter a positive integer: ')
n = int(user_number)

while n > 1:
    print(n)
    n -= 1


# ## 3.  Fizzbuzz
# 
# One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

# - Write a program that prints the numbers from 1 to 100.

# In[ ]:


for num in range(1,101):
    print(num)


# - For multiples of three print "Fizz" instead of the number

# In[ ]:


for num in range(1,101):
    if num % 3 == 0:
        print('Fizz')
    else:
        print(num)


# - For the multiples of five print "Buzz".

# In[ ]:


for num in range(1,101):
    if num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)


# - For numbers which are multiples of both three and five print "FizzBuzz".

# In[ ]:


for num in range(1,101):
    if (num % 3 == 0 and num % 5 ==0):
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)


# ## 4. Display a table of powers.
# - Prompt the user to enter an integer
# - Display a table of squares and cubes from 1 to the value entered.
# - Ask if the user wants to continue.
# - Assume that the user will enter valid data.
# - Only continue if the user agrees to.
# 

# In[4]:


user_num = input('What number would you like to go up to?')
n = int(user_num)
con = str(input('Would you like to continue? (y or n):'))
i = 1

if con.lower() == 'y':
    print('Here is your table:')
    print('Number    | Squared    |Cubed ')
    print('----------|------------|-------')
    while i <= n:
        print(i, '         ', i ** 2, '          ', i ** 3)
        i +=1


# **Bonus:** Research python's format string specifiers to align the table

# In[ ]:





# ## 5. Convert given number grades to letter grades
# - Prompt the user for a numerical grade from 0 to 100.
# - Display the corresponding letter grade.
# - Prompt the user to continue.
# - Assume that the user will enter valid integers for the grades.
# - The application should only continue if the user agrees to.
# - Grade Ranges:
#     - A : 100 - 88
#     - B : 87 - 80
#     - C : 79 - 67
#     - D : 66 - 60
#     - F : 59 - 0
# 

# In[2]:


#num_grade = input('Enter a numerical grade from 0 to 100: ')
#ng = int(num_grade)

con = 'y'
while con == 'y':
    num_grade = input('Enter a numerical grade from 0 to 100: ')
    ng = int(num_grade)
    if ng in range(88,101):
        print('A')
    elif ng in range(87,81):
        print('B')
    elif ng in range(67, 80):
        print('C')
    elif ng in range(60,67):
        print('D')
    else:
        print('F')
    con = input('Would you like to continue (y or n)?:"')


# ## 6. 
# - Create a list of dictionaries where each dictionary represents a book that you have read.
# - Each dictionary in the list should have the keys 
#     - title
#     - author
#     - genre.
# - Loop through the list and print out information about each book.

# In[2]:


my_books = [
    {
        'title': 'Beautiful Evidence',
        'author': 'Tufte',
        'genre': 'Visualization'
    },
    {
        'title': 'Visual Explanations',
        'author': 'Tufte',
        'genre': 'Visualization'
    },
    {
        'title': 'Envisioning Information',
        'author': 'Tufte',
        'genre': 'Visualization'
    },
    {
        'title': 'The Visual Display of Quantitative Information',
        'author': 'Tufte',
        'genre': 'Visualization'
    },
    {
        'title': 'Naked Statistics',
        'author': 'Wheelan',
        'genre': 'Background'
    },
    {
        'title': 'Weapons of Math Destruction',
        'author': "O'Neill",
        'genre': 'Applications'
    },
    {
        'title': 'Data Science from Scratch',
        'author': 'Grus',
        'genre': 'How-to'
    },
    {
        'title': 'Python for Data Science for Dummies',
        'author': 'Mueller',
        'genre': 'How-to'
    },
    {
        'title': 'Mac OS for Dummies',
        'author': 'Levitus',
        'genre': 'How-to'
    },
    {
        'title': 'How Charts Lie',
        'author': 'Cairo',
        'genre': 'Background'
    },
]


i = 0
for book in my_books:
    while i < len(my_books):
        print(my_books[i])
        i += 1
    


# ## b. Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.

# In[4]:


print('Here are the current genres: ')
i = 0
current_genres = []
for book in my_books:
    while i < len(my_books):
        current_genres.append(my_books[i]['genre'])
        i += 1
print(set(current_genres))

user_genre = input('Enter an exact genre name to search for titles:')

i = 0
user_titles = []
for book in my_books:
    while i < len(my_books):
        if my_books[i]['genre'] == user_genre:
            user_titles.append(my_books[i]['title'])
        i +=1
print('Here is a list of', user_genre, 'books:')
print(user_titles)


# In[ ]:




