#!/usr/bin/env python
# coding: utf-8

# 1. Define a function named `is_two`. It should accept one input and return `True` if the passed input is either the number or the string 2, `False` otherwise.

# In[11]:


def is_two(x):
    if x == (2 or '2'):
        return(True)
    else:
        return(False)


# In[13]:


is_two(2)


# 2. Define a function named `is_vowel`. It should return `True` if the passed string is a vowel, `False` otherwise.

# In[24]:


def is_vowel(l):
    vowels=['a', 'e', 'i', 'o', 'u']
    if l.lower() in vowels:
        return(True)
    else:
        return(False)
    
#any way to make it convert letters to strings?


# In[21]:


is_vowel('b')


# 3. Define a function named `is_consonant`. It should return `True` if the passed string is a consonant, `False` otherwise. Use your `is_vowel` function to accomplish this.
# 

# In[25]:


def is_consonant(l):
    vowels=['a', 'e', 'i', 'o', 'u']
    if l.lower() not in vowels:
        return(True)
    else:
        return(False)


# In[27]:


is_consonant('e')


# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

# In[31]:


def capitolize_word(word):
    if is_consonant(word[0]):
        return(word.title())
    else:
        return(word)


# In[32]:


capitolize_word('anana')


# 5. Define a function named `calculate_tip`. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
# 

# In[33]:


def calculate_tip(percent, total):
    return (percent * total)
    


# In[35]:


calculate_tip(.25, 20)


# 6. Define a function named `apply_discount`. It should accept a original price, and a discount percentage, and return the price after the discount is applied.
# 

# In[39]:


def apply_discount(original_price, discout_percent):
    return(original_price * (1 - discout_percent))


# In[40]:


apply_discount(100, .15)


# 7. Define a function named `handle_commas`. It should accept a string that is a number that contains commas in it as input, and return a number as output.

# In[45]:


def handle_commas(str):
    return(float(str.replace(",","")))


# In[46]:


handle_commas('1,000,000,000')


# 8. Define a function named <code>get_letter_grade</code>. It should accept a number and return the letter grade associated with that number (A-F).</li>
# 

# In[47]:


def get_letter_grade(num_grade):
    if num_grade >=90:
        return('A')
    elif num_grade >=80:
        return('B')
    elif num_grade >=70:
        return('C')
    elif num_grade >=60:
        return('D')
    else:
        return('F')


# In[50]:


get_letter_grade(75)


# 9. Define a function named <code>remove_vowels</code> that accepts a string and returns a string with all the vowels removed.

# In[59]:


def remove_vowels(str):
    new_str = []
    vowels=['a', 'e', 'i', 'o', 'u']
    for letter in str:
        if letter not in vowels:
            new_str.append(letter)
    return("".join(new_str))    


# In[60]:


remove_vowels('abracadabra')


# 10. Define a function named <code>normalize_name</code>. It should accept a string and return a valid python identifier, that is:<ul>
# <li>anything that is not a valid python identifier should be removed</li>
# <li>leading and trailing whitespace should be removed</li>
# <li>everything should be lowercase</li>
# <li>spaces should be replaced with underscores</li>
# <li>for example:<ul>
# <li><code>Name</code> will become <code>name</code></li>
# <li><code>First Name</code> will become <code>first_name</code></li>
# <li><code>% Completed</code> will become <code>completed</code></li>

# In[ ]:





# In[ ]:





# 12. Write a function named <code>cumulative_sum</code> that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.<ul>
# <li><code>cumulative_sum([1, 1, 1])</code> returns <code>[1, 2, 3]</code></li>
# <li><code>cumulative_sum([1, 2, 3, 4])</code> returns <code>[1, 3, 6, 10]</code></li>

# In[65]:


def cumulative_sum(*args):
    result=0
    for num in args:
        result = result + num
    return result


# In[68]:


cumulative_sum(10, 20, 30, 40, 50)


# <h3 id="additional-exercise">Additional Exercise</h3>
# <ul>
# <li>Once you've completed the above exercises, follow the directions from https://gist.github.com/zgulde/ec8ed80ad8216905cda83d5645c60886 in order to thouroughly comment your code to explain your code.</li>
# </ul>
# 

# In[ ]:





# In[ ]:





# <h3 id="bonus">Bonus</h3>
# <ol>
# <li>Create a function named <code>twelveto24</code>. It should accept a string in the format <code>10:45am</code> or <code>4:30pm</code> and return a string that is the representation of the time in a 24-hour format. <strong>Bonus</strong> write a function that does the opposite.</li>
# <li>Create a function named <code>col_index</code>. It should accept a spreadsheet column name, and return the index number of the column.<ul>
# <li><code>col_index('A')</code> returns <code>1</code></li>
# <li><code>col_index('B')</code> returns <code>2</code></li>
# <li><code>col_index('AA')</code> returns <code>27</code></li>
# </ul>
# </li>
# </ol>

# In[ ]:





# In[ ]:




