#!/usr/bin/python
# This python script serves as an example to reference
# while learning/re-learning python. There will be different
# Sections added and they will be labeled accordingly.
from builtins import zip

#---------------------------#
# Object and Data Structure #
#---------------------------#
my_string = 'String'
my_second_string = 'String 2'
my_third_string = "There's an single quote in here!"
my_fourth_string = '"Python is cool"'
my_math_variable = 5*10
my_list = [1,2,3,4,5]
my_second_list = [6,7,8]
my_dictionary = {'key1':'value1','key2':'value2'}
my_dictionary_fmt = {'apple':2.25,
                     'bread':5.99,
                     'milk':4.80}
my_flex_dictionary = {'key':'value',           # Key value pair
                      'keylist':[1,2,3],       # Key contains list as value. Can pull from list like: my_flex_dictionary['keylist'][2]
                      'kik':{'insidekey':100}, # Key inside of key (call using my_flex_dictionary['kik']['insidekey']
                      'ree':['one', 'two', 'three']}                                                 # ^ returns 100
my_tuple = (1,2,3)


# Strings, indexing, and slicing
#-------------------------------#
# Print string variable...
print(my_fourth_string)

# Print tri from the word string...
print('string'[1:4])

# Print ring from the word string...
print('string'[2::])


# Concatenation - merging
#-------------------------------#
# Concatenate lists...
print(my_list + my_second_list)


# Using methods
#-------------------------------#
# Print uppercase variable with method...
print(my_third_string.upper())

# Methods, append 9...
my_second_list.append(9)
print(my_second_list)

# Methods, remove 9...
my_second_list.pop()
print(my_second_list)

# Using the sort method to sort lists...
my_third_list = ['a','e','x','b','c']
print(my_third_list)
my_third_list.sort() # Actually sorts variable assigning new sorted var.
print(my_third_list)

my_num_list = [4,1,8,3]
print(my_num_list)
my_num_list.sort() # Actually sorts variable assigning new sorted var.
print(my_num_list)

# Reverse method...
my_third_list.reverse() # Actually reverses variable assigning new reversed var.


# Math and numbers
#-------------------------------#
# Print number variable (integer)...
print(my_math_variable)

# Do math with variable and set new variable (float)...
my_math_variable_2 = my_math_variable / 11
print(my_math_variable_2)

# Use float formatting... "{value:width:precision f}"
print("The formatted result is {r:4.2f}".format(r=my_math_variable_2))


# Print formatting
#-------------------------------#
# Print formatting examples...
print('Python formatting {}'.format('rules!'))
name = "Sam"
age = 3
print(f'{name} is {age} years old.')


# Dictionaries
#-------------------------------#
# Print entire dictionary...
print(my_dictionary)

# Print key1 value...
print(my_dictionary['key1'])
print(my_dictionary_fmt['milk'])

# Print specific from list and format with method...
print(my_flex_dictionary['ree'][2].upper())

# Add new key value pair to dictionary...
my_flex_dictionary['newkey'] = 300
print(my_flex_dictionary)

# List all keys in dictionary...
print(my_dictionary_fmt.keys())

# List all values...
print(my_dictionary_fmt.values())


# Tuples (Immutable)
#-------------------------------#
# Tuples are like lists, but immutable and have less methods...
t2 = ('one', 2, 'one')
print(t2)

# Count instances of 'one' in t2...
print(t2.count('one'))

# Show index of where 'one' appears in tuple the first time...
print(t2.index('one'))


# Sets (unordered collections of unique elements)
#-------------------------------------------------#
my_set = set()

# Add values to my_set...
my_set.add(1)
print(my_set)

# Convert messy list to set and rid of the duplicate values...
shitlist = [1,1,1,1,1,1,1,2,2,2,2,3,3,3,3,3]
print(shitlist)
set(shitlist) # results in {1, 2, 3}


# Booleans (T or F)
#-------------------------------#
# Must have capitalized True or False
print(1 > 2)  # returns False
print(1 == 1) # returns True


# I/O with Basic Files
#-------------------------------#
# To open file called file.txt OLDER WAY OF DOING THIS...
my_file = open('./scratch/file.txt')

# Read contents of file.txt
my_file.read()

# To re-read, you must seek the cursor back to 0
my_file.seek(0)
my_file.read()

# Output with cleaner lines, allows for looping through list...
my_file.seek(0)
my_file.readlines()

# Close file after using...
my_file.close()

# Better way to open file... This will close the file when you are done using it. Call contents to see content of file.
with open('./scratch/file.txt') as my_new_file:
    contents = my_new_file.read()

# Permissions:
# r = read
# w = write
# a = append
# r+ = read and write
# w+ = write and read (overwrites existing file or creates new)

# Open with read-only mode...
with open('./scratch/file.txt',mode='r') as my_new_file:
    contents = my_new_file.read()

# Open with write-only mode...
with open('./scratch/0sdf3we9edf.txt',mode='w') as my_new_file:
    contents = my_new_file.write('Created by Python')

# Append new lines to end of file...
with open('./scratch/file.txt',mode='a') as my_new_file:
    my_new_file.write('\nNewly appended line')



# Comparison Operators
#-------------------------------#
# Equals...
2 == 2 # True
2 == 1 # Not true
'hello' == 'goodbye' # False
'2' == 2 # False

# Not Equals...
3 != 3 # False
4 != 5 # True

# Greater than...
2 > 1 # True
2 < 2 # False
2 >= 2 # True


# Logical operators
#-------------------------------#
# Multiple comparisons with logical operators... and, or, not
# True, lets use logical operators though
1 < 2 < 3
1 < 2 and 2 < 3
'h' == 'h' and 2 == 2

# For organization, we can use (). Not REQUIRED though...
('h' == 'h') and (2 == 2)

# Or...
1 == 1 or 1 == 100 # True

# Not...
not(1 == 1) # False
not 1 == 1  # False
not 400 > 5000 # True


# Python if statements
#-------------------------------#
# if some_condition:
#     execute some code
# elif: some_other_condition:
#     do something different
# else:
#     do something else
hungry = True

if hungry:
    print('Feed me!')
else:
    print("Don't feed me!")

# Another example...
loc = 'Bank'

if loc == 'Auto Shop':
    print('Fix my car!')
elif loc == 'Bank':
    print('Money is nice!')
elif loc == 'Store':
    print('Welcome to the store.')
else:
    print('This isnt the car shop?')



# Python for statements
#-------------------------------#
# my_iterable_list = [1,2,3]
# for item in my_iterable_list:
#     print(item)

my_list = [1,2,3,4,5,6,7,8,9,10]

for num in my_list:
    print(num)

# Use list to do something different...
for num in my_list:
    print('Hello')

# Check for even or odd... If divided by 2 == 0...
for num in my_list:
    if num % 2 == 0:
        print(f'Even number:  {num}')
    else:
        print(f'Odd number: {num}')


# For every number in initial my_list variable, do list_sum + number and assign sum to list_sum...
list_sum = 0

for num in my_list:
    list_sum = list_sum + num
    
    print(list_sum)

# If the print were to be outside the indentation, you would only get the final number. (55)
# If we do not want to use a variable to iterate through something, just use an _...
for _ in 'Hello World':
    print('Cool!')

# Tuple un-packing pairs...
my_tuple_list = [(1,2),(3,4),(5,6)]

for item in my_tuple_list:
    print(item)

# Or, alternatively...
for a,b in my_tuple_list:
    print(a) # If you want to only see value a in tuple pair, only print a
    print(b)

# Unpack items from a dictionary... 
dict = {'type':'Test','num':1,'class':'None'}

for item in dict:
    print(item) # Note how this only prints the keys, if we want the values as well, we must do the following

for item in dict.items(): # Can also use .values()
    print(item)

# Again, we can use unpacking by copying the format...
for key,value in dict.items(): # Can also use .values()
    print(value)



# Python while loops
#-------------------------------#
# Simple example...
x = 0

while x < 5:
    print(f'The value of x is {x}')
    x += 1 # Add x by 1
else:
    print('The value of x is greater than 5.')

# Using break, continue, pass...
# break    = Breaks out of the current closest enclosing loop.
# continue = Goes to the top of the closest enclosing loop.
# pass     = Does nothing at all.

# Break example:
w = 'Sammy'

for letter in w:
    if letter == 'a': # If the letter is a, break out of the loop
        break
    print(letter)
#--
r = 0

while r < 5:
    if r == 2:
        break # Once r is equal to 2, break. 
    print(r)
    r += 1

# Continue example:
for letter in w:
    if letter == 'a': # If the letter is a, go back to the top of the loop and continue, dont print a.
        continue
    print(letter)

# Pass example: (Instead of erroring, just pass and let me continue.
q = [1,3,5]

for item in q:
    # Nothing happens here...
    pass

print('This comment outside of the for loop still works.')



# Useful Operators
#-------------------------------#
# Range for iteration...
#################################
# Prints 0 - 10
for num in range(10):
    print(num)

# Prints 3 - 9
for num in range(3,10):
    print(num)

# Prints 0 - 10 in a step size of 2...
for num in range(0,10,2):
    print(num)

# Using range to generate a list... 0-10 in step size of 2
print(list(range(0,11,2)))

# Enumeration
###################################
# Without enumerating...
index_count = 0

for letter in 'abcde':
    print('At index the letter is {}'.format(index_count,letter))
    index_count +=1

# With enumerating...
word = 'abcde'

for item in enumerate(word):
    print(item)

# This provides us with tuples... (0, 'a') and so on...
for index,letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')

# Zip
###################################
# Zip list together from 2 seperate list, giving us tuples (1, a) (2, b)...
list_1 = [1,2,3]
list_2 = ['a','b','c','d'] # If there is an extra value in a list, it will be left out. 
list_3 = [11,12,13]

for item in zip(list_1,list_2, list_3):
    print(item)

# To list the zip values...
print(list(zip(list_1,list_2)))


# In operator
###################################
# Check to see if x is in a list, dictionary, etc...
print('x' in [1,2,3]) # False

# Dictionary example...
t = {'mykey':345}

345 in t.values()



# Min, Max, & Random
###################################
minmax = [10,20,30,40,50,60,70,80]

# Print min of list...
print(min(minmax))

# Print max of list...
print(max(minmax))

# Using random to shuffle list...
from random import shuffle, randint

rando_list = [3,4,5,6,7,8,9]

print(rando_list)
shuffle(rando_list)

print(rando_list)

# Using random to grab random integer from range...
print(randint(0,100))

# Set variable as random number... Not sure why you would do this...
rando_var = randint(22,35)

print(rando_var)


# User Input
###################################
# Input always takes a string...
result = input('Enter a number here: ')

print(result)

# If we want to get a format other than string, we have to do the following...
print(float(result))
print(int(result))

# Or, to get around this, just wrap the var in the type when prompting for input
# result = int(input('Enter a number here: '))




