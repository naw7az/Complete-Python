# Binary conversion ::::::::::::::::::::::::::::::::::::::::::::::::::::::

print(bin(5))  # the type is string
print(int("0b101", 2))


# To get value of numbers inside a string :::::::::::::::::::::::::::::::::::::::::::

a_string = "1/2"
print(eval(a_string))  # int won't work here, int works only for base 10(integer)


# augmented assignment operator ::::::::::::::::::::::::::::::::::::::

some_value = 5
some_value *= 3 # this is short for---> some_value = some_value*3
print(some_value)


# string ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

print(type("hi hello there"))
username = "Super coder"
password = "Super secret"
long_string = '''
wow
o o
---
'''
print(long_string)
first_name = "John"
last_name = "Felix"
full_name = first_name + ' ' + last_name
print(full_name) # or u can use space after assigning Felix as last name.


# string concatenation ::::::::::::::::::::::::::::::::::::::::::::

print('Hello' + ' Felix') # if u put 4 instead of 'Felix' , it won't work. It only work with same data type.

# type conversion ::::::::::::::::::::::::::::::::::::::::::::::::::::

print(str(100))
print(type(str(100)))  # integer converted to string
print(type(int(str(100))))  # integer converted to string and again back to integer


# Escape Sequence :::::::::::::::::::::::::::::::::::::::::::::::::

weather = "\t It\'s \" kind of\"sunny \n hope you have a good day"
print(weather)
\- everything after this will be considered a string
\t- for tab
\n- for new line


# formatted string ::::::::::::::::::::::::::::::::::::::::::::::::::::

name = 'Johnny'
age = 55
print(f'hi {name}. you are {age} years old') # python 3(better)
print('hi {}. you are {} years old'.format(name, age)) # python 2


# String Indexes ::::::::::::::::::::::::::::::::::::::::::::::::::::

who = '01234567'
print(who[0:8:2])  # [start(inc):stop(exc):pattern]
print(who[-1])     # -ve for backward
print(who[::-1])     # Reverse the string


# Immutability :::::::::::::::::::::::::::::::::::::::::::::::::::

selfish = 'my name is'
# this particular code will not work -> selfish[0] = "k"
selfish = "keep"
print(selfish)


# Built-in Methods for string ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

quote = "to be or not to be"
x = "     hello   ".strip()  # used to remove spaces from start and end.{added later}
print(quote.upper())
print(quote.find('be'))
print(quote.capitalize())
print(quote.replace('be', 'me'))  # this is a new string all-together and not assigning.
print(quote)   # remember strings are immutable.
print(x)  # {added later}
print(quote.split(" "))  # splitting string into multiple items of a list, the argument should be in string


# Data Structure 1 - List(Array) ::::::::::::::::::::::::::::::::::::::::::

amazon_cart = ['notebooks', 'sunglasses', 'pixel 4']
print(amazon_cart[2])

# List Slicing - Copying vs Modifying : remove hash from either one only at a time.
# [:] <--this is the KEY DIFFERENCE.
amazon_cart = ['notebook',
               'sunglasses',
               'toys',
               'grapes']
amazon_cart[0] = 'laptop'
# MODIFIED
# new_cart = amazon_cart  # here amazon_cart is MODIFIED to new_cart.
# new_cart[0] = 'gum'     # that means amazon_cart is the new_cart.
# print(new_cart)         # Any change in new_cart will effect amazon_cart.
# print(amazon_cart)

# COPIED
new_cart = amazon_cart[:]  # here amazon_cart is COPIED to new_cart.
new_cart[0] = 'gum'        # that means new_cart is totally different from amazon_cart.
print(new_cart)            # hence change in new_cart will have no effect in amazon_cart.
print(amazon_cart)


# Matrix - multi-dimension list(Array) :::::::::::::::::::::::::::::::::::::::;

matrix = [
    [1, 2, 3],  # 3 sub-array and 1 main array
    [8, 6, 5],
    [9, 3, 7]
         ]  # matrix is list inside a list (here 2 dimensional)

print(matrix[0][2])


# List Methods 1 - open one at a time (can open all too) ::::::::::::::::::::::::::

basket = [1, 2, 3, 4, 5]

# append
# basket.append(70)  # append changes the list in place. It does not produce(return) a value which we can store.
# new_list = basket  # hence if we write new_list = basket.append(70), printing new_list will show 'none'.
# print(new_list)

# insert
# basket.insert(4, 45)  # same as append, insert changes the list in place.
# new_list = basket     # insert can take any index in the list unlike append.
# print(new_list)

# extend
# basket.extend([104, 89])  # extend also change the list in place.
# new_list = basket         # in extend we are giving a new list to add.
# print(new_list)

# pop
# basket.pop()    # pop() remove the very last item from the list.
# basket.pop(0)    # pop(item index) will remove the item from that index.
# print(basket)    # pop will return a value unlike the other method. Try "new_list = basket.pop(3)"

# remove
# basket.remove(5)  # in remove we have to put the item which we want to remove .
# print(basket)     # remove changes the list in place. same as append.

# clear
basket.clear()   # clear removes everything in the list.
print(basket)    # clear changes the list in place. same as append.


# List Methods 2 - open one at a time ( or all) :::::::::::::::::::::::::::::::::

basket = ['a', 'b', 'c', 'd', 'e', 'c']

# index
print(basket.index('d', 0, 4))  # give the index of the item :(item, start, stop) .
print('d' in basket)          # in is keyword here.
print('x' in basket)

# count
print(basket.count('c'))   # counts how many times the item occurs in list.


# List Methods 3 - open one at a time ::::::::::::::::::::::::::::::::::::::

basket = ['a', 'b', 'c', 'd', 'e', 'c']

# sorted
print(sorted(basket))   # here sorted is a function and it will create a new list.
print(basket)

# sort
# basket.sort()      # here sort is a method.It will modify the existing basket.
# print(basket)

# copy
# new_list = basket.copy()  # it just copy the list. :\
# print(new_list)

# reverse
# basket.reverse()
# print(basket)


# Common List Pattern ::::::::::::::::::::::::::::::::::::::::::::::::::::

basket = ['a', 'x', 'b', 'c', 'd', 'e', 'c']

basket.sort()
basket.reverse()
print(basket[::-1])    # reversed again due to -1.It creates a new list.
print(basket)
print(range(0, 101, 2))  # range(start, stop, pattern)
print(list(range(0, 101, 2)))

# join - It is actually a string method but can be used for lists.
sentence = " "
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'JOJO'])  # join add every item of the list with a string.
print(new_sentence)  # remember join method returns a value so we may  store it.
# a shortcut for line 13,14(if you copy whole code) is : new_sentence = ' '.join(['hi', 'my', 'name', 'is', 'JOJO'])


# list unpacking ::::::::::::::::::::::::::::::::::::::::::::::::::::::::

a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a)
print(b)
print(c)       # *other will take all the items which are not assigned.
print(other)   # remember use '*' only while assigning the rest of item.
print(d)       # d is assigned to last item as 'other' took everything between c and d.


# None :::::::::

weapons_start_game = None
print(weapons_start_game)


# Data Structure 2 - Dictionary :::::::::::::::::::::::::::::::::::::::::

dictionary = {
    'a': [1, 2, 3],   # key(a) and value[1, 2, 3], here the value of first key is a list.
    'b': 'Hello, me is dimitri',
    'x': True
 }
my_list = [   # here the 2 indexes are dictionaries.
 {
    'a': [1, 2, 3],   # key(a) and value[1, 2, 3]
    'b': 'Hello, me is dimitri',
    'x': True
 },
 {
    'a': [1, 2, 3],   # key(a) and value[1, 2, 3]
    'b': "When I want to rush B, I just say 123",
    'x': False
 }]

print(dictionary)
print(dictionary['b'])  # access the key to get the value.
print(my_list[1]['b'])
print(my_list[0]['a'][2])


# Dictionary Key ::::::::::::::::::::::::::::::::::::::::::::::::::::::::

dictionary = {
    123: [1, 2, 3, 4, 5],
    True: 'God',
    # 123: "Hello"
    # [100]: True
}

print(dictionary[123])  # A key needs to be immutable.And a list ([100] here) is mutable.
print(dictionary[True])  # hence we will get an error if we print it.
# print(dictionary[100])  # Mostly a key for a dictionary is a string.
print(dictionary[123])   # Every key should be unique for a value otherwise it will overwrite the previous value.


# Dictionary Methods 1 ::::::::::::::::::::::::::::::::::::::::::::::::::::::::

user = {
    "Basket": [1, 2, 3, 4, 5],
    "Greet": 'Hello',
    # "age": 20
}

"""
 get is a method used to get the value for a key, and if key doesn't exist then it will show none.
 so that we can avoid error(main reason). It can also add a value if key doesn't exist. But the
  k-v pair will not be added in the actual dictionary."""

print(user["Basket"])   # this can be used to get a particular value(or change it) for a key, also be used to add k-v pair.
print(user.get("age", 45))   # hash and un hash age to see difference.


# Another way of creating a dictionary(Not very common)
user2 = dict(name="John Wick")  # here name is a Property(later talk about it).
print(user2['name'])


# Dictionary Methods 2 - (Open 1 at a time) ::::::::::::::::::::::::::::::::::::::::

user = {
    "Basket": [1, 2, 3, 4, 5],
    "Greet": 'Hello',
    "age": 20
}
print('Greet' in user)
print('Hello' in user)  # this will only check keys not values.

# keys
# print('Greet' in user.keys())  # to check keys

# values
# print('Hello' in user.values())  # to check values
# print(user.items())   # returns a tuple for every key-values pair in the dictionary.

# to use list method in a dictionary - this is only applicable when the value of the key is a list.
# user['Basket'].append(47)
# print(user)

# copy and clear
# user2 = user.copy()
# user.clear()   # clear is a method which modifies(doesn't return a value to store) the dictionary.
# print(user)    # print(user.clear()) <--- this will give none.
# print(user2)

# pop
# print(user.pop("age"))  # remove the key-value pair and returns the value.
# print(user)             # key-value pair got removed.

# popitem              # popitem removes one of the key-value pair randomly.Remember dictionary is unordered.
# print(user.popitem())  # Since the dictionary is small it is removing the last pair.

# update
print(user)
user.update({"Basket": [3, 5]})  # update doesn't return a value.
user.update({"hot": True})
print(user)


#  Data Structure 3 - Tuple::::::::::::::::::::::::::::::::::::::::::::::::::::::::

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1])          # a tuple is immutable, so we cannot change any of it's value.
print(5 in my_tuple)

#  tuple makes our code safer because other user cannot modify it unlike a list.

user = {
    (1, 2): [1, 2, 3],
    "greet": "hello",
    "age": 20
}
print(user[(1, 2)])  # as we can see a tuple can be used as a key since it's immutable.


# Tuple Methods ::::::::::::::::::::::::::::::::::::::::::::::::::::::::

my_tuple = (5, 2, 3, 4, 5)
new_tuple = my_tuple[1:4]   # tuple slicing
print(new_tuple)
print(my_tuple.count(5))  # count the item
print(my_tuple.index(5))  # return the index of first occurrence of item.
print(len(my_tuple))

x, *z, a = (9, 87, 67, 33, 45,)  # same thing we do in list.
print(x)
print(z)  # remember *variable in tuple will return a list.
print(a)


# Data Structure 4 - Set :::::::::::::::::::::::::::::::::::::::::::::::

my_set = {1, 3, 6, 8, 9, 9}  # like dictionary but without keys
print(my_set)  # the 2nd 9 is not returned. item should be unique in a set.
my_set.add(100)   # a set is unordered, hence 100 is not placed at last.
my_set.add(6)    # 6 will not be added since it's already there.
print(my_set)
print(len(my_set))  # remember 100 was added and in set we do not count duplicates.
print(list(my_set))  # to convert into a list

my_list = [1, 2, 2, 4, 4, 7, 8, 6, 9, 0]
print(set(my_list))  # this can be used to remove duplicate from a list.


# Set Methods -(Open 1 at a time) ::::::::::::::::::::::::::::::::::::::::

my_set = {1, 2, 3, 4, 5}
you_set = {4, 5, 6, 7, 8, 9, 10}
sure_set = {98, 45}
new_set = {4, 5}

# difference
# print(my_set.difference(you_set))  # items only in my_set.
# print(you_set.difference(my_set))  # items only in you_set.

# discard
# my_set.discard(2)  # removes 2
# print(my_set)      # it doesn't return a value(modifies).

# difference_update
# my_set.difference_update(you_set)  # remove items from my_set which are present in you_set also.
# print(my_set)

# intersection
# print(my_set.intersection(you_set))  # common between 2 sets
# print(my_set & you_set)  # shortcut for intersection

# isdisjoint
# print(my_set.isdisjoint(you_set))  # here we are asking that whether these sets have nothing in common.
# print(my_set.isdisjoint(sure_set))

# union
# print(my_set.union(you_set))  # just like venn diagram.
# print(my_set | you_set)  # shortcut for union

# issubset
# print(new_set.issubset(you_set))  # whether subset or not.

# issuperset
print(my_set.issuperset(new_set))  # whether superset or not.


# Conditional Logic :::::::::::::::::::::::::::::::::::::::::::::::::

# Here we can control(or break) the flow of code by skipping lines(if false)
is_old = True
is_licenced = True

# simplified version
# if is_old:  # when condition given is true then only print.
#     print("you are old enough to drive! ")
# elif is_licenced:   # only runs when 'if' condition is false and given condition is true.
#     print("You are licensed to Drive! ")
# else:    # only runs when all the given conditions are false.
    # print("Not allowed to drive. ;) ")

# and keyword :
if is_old and is_licenced:
    print("YOU CAN DRIVE !!!")  # print only when both condition are true.
else:
    print("Not allowed to drive. ;) ")
print("Done")


# Truthy or Falsy :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

is_old = "Hello"  # here the if statement is printed that means both condition is true.
is_licenced = 5  # but we did not assign any boolean then why?

# These are called truthy values in python
print(bool("Hello"))  # Python only understand true or false in conditional logic.
print(bool(5))        # hence under the hood python do these two code.
# an empty string and 0 is considered falsy. Try it yourself.

if is_old and is_licenced:
    print("YOU CAN DRIVE !!!")
else:
    print("Not allowed to drive. ;) ")


# Ternary Operator(Conditional Expression) - A shortcut :::::::::::::::::::::::::::::::::::

# syntax--> (condition_if_true) if condition else (condition_if_false)
is_friend = True
can_text = "texting allowed" if is_friend else "not allowed to text."
print(can_text)  # Try it few times to get a hand on it.


# Short Circuiting - and & or ::::::::::::::::::::::::::::::::::::::::::::::

is_user = True  # make this false while doing 'and'.
is_friend = True

# or
if is_user or is_friend:  # here after checking is_user to be true python sees 'or'and did not even go to is_friend.
    print(" best friend")  # because anyway it has to print this (or means either).python short circuit 'is_friend'.

# and
# if is_user and is_friend:  # here after checking is_user to be false python sees 'and' ,did not even go to is_friend.
#     print(" best friend")  # because anyway it will not print (and means both).python short circuit 'is_friend'.


# Logical Operators :::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# 'and' & 'or' are already covered.Remember those two are also logical operators.
print('a' > 'b')  # check ZTM(notes) for reason.
print('a' > 'A')
print(1 < 2 < 3 < 4)
print(1 < 2 > 3 < 4)  # short circuit at 2>3 since it is false.
print(1 >= 0)
print(0 <= 0)
print(0 != 1)
print(0 != 0)
print(not True)
print(not 1 == 1)  # not does the opposite. 1==1 is true and not put false.


# is vs == ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# ==
# Ideally we(and we should) use logical operator on same data type.
# but here python is changing one type to another before comparing.
print(True == 1)  # T
print("" == 1)   # F
print([] == 1)   # F
print(10 == 10.0)   # T python changes int into float or vice versa .
print([] == [])   # T

# is - here none of the data are stored in same location except when they are exactly the same.
print(True is 1)  # F
print("" is 1)   # F
print([] is 1)   # F
print(10 is 10.0)   # F
print(1 is 1)   # T
print([] is [])  # The reason to get false in here is that these are two completely different lists.
print([1, 2, 3] is [1, 2, 3])  # This will happen with most of the data structures since both are stored differently.
print((1, 2, 3) is (1, 2, 3))  # This is true because tuple is immutable just like numbers and strings hence stored in same location.


# for loops- open 1 at a time :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

""" syntax: for variable in iterable:
              print(variable) """  # this can be used to write multi-line comment

# for item in "Zero to Mastery":
#     print(item)

# for item in (1, (1, 2), (1, 2, 3), (1, 2, 3, 4), (1, 2, 3, 4, 5)):
#     print(item)

# nested loops
for item in (1, 2, 3, 4, 5):  # the loop starts from here take first value(1 as item) then go to nested loop.
    for x in ['a', 'b', 'c']:  # here again it takes the first value(a as x) then get to print.
        print(item, x)  # after this the interpreter goes back to the nested loop complete it then goes to bigger loop.


# Iterable

user = {                   # You remember this is a dictionary ;)
    'name': "Goblin",
    'age': 67,
    'can_swim': False
}

for things in user:  # default for iterating keys
    print(things)

for things in user.items():  # iterate key-value pair in form of tuple
    print(things)

for things in user.keys():  # iterate keys only(better and descriptive)
    print(things)

for things in user.values():  # iterate value only
    print(things)

for k, v in user.items():  # here k is taking all keys while v takes all values.
    print(k, v)    # Always remember we define variable(s)[k,v here] while making loops.

# for looping in 5:  # 'int' objects are not iterable. you will get an error like this.
#     print(looping)  # because 5 is not a collection of anything.It's just 5.



# Exercise - Tricky Counter ::::::::::::::::::::::::::::::::::::::::::::::::

# Get the sum of all numbers in the list..?
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Solution :
counter = 0   # We need an extra variable here outside the loop to do sum, I did't think of this.
for num in my_list:
    counter = counter + num
print(counter)  # print is outside so that we get the total of all number and not after every loop.


# range() - useful in looping ::::::::::::::::::::::::::::::::::::::::::::::

for numbers in range(10):  # 0 is default for start.
    print(numbers)

for numbers in range(0, 10):
    print("email sent")

for numbers in range(0, 10, 2):
    print(numbers)

for numbers in range(10, 0, -1):  # to get the loop of range in reverse we have to put start and stop in reverse.
    print(numbers)  # and also we have to put the pattern(-1), then only it will print.

for _ in range(3):  # here the _ took 0 as first number of range then printed the list of range(10).
    print(list(range(10)))  # repeated it 3 times up to 2(0-1-2).


# enumerate() ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

for character in enumerate("Hello"):  # iterate the object along with it's index in tuple.
    print(character)

for index, value in enumerate("Super Mario"):  # to get spacing without tuple.
    print(index, value)

# Exercise: Find the index of number 50...?

for i, char in enumerate(list(range(100))):
    if char == 50:  # did't think of this if statement inside loop.
        print(f'index of 50 is {i}')


# while loops :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

i = 0
while i <= 50:  # DO NOT run this without break , this is an infinite loop.
    print(i)
    break  # With the break statement we can stop the loop even if the while condition is true.

# we can also  break(when condition gets false) like this:
while i <= 5:
    print(i)
    i += 1
    # break  # break will come out of 'else' statement as well. try removing # from break.
else:   # else condition will only execute if there isn't a break. After while condition turns to false.
    print("Done with looping")


# while loops 2 ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# for loops are simple and readable,but on the other hand while loops are flexible and powerful.
# hence for simple and short iterable objects use for loops.
# but if we are not sure how many times the loop is needed then use while loops.
my_list = [1, 2, 3]

for item in my_list:
    print(item)

i = 0
while i < len(my_list):
    print(my_list[i])  # here when i(index)=0 , value is 1.
    i += 1

# Useful way of using while loops
while True:
    response = input("Say something: ")
    if response.lower() == "stop":  # here looping can happen infinite times(true always) unless the user says "stop".
        break


# break, continue, pass - open 1 at a time ::::::::::::::::::::::::::::::::::::::::::::

my_list = [1, 2, 3]

# break - It just break out of the loop even if it is True.
for item in my_list:
    print(item)
    break

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    break

# continue - makes the interpreter to continue from the top of enclosing loop.
for item in my_list:
    continue     # the interpreter will see the print only after completing the loop, all because of 'continue'.
    print(item)

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1  # here continue will work properly(because it's at end), even without continue we will get the same result.
    continue  # but make sure to understand what happens to the loop based on the position of 'continue'.

# pass - it just pass to the next line, not useful.
for item in my_list:  # pass is good place holder, let's say we have to put something here but not coming to mind.
    pass   # without pass we will get an error here. try it.

i = 0
while i < len(my_list):
    pass
    print(my_list[i])
    i += 1


# Our first GUI :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Exercise!
# Display the image below to the bottom where the 0 is going to be ' ', and the 1 is going to be '*'.
# This will reveal an image!

picture = [
  [0, 0, 0, 1, 0, 0, 0],
  [0, 0, 1, 1, 1, 0, 0],
  [0, 1, 1, 1, 1, 1, 0],
  [1, 1, 1, 1, 1, 1, 1],
  [0, 0, 0, 1, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0]
]

# Solution:(This was actually tough)
# try to hash(or remove) end="" and print("") to understand properly.

for row in picture:  # this is for every lists in the bigger list.
    for pixel in row:  # I didn't think of this step. This is needed for every number on each list.
        if pixel == 1:
            print("*", end="")  # Ideally there is a new line between every two print.But we don't want that.
        else:  # the default in above line is print("*", end=/n) for new line but we don't want that.
            print(" ", end="")  # but now everything is in single line.We need a new line after every sub-list.
    print("")  # this will make sure that after every row we get an empty string and new line(default is new line).
# print x above instead of "" to understand.


# Exercise: Check for duplicate in list ::::::::::::::::::::::::::::::::::::::::::::::

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# Solution :
duplicates = []
for value in some_list:
    if some_list.count(value) > 1:  # I didn't think of this count method.
        if value not in duplicates:  # to make sure that if value already present in duplicate, it won't append.
            duplicates.append(value)
print(duplicates)


# Defining Functions::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

"""This is very useful when we have a piece of code which we want again.
Defining a function also makes our code DRY(since we don't need to copy whole code).
"""


def say_hello():  # here def is used to define(or create) a function.
    print("hello")  # this function is used to print "hello".


say_hello()
print(say_hello)  # To get the location of our defined function in memory.
print("")

# To have multiple Christmas Tree:
picture = [
  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
  [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
  [0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0],
  [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
]


def christmas_trees():
    for row in picture:
        for pixel in row:
            if pixel == 1:
                print("*", end="")
            else:
                print(" ", end="")
        print("")
    print("")


christmas_trees()
christmas_trees()


# arguments and parameters ::::::::::::::::::::::::::::::::::::::::::::::::::

"""Remember that if we use parameters, we have to use arguments for
 all those parameters which were used in defined function """

# parameters - (name, age, country)

def say_hello(name, age, country):  # parameters are variables used while defining a function.
    print(f"hello {name}, you are {age} years old living in {country}")
    print("")

# arguments - ("Adil", 21, "India")

say_hello("Adil", 21, "India")  # we assign the parameters with arguments while using the function.
say_hello("John", 37, "USA")


# default parameters and keyword arguments :::::::::::::::::::::::::::::::::::::::::::::::::::::::::

def say_hello(name="Darth Vader", age=43, country="Death Star"):
    print(f"hello {name}, you are {age} years old living in {country}")
    print("")

# positional arguments

"""The arguments used here are called POSITIONAL ARGUMENTS, since their position
 matters.(If we write 21 instead of Adil then the output doesn't make any sense.)"""

say_hello("Adil", 21, "India")

# keyword arguments

"""As we can see, here the position doesn't matter.But it is a bad practice
 because we are making the code complicated, We should follow the pattern of
 parameters when we initially defined the function. """

say_hello(country="India", name="Adil", age=21)

# default parameters

"""default parameters are already assigned with some default value while defining
the function.Hence if we miss some arguments, the default value will take its place."""

say_hello()
say_hello("Mr.Wick")


# return ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

"""A function always have to return something, If they don't return
something then the default is none(i.e. it modifies only.)
Also as soon as we return something, the function gets over."""

def summation(num1, num2):
    return num1 + num2  # remove return here to see getting none.

print(summation(4, 5))  # remember we have to use print when we only use return(in function) to get the result.
total = summation(10, 5)  # return is a good practice because we can store the result in some variable.
print(total*3)

# nested function - Not a good practice and little complicated

def add(numb1, numb2):
    def another_function(n1, n2):  # this function is actually adding two parameters(but we can't use this function).
        return n1 + n2
    return another_function(numb1, numb2)  # here we are assigning numb1=n1 and numb2=n2 for the bigger function.

_sum = add(25, 75)
print(_sum)


# docstring ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

def test(a):
    """Info: this function test and prints param a"""
    print(a)  # ABOVE IS A DOCSTRING , used to tell others what this function does.

test(45)  # the info above will be shown here while giving arg to "a".It works in repl but not in pycharm.

# USE 1 at a time
# help(test)  # help function will give the info written above and many other thing.
print(test.__doc__)  # .__doc__ is one of the dander method.


# clean code ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# A Normal Code

# def is_even(num):
#     if num % 2 == 0:
#         return True
#     elif num % 2 != 0:
#         return False

# print(is_even(47))

# 1st clean-up

# def is_even(num):
#     if num % 2 == 0:
#         return True
#     return False  # We don't have to write elif because when if condition is not true it will "return" false directly.

# print(is_even(47))

# Final clean-up

"""We actually don't even need if statement also, because we are returning
 an expression here(important to understand this), which the interpreter will
 check and tell us if true or not automatically.This will give the cleanest code."""

def is_even(num):
    return num % 2 == 0

print(is_even(47))


# *args and **kwargs ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

"""Imp: We can write anything after * and ** but the preferred
parameters are *args and **kwargs, so everyone can understand.
The order in which we can use: params > *args > default params > **kwargs"""

# *args
""" *args(which is a parameter) allows us to use multiple positional arguments for just 1 parameter.
as we can see the arguments are stored in the form of a tuple in *args"""

def func_1(*args):
    print(args)
    return sum(args)

print(func_1(1, 2, 3, 4, 5))

# **kwargs
""" **kwargs(which is a parameter) allows us to use multiple keyword arguments for just 1 parameter.
as we can see the arguments are stored in the form of a dictionary in **kwargs"""

def func_2(**kwargs):
    print(kwargs)

func_2(num1=2, num2=3)

# both together

def super_func(*args, **kwargs):
    total = 0
    for item in kwargs.values():
        total += item
    return sum(args) + total

print(super_func(1, 2, 3, 4, 5, num1=2, num2=3))


# Exercise: Function (Highest even) ::::::::::::::::::::::::::::::::::::::::::::

def highest_even(*args):
    evens = []  # didn't think of this and max(evens), I'll get better.
    for item in args:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)

print(highest_even(4, 24, 27, 28, 16, 12, 17, 29, 13))


---# scope ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

"""Scope simply means what variables do you have access to.There
 are two types of scope, global scope and functional scope.A functional
 scope can only be called inside the function but a global scope can be called anywhere."""

x = 50  # x has a global scope, it can be called from anywhere in the code.
def some_func():
    total = 100  # total has functional scope, can only be called inside this particular function.
    print(x)

# print(total)  # you will get an error, since total has functional scope.
some_func()


# scope rules :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

""" Rules: order in which we should check variable, when it is called
#1 - start with local function
#2 - then parent function
#3 - then global function(the parent of parent function is global scope)
#4 - built-in python functions.
"""
a = 1

def parent_func():
    a = 10  # hash this also to get #3 rule

    def local_func():
        # a = 5  # hash this to get #2 rule
        # return a
        return sum  # this is #4 rule, hash above two line to get this

    """here python sees 'sum' as variable then follow the rules to check for
    it's value if its not present then at the end it checks whether it is a
    built-in function(and yes it is) """

    return local_func()

print(parent_func())  # the order for this is written above
print(a)  # this will always call the global variable.


# global keyword and dependency injection :::::::::::::::::::::::::::::::::::::::::::::::::::

total = 0

# global keyword:

"""global keyword can get really complicated if the code is too long, and
remember the value of global variable will change."""

# def count_1():
#     global total  # global is used to get global variable for a function.
#     total += 1
#     return total

# count_1()  # after this the total is set to 1 not 0.
# count_1()
# print(count_1())
# print(total)  # the global total is changed(dependent)

# dependency injection :

"""by this method the global variable will always be set to it's initial
value."""

def count_2(total):
    total += 1
    return total

# this is not the part of dependency injection(just to show global keyword method won't work here.)
count_2(total)
count_2(total)
print(count_2(total))

# this is the part of dependency injection
print(count_2(count_2(count_2(total))))
print(total)  # here the global total is independent of function.


# nonlocal keyword :::::::::::::::::::::::::::::::::::::::::::::::::::::::::

"""This is used to change the value of variable present in parent function.
This will also makes our code complicated so use only when it is needed."""

def outer():
    x = "local"

    def inner():
        nonlocal x  # by using this, we can change the value of x in 'outer' function.
        x = "nonlocal"  # hash above line to see the difference(scope rule).
        print("inner:", x)

    inner()
    print("outer:", x)
outer()


---# Object Oriented Programming :::::::::::::::::::::::::::::::::::::::::::::::::::::::::

"""Creating our own objects(data types) with different attributes and methods
using the class keyword. OOP is a paradigm, a way to think and structure our code.
We can create real life things by making an object for that."""

class BigObject:  # Class(Blueprint)
    # some code
    pass

obj1 = BigObject()  # Instantiate(created an object)
obj2 = BigObject()  # Instantiate(created another object)

print(type(45))
print(type([]))
print(type(obj1))  # It is a type of BigObject(data type that we just created).


# Creating our own objects ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

"""While creating a class the first letter should be capital for each word
 with no spaces or underscore in between."""

"""1. The first parameter while defining any method is self.
   2. init(stands for initialize) is a dander method.
   3. self is reference for objects which hasn't been created yet.
   4. This "self.char_name(attribute)" means that for our future object this will tell it's name(param).
   5. Class Object Attribute(COA) are used when something is same for all the objects."""


class PlayerCharacter:
    membership = True  # 5(Class Object Attribute)

    def __init__(self, name, age):  # this is called Constructor Function, needed while defining a class.
        if PlayerCharacter.membership:  # or we can also do "self.membership" because It's a COA(point 5).
            self.char_name = name  # calling the attributes(.char_name) will print the arguments(Ghost).
            self.char_age = age

    def run(self):  # run is a method(not attribute).
        return f"run {self.char_name} "  # remember to use self while assigning attribute.
# here we cannot return {playerCharacter.char_name} because char_name is not a COA, it is defined inside the constructor.

player1 = PlayerCharacter("Ghost", 44)
player2 = PlayerCharacter("Scream", 27)

print(player1)  # tells memory location
print(player1.char_name)  # the placeholder for player1(object) was "self" while creating the class.
print(player1.char_age)
print(player1.membership)

print("")

print(player2.char_name)
print(player2.char_age)
print(player2.run())

player2.attack = 50
print(player2.attack)


---# @classmethod, @staticmethod and instance method :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

"""As we can see we don't need to instantiate to use a staticmethod(***or classmethod if it's not
 taking access over class specific data)unlike run which is(also a method) defined separately.
 A classmethod can have access to constructive function(using cls) but not static method.
 And remember we don't use either much often."""


class PlayerCharacter:
    membership = True  # normal class object(COA)
    def __init__(self, name, age=44):
        if PlayerCharacter.membership:
            self.char_name = name
            self.char_age = age

    def run(self):  # run is an instance method
        return f"run {self.char_name} "

    @staticmethod
    def adding_things1(numb1, numb2):  # this two line code will also work in classmethod,try(***read top statements).
        return numb1 + numb2  # but we use classmethod to gain access to class specific data hence use staticmethod.

    @classmethod
    def adding_things2(cls, num1, num2):  # cls stands for class(similar to self but for method and not attribute)
        return cls("Ted", num1 + num2)   # cls here give access to the constructive function.

"""ted becomes argument for name(param) which we used in constructive function."""

# for staticmethod
print(PlayerCharacter.adding_things1(4, 6))  # it's working without instantiate
# print(PlayerCharacter.run())  # this won't work, first we need an object.

# for class method
player_3 = PlayerCharacter.adding_things2(10, 3)  # instantiating the classmethod
print(player_3.char_name)
print(player_3.char_age)  # getting access to attribute in constructive function.


---# private and public variable (in Abstraction):::::::::::::::::::::::::::::::::::::::::::::::::::


class PlayerCharacter:
    membership = True  # COA

    def __init__(self, name, age):
        if PlayerCharacter.membership:
            self._char_name = name  # underscore at start to tell it's a private variable to other user.
            self._char_age = age    # It is just a convention, still anyone can gain access if they want.

    def run(self):
        return f"run {self._char_name} "

    def speak(self):
        return f"my name is {self._char_name}, and I am {self._char_age} years old"

player1 = PlayerCharacter("Adil", 21)

"""In this way anyone can gain access over our class data and modify it from outside.
and to avoid that we use '_' as the first letter of our attribute/method."""
# player1.speak = "boo"
# print(player1.speak)

print(player1.speak())


# Inheritance :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

"""We are making a game for 2 characters and both need to sign in.hence we
 will inherit the sign in function for both the character from the parent class.
 But the characters should have different attribute hence making attribute in subclass.
We need __init__  when we are making an attribute to the class."""

class User:
    def sign_in(self):
        return "logged in"

class Wizard(User):  # here we pass the parent class in subclass
    def __init__(self, name, magic):
        self.wiz_name = name
        self.wiz_magic = magic

    def attack(self):
        return f"attacking with magic, magic left: {self.wiz_magic}"

class Archer(User):
    def __init__(self, name, arrows):
        self.arc_name = name
        self.arc_arrows = arrows

    def attack(self):
        return f"attacking with arrows, arrows left: {self.arc_arrows}"

wizard_1 = Wizard("Mist", 77)
print(wizard_1.sign_in())  # now Wizard can use methods of User(because we passed it).
print(wizard_1.attack())
print("")
archer_1 = Archer("Robin", 49)
print(archer_1.sign_in())
print(archer_1.attack())
print("")

# To check(whether an object belongs to a specific class) instance

# wizard_1  # un hash this and put . to see methods which belong to object (base class).
print(isinstance(wizard_1, Wizard))  # subclass
print(isinstance(wizard_1, User))    # parent class
print(isinstance(wizard_1, object))  # object is the base class that python comes with(parent of parent class)


# Polymorphism :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

"""The example of polymorphism is the player_attack function, which is same for both the subclasses
 but returns different thing for each subclass(it's like player_attack has many forms)."""

class User:

    def attack(self):
        print("do nothing")


class Wizard(User):
    def __init__(self, name, power):
        self.wiz_name = name
        self.wiz_power = power

    def attack(self):
        User.attack(self)  # to have both attack of User and Wizard(only work if you print the result not return it).
        print(f"attacking with magic, magic left: {self.wiz_power}")

class Archer(User):
    def __init__(self, name, arrows):
        self.arc_name = name
        self.arc_arrows = arrows

    def attack(self):
        return f"attacking with arrows, arrows left: {self.arc_arrows}"

wizard_1 = Wizard("Mist", 77)
archer_1 = Archer("Robin", 49)

# Polymorphism

def player_attack(char):  # A function outside the class where we use our method and attribute(defined in class).
    return char.attack()
# here we should pass that argument(our objects) which has a method called attack.
player_attack(wizard_1)  # remember we have already printed the result, hence no print needed.
print(player_attack(archer_1))


---# super() :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

"""As we can see email attribute is not working because it is defined by __init__.
but sign_in method will work, hence we need to use super().__init__(param) to
 call the "attribute" from super(parent)class"""

class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        return "logged in"

class Wizard(User):
    def __init__(self, name, magic, email):
        super().__init__(email)  # super refers to super(parent)class which is User.
        self.wiz_name = name
        self.wiz_magic = magic

    def attack(self):
        return f"attacking with magic, magic left: {self.wiz_magic}"

wizard_1 = Wizard("Mist", 77, "mist@outlook.com")
print(wizard_1.email)  # remember, sign_in is method and email is an attribute.
print(wizard_1.sign_in())  # the syntax is different for both.
print(dir(wizard_1))  # for all methods that we can use.


# dunder methods :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

"""dunder method allow us to use python specific function, It works like a function
and we can also determine and change what that function does by modifying it's dunder method"""

class Toy:
    def __init__(self, color, age):
        self.toy_color = color
        self.toy_age = age
        self.my_dict = {"name": "Mojo Jojo",
                        "has_pets": True}

    def __str__(self):  # because we modified it,the  __str__ returns 'red' when called.
        return self.toy_color  # hash these two line to see what you get without modification.

    def __len__(self):
        return 100

    def __del__(self):
        return "deleted!"

    def __call__(self):
        return "yes??"

    def __getitem__(self, item):
        return self.my_dict[item]

action_figure = Toy("red", 4)

# __str__
print(action_figure.__str__())  # both do the same thing
print(str(action_figure))  # i.e, change the data type to string but we modified it

# __len__
print(action_figure.__len__())  # both do the same thing
print(len(action_figure))  # i.e, calculate number of characters but we modified it

# __del__
print(action_figure.__del__())  # avoid using delete(both dunder method and function)in real use,it can create some bug
# del action_figure   # for this to work you have to print the result in __del__.

# __call__
print(action_figure.__call__())  # __call__ is actually used(under the hood) to call different function in python
print(action_figure())  # hence we can use this syntax for call{() <-- we use this to call something in python}.

# __getitem__
print(action_figure["name"])  # __getitem__ was actually used to make the call for a value of key in a dictionary.


# Exercise: Extending List(inheritance) ::::::::::::::::::::::::::::::::::::::::::::::::::::::

"""Aim: to make an object which has all function and methods of a list
 and modify the result of only len() function. """

class SuperList(list):  # I did it myself.....alhamdulillah
    def __len__(self):
        return 1000


super_list = SuperList()
print(len(super_list))
super_list.append(5)
print(super_list)

print(issubclass(SuperList, list))  # To cross-check


# multiple inheritance :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

""" Try to avoid multiple inheritance, it makes our code complicated but powerful.
 Remember: With Great Power Comes Great Responsibility."""

class User:
    def sign_in(self):
        return "logged in"

class Wizard(User):
    def __init__(self, name, magic):
        self.wiz_name = name
        self.wiz_magic = magic

    def magic(self):
        return f"attacking with magic, magic left: {self.wiz_magic}"

class Archer(User):
    def __init__(self, name, arrows):
        self.arc_name = name
        self.arc_arrows = arrows

    def arrow(self):
        return f"attacking with arrows, arrows left: {self.arc_arrows}"

    def run(self):
        return f"Started Sprinting"

class Wizarcher(Wizard, Archer):  # this character has power of both the above characters
    def __init__(self, name, magic, arrows):
        """the two code below is another way of using super() syntax, can't use super()
           because we need multiple inheritance."""
        Wizard.__init__(self, name, magic)  # to get all attribute from Wizard
        Archer.__init__(self, name, arrows)  # to get all attribute from Archer

wizarcher = Wizarcher("Gearalt", 110, 76)  # 3 arguments because 3 param was given while initializing.

# now we can use all attribute and methods of the Wizard and Archer Classes.
print(wizarcher.arc_name)
print(wizarcher.wiz_name)
print(wizarcher.wiz_magic)
print(wizarcher.arc_arrows)
print(wizarcher.magic())
print(wizarcher.arrow())
print(wizarcher.run())


---# MRO - Method Resolution Order :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

""" MRO is a rule that python follows to determine when you run a method,
which one to run in a complicated inheritance structure like shown here.

|---A---|   3rd
|       |
C       B   2nd
|       |
|---D---|   1st
"""

class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B, C):  # Remember: B was given before C
    pass


print(D.num)  # we got 1 because it checked(after D) B first then C and got value of 'num'.
print(D.mro())  # to check the order


# Depth-First Search :

"""Depth-first search (DFS) is an algorithm for searching tree.The algorithm starts at the root node
 and explores as far as possible along each branch before backtracking."""

class X:
    pass
class Y:
    pass
class Z:
    pass
class U(X, Y):
    pass
class V(Y, Z):
    pass
class W(V, U, Z):  # The search goes to X and Y before Z due to Depth-First Search
    pass

print(W.__mro__)  # dunder method for MRO


# pure functions ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

"""A pure function will create less bug in a complex code.
   and makes the code clean. But we need our function to interact with outside
   world hence we cannot have a program with all pure functions."""

# A pure function
def multiply_by2(li_1):
    return [2 * item for item in li_1]

print(multiply_by2([1, 2, 3]))

# Not a pure function
def prod_2(li_2):
    print([2 * item for item in li_2])  # print is interacting with the console.

prod_2([1, 2, 3])

# Not a pure function
new_list = []   # this is outside the function.

def multi_2(li_3):
    for item in li_3:
        new_list.append(item * 2)
    return new_list

print(multi_2([1, 2, 3]))


# map() ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

"""As we can see, by using map() we are separating data and function.
Remember**: we don't need to call the function in map { () <-- no need of this after function }.
map() itself do the calling(of function) and looping(iteration) over my_list and we don't
have to write any code inside the function."""

my_list = [1, 2, 3]  # data

def multi_2(lst):  # function
    return lst * 2

print(map(multi_2, my_list))  # only give the memory location
print(list(map(multi_2, my_list)))  # taking my_list(arg) as lst(param) and looping over.
print(my_list)  # map create a new list instead of modifying my_list, hence we have a pure function.


---# filter() :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

"""A filter() function is used when we need to remove(or filter) some
item from the given input(usually a data structure).
Again no need to call the function."""

my_list = [1, 2, 3]  # data

def check_odd(item):  # function
    return item % 2 != 0

print(filter(check_odd, my_list))  # memory location
print(list(filter(check_odd, my_list)))
print(my_list)  # just like map(), filter() doesn't modify the outside list.


# zip() ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

"""A zip() function is used when we need to combine(zip into a tuple)
 multiple input to a single output(list/tuple of tuples).
Remember: No need to define a function for zip()."""

my_list = [1, 2, 3]  # data 1
your_tuple = (10, 20, 30)  # data 2, notice how this is a tuple and not a list.
their_list = [5, 10, 15]  # data 3

print(zip(my_list, your_tuple, their_list))  # memory location
print(list(zip(my_list, your_tuple, their_list)))  # write tuple instead of list to get tuple.
print(my_list)  # doesn't modify the outside list.


# reduce() ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from functools import reduce  # covered in module section(later on)

my_list = [1, 2, 3]  # data

def accumulator(acc, item):
    print(acc, item)  # this code is only to explain how reduce works, no need of this
    return acc + item

"""In reduce() we need to give 3 arguments.
here initial value of acc is set to 0 and my_list is passed as an arg for item(param).
the print statement inside the function shows us exactly each step taken by
reduce().
Remember: no need of calling the function, reduce work without being
 inside of a list unlike other functions, the default value of initial is 0,
 and we need to import reduce to use it."""

print(reduce(accumulator, my_list, 0))  # syntax -> reduce(function, iterable(data), initial)
print(my_list)  # doesn't modify the outside list


# lambda function :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

""" A lambda function is a small anonymous function that we only need to use once.
It can take any number of arguments, but can only return one expression.
Remember: we can't call a lambda function(it has no name)."""

from functools import reduce
my_list = [1, 2, 3]

# syntax -> lambda arguments: expression
print(list(map(lambda item: item * 2, my_list)))
print(list(filter(lambda item: item % 2 != 0, my_list)))
print(reduce(lambda acc, item: acc + item, my_list))  # initial is 0.


# Exercise: Lambda function :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# square

my_list = [5, 4, 3]  # got this one
print(list(map(lambda item: item**2, my_list)))

# list sorting - sort the list according to the second item in the tuple

a = [(0, 2), (4, 3), (9, 9), (10, -1)]  # didn't get this, quite tough

"""here, a.sort(), will sort the list according to the first item in tuple.
but we will use key(param in sort) and pass a (lambda)function to tell how to sort the list."""

a.sort(key=lambda x: x[1])  # x is each tuple inside the list
print(a)


---# List Comprehensions ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

"""A data structure comprehension is a quick way of looping over iterable, instead
 of looping and appending into an empty list."""

# syntax -> [expression for var in list if condition]
my_list = [num for num in range(0, 11)]
my_list2 = [num**2 for num in range(0, 11)]
my_list3 = list(num**2 for num in range(0, 11) if num % 2 == 0)  # little change in syntax

print(my_list)
print(my_list2)
print(my_list3)


# List Comprehensions 2 ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

a = [[1, 1], [1, 3], [5, 1], [6, 1]]
val = 5
v = [val in l for l in a]

print(v)
print(all(v))  # all() will return True only if all the item in iterable is True, else return False.


# Set and Dictionary Comprehensions ::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Set Comprehension :

"""syntax -> {expression for var in set if condition}"""
my_set = {num for num in range(0, 11)}
my_set2 = set(num ** 2 for num in range(0, 11) if num % 2 == 0)  # little change in syntax

print(my_set)
print(my_set2)

# Dict Comprehension :

simple_dict = {
    "a": 1, "b": 2, "c": 3
}

"""syntax -> {expression for key, value for key,value in dict.item() if condition}"""
my_dict = {k: v ** 2 for k, v in simple_dict.items()}
my_dict2 = {k: v ** 2 for k, v in simple_dict.items() if v % 2 == 0}
my_dict3 = {k*v for k, v in simple_dict.items()}  # a set
new_dict = {num: num * 2 for num in [1, 2, 3]}

print(my_dict)
print(my_dict2)
print(my_dict3)
print(new_dict)


# Exercise: Comprehension ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

"""get a list of alphabets(once) which are getting repeated"""

some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]  # did it Alhamdulillah
duplicate = list({i for i in some_list if some_list.count(i) > 1})
print(duplicate)


# Decorators :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

def hello():
    return "halloo's"

"""In python functions can be assigned, passed as an argument and can do many more
things just like a variable.
below, del is just deleting the name reference(hello) for the function, and now greet is
only pointing(defining) that function, it will show error if we print hello()."""

greet = hello
del hello  #
print(greet())
# print(hello())  # error, hello is no longer pointing(defining) the function


# Higher Order Functions(HOC) :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

"""Two types of Function can be HOC:
1. A Function which accepts another function passed as an argument.
2. A Function returning another Function.
   Ex: map(), reduce() etc."""


def out_func(say):  # HOC(1.)
    return say

def in_func():
    return "supp, how u doing!"

print(out_func(in_func()))  # function passed as an argument


def greet():  # HOC(2.)
    def fun():
        return 5
    return fun()  # returning function inside a function

print(greet())


---# Decorators 2 ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

"""Decorator is a function that wraps another function and enhances it or
 changes it."""

def my_decorator(func):  # defining decorator(an HOC, ex of both 1 and 2)
    def wrap_func():  # wrap ******* around the output of passed function
        print("*****************")
        func()
        print("*****************")
    return wrap_func  # remember not to call the 'wrapping' function while returning

@my_decorator
def hello():
    print("helllooo")

@my_decorator
def bye():
    print("see you later")

hello()
bye()


# Decorator Pattern ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

""" This below is the syntax(Pattern) of a decorator function(excluding the printing stars),
here we can add anything we want to enhance the called function."""

def my_decorator(func):
    def wrap_func(*args, **kwargs):  # to get multiple arguments and keyword arguments
        print("*********************************")
        func(*args, **kwargs)  # calling arguments and keyword arguments
        print("*********************************")
    return wrap_func

"""emoji is a default parameter, inside hello() we can put multiple
arguments and kwargs as we already defined it in decorator function."""

@my_decorator
def hello(greeting, age, emoji=":)"):  # remember the order of args and kwargs
    print(f'{greeting} {emoji}, I am {age} years old ')

hello("hello", 21)


# Application of Decorators ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

""" Making a code to see runtime of our code."""

from time import time  # covered in module section, later

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()  # initial time
        result = fn(*args, **kwargs)  # we assigned the fn to variable to return it later
        t2 = time()  # final time
        print(f'It took {t2 -t1} sec')
        return result
    return wrapper

@performance
def time_taken():   # if range was for a big number it will take more time, to reduce that we can use generator(later)
    for i in range(10000000):
        var = i * 5

time_taken()


# Errors in python :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

"""An error that crashes our program is called an Exception."""

# print(1 + "hello")  # type errors

# def hoo()  # syntax error
#     pass

# print(1 + so)  # name error

# li = [2, 4, 5, 7]  # index error
# li[6]

# dic = {1: 3, 2: 4}  # key error
# dic[4]

# 5/0  # Zero Division Error


---# Error Handling :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

""" Error Handling allow us to let the code running even if there are errors.
 Remember: we can use except keyword only once for a particular type of error."""

while True:  # while loop, so that we can ask for age again and again
    try:
        age = int(input("what is your age? "))
        print(age)  # A value error if we give a string
        print(10/age)  # A zero division error if we put age as 0

    except ValueError:  # to replace value error message with the code inside
        print("please enter a number")

    except ZeroDivisionError:  # to replace zero division error with the code inside
        print("please enter age higher than 0")

    else:
        print("thank you!")
        break  # to break out of loop if input is a valid number


# Error Handling 2 ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

""" Remember: you cannot concatenate error message(err here) with a string, have to use formatted string."""

def division(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as err:  # err will give exact information about error
        return f" The error --> {err}"

print(division(6, 0))


# Exercise: Error Handling ::::::::::::::::::::::::::::::::::::::::::::::::::::::

"""to check what happens when we put continue and break in between"""

while True:   # alhamdulillah
    try:
        age = int(input("what is your age? "))
        print(age)
        var = 10/age

    except ValueError:
        print("please enter a number")
        continue

    except ZeroDivisionError:
        print("please enter age higher than 0")
        break

    else:
        print("thank you!")
        break  # hash this and put a valid number in console to get last code

    finally:  # this will run(regardless of any condition above even break) at the end
        print("ok , i am done")

    print("can you here me")  # this won't run because of break, it is inside loop and break comes out of it


# Error Handling 3 :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

while True:
    try:
        age = int(input("what is your age? "))
        print(age)
        var = 10/age
        raise ValueError("hey, cut it out!")  # to display red message for any valid number, very rare use

    except ZeroDivisionError:  # this will still work, put 0
        print("please enter age higher than 0")


# Generators ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

"""Generators are function which can have a set of values but doesn't take
much memory , because it generate each value at a time in memory."""

range(100)  # not taking much memory
memory_taker = list(range(100))  # memory for each and every value till 100(well 99)

def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result

print(memory_taker)
print(make_list(100))


---# Generators 2 ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

"""Generators are a subset of iterable.
i.e, all generator are iterable(range) but not all iterable are generator(list).

yield pauses the function and comes back to it when we do next.
It remember each and every value inside the generator."""

def generator_func(num):
    for i in range(num):
        yield i * 2  # yield is keyword for a generator function instead of return

for item in generator_func(15):  # we are looping over generator function(since it's an iterable)
    print(item)  # we get one value at a time, hence less memory unlike make_list.
print("*******")

gen = generator_func(15)
next(gen)  # next can be used to call each value inside the generator
next(gen)  # next can be called until the range expires.
print(next(gen))  # put 1 above instead of 15 to see Stop Iteration error
print("*******")

def make_list(num):
    result = []
    for i in range(num):
        result.append(i * 2)
    return result

print(make_list(15))  # takes lot of memory


# Under The Hood Of Generators ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

"""Working of for loop under the hood.
As we can see that it is taking the same memory location for every item
in iterable."""

def forloop_working(iterable):
    iterator = iter(iterable)  # iter function is used to iterate over an iterable data type.
    while True:
        try:
            print(iterator)  # shows memory
            print(next(iterator) ** 2)

        except StopIteration:
            break


forloop_working([1, 4, 6, 7])

print("****************************")

"""Working of range(generator) function under the hood."""

class MyGen:  # using class because we have to create our own data type(range function).
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):  # returning self because we want the exact same functionality iter has.
        return self

    def __next__(self):  # needed for our for loop to go to next item between fist and last.
        if MyGen.current < self.last:
            num = MyGen.current  # this line can be removed but then we won't get 0.(Try yourself)
            MyGen.current += 1
            return num
        raise StopIteration  # to stop for loop when in last number.


gen = MyGen(0, 15)  # MyGen is working as range now.
for i in gen:
    print(i)


# Exercise: Fibonacci Numbers :::::::::::::::::::::::::::::::::::::::::::::::::::::::::

""" By using a generator function"""

def gen_fib(num):  # This was quite tough(couldn't do it), alhamdulillah
    a = 0
    b = 1
    for i in range(num+1):  # to get F20 also
        yield a  # remember, i am only getting 'a' as the output. 'b' is to increment in fibonacci series.
        temp = a
        a = b
        b = temp + b

for x in gen_fib(20):
    print(x)

"""By using a List"""

def lst_fib(num):
    result = []
    a = 0
    b = 1
    for i in range(num+1):  # to get F20 also
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result

print(lst_fib(20))


---# modules in python :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import utility

"""we can't import shop_cart directly like utility, because it is in
different package(a folder inside a project containing modules)."""

import shopping.shop_cart  # import package.module

print(shopping.shop_cart.buy("apple"))
print(utility.divide(2, 16))


# different ways to import - open 1 at a time ::::::::::::::::::::::::::::::::::::::::::::::

"""this way of importing makes our code concise and clean."""

# from utility import multiply, divide, max   # from module import function(or write "*"  to import all function)
# from shopping.shop_cart import buy  # from package.module import function
#
# print(buy("mango"))
# print(divide(12, 48))
# print(multiply(12, 48))
# print(max())   # this will overwrite the built-in max function, not good

"""But this is the best way to import so there is no name confusion and overwriting.
making a max function in utility, but max is also a built-in function."""

import utility
from shopping import shop_cart  # from package import module

print(shop_cart.buy("banana"))  # module.function
print(utility.max())
print(max([2, 4, 5]))  # built-in max function is working properly


# __name__ :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

"""the output '__main__' for print(__name__) is only for the module which we are running(main module) and
   for all the other imported module the output is their specific name like 'utility' etc.
(works only if print(__name__) was written inside the imported module, otherwise we won't see any module name.)"""

import utility
from shopping import shop_cart
print(__name__)

if __name__ == '__main__':  # to check whether the module is imported or main.
    print(shop_cart.buy("banana"))
    print(utility.max())
    print(max([2, 4, 5]))

print(type(utility.stud))  # as we can see stud(the object) belongs to a class(Student) which belongs to utility.


# python built-in modules :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import random as ran  # import module as 'rename the module'

print(ran)  # location of module

# two things to do when you don't know about the module

# help(random)  # 1. to learn about the module
# print(dir(random))  # 2. to get all the method which can be used

print(ran.random())  # random number between 0-1, due to 'ran' we don't have confusion here
print(ran.randint(72, 100))  # random integer between given arg

my_list = [1, 2, 3, 4, 5]
print(ran.choice(my_list))  # pick random item from iterator
ran.shuffle(my_list)  # shuffle modifies the list
print(my_list)


# python built-in modules 2 ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

"""sys.argv can only be used when we are running the code in terminal.
sys.argv[0] is name of the file itself, after that we can give parameters
by writing sys.argv[1] for 1st param and so on."""

# this is a copy of hello.py from desktop(just to show, run the original file from terminal)
import sys

first = sys.argv[1]
last = sys.argv[2]

print(f'Hiiii!! {first} {last}')


---# Exercise: Guessing game :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# this is a copy of sir_randomgame.py from desktop(just to show, run the original file from terminal)
import random
import sys
first = int(sys.argv[1])
last = int(sys.argv[2])
number = random.randint(first, last)

while True:
    try:
        guess = int(input(f"Guess a number between {first}-{last}:  "))
        if first <= guess <= last:
            if guess == number:
                print("yip!!! YOU WON ")
                break
            print("good choice but incorrect")
        else:
            print(f"hey noob... i said between {first}-{last}")
    except ValueError:
        print("Can only give integerB")
        continue


# installing packages online :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

""" go to settings > project: (name of project) > project interpreter > select project
> click '+' > search for package and install"""

import pyjokes
joke = pyjokes.get_joke("en", "all")
print(joke)


---# Useful Modules ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from collections import Counter, defaultdict, OrderedDict

"""Notice how Counter and OrderedDict are Classes and not Functions.
Remember to use Caps(first letter) while using them."""

lst = [1, 1, 2, 3, 4, 4, 4, 6, 6, 8, 7, 7, 7]
sen = "blah blah boos"
print(Counter(lst))  # return a dict showing number of times each item occurs in iterable.
print(Counter(sen))

# syntax: var = defaultdict(function, dictionary)
dic = defaultdict(lambda: 'does not exist', dict(a=1, b=2, c=3))
print(dic['english'])  # this will return the output of the function if the item doesn't exist in dictionary.

"""No need of OrderedDict from python 3.7, dicts are now ordered, get used to it
this is currently python 3.8."""

dic2 = OrderedDict({"a": 1, "b": 2})
dic3 = OrderedDict({"b": 2, "a": 1})
print(dic2 == dic3)  # the Order of k-v pair is different

dic4 = {"a": 1, "b": 2}
dic5 = {"b": 2, "a": 1}
print(dic4 == dic5)  # for a normal dict, the order doesn't matter


# Useful Modules 2 ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import datetime
from array import array

print(datetime.time(6, 44, 32))
print(datetime.datetime.now())
print(datetime.date.today())

""" An array is a type of list that can only have items of the same datatype
and we need to declare which datatype we want, here "i" stands for integer.
Remember: array takes less memory than list(but lists are dynamic)."""

arr = array("i", [1, 2, 3])  # can't have a str instead of 1
print(arr[0])


# How to Debug Code :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

"""The act of finding errors(bug) and removing them is called debugging.
Tips for debugging :
1. Use linter: A tool which analyzes source code to flag programming errors, bugs, stylistic errors,
               and suspicious constructs(basically the underline which comes while coding, it's built-in in pycharm).
2. Use IDE/text editor
3. ALWAYS READ THE ERROR AND IN WHICH LINE IT IS.
4. Use pdb : stands for Python Debugger, it's a built-in module which step through your code to find errors.
   a- to get all arguments inside the current function
   step - go to next line(from the line in which we used pdb.set_trace() )
   list - give the source code
   help - tells about pdb
   continue - exit out of pdb and run the code """

import pdb

def add(num1, num2):
    pdb.set_trace()  # to interact with pdb, remove this after debugging
    return num1 + num2

print(add(4, "44"))  # type error here


---# Working with files in python :::::::::::::::::::::::::::::::::::::::::::::::::::::::

"""this is a copy of script.py file from desktop which was used to open
   script.txt file and read it in cmd.Open this in vscode and run in cmd.
   Remember: python use the cursor(this vertical line) to read a file(txt)."""

my_file = open("script.txt")

print(my_file.read())  # after this the cursor goes to last letter and ends.
my_file.seek(0)  # to move the cursor back to first letter
print(my_file.read())  # you can only read the file once if you don't use seek.
my_file.seek(0)
print(my_file.read())
my_file.seek(0)

print(my_file.readline())  # print this again to read 2nd line as well and so on.
my_file.seek(0)
print(my_file.readlines()) # return a list with each line as item

my_file.close()  # always do this at the end


# Read, Write, Append :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

"""this is a better way of opening files in python.
   The default param is mode="r", for read only
   mode='w' means write only.
   mode='r+' means read and write
   my_file.write() will replace everything in the txt file(when mode='w').
   my_file.write() will overwrite(each letter) in the txt file(when mode='r+').
   Remember: To avoid overwriting/replacement use append mode."""

with open('script2.txt', mode='a') as my_file:  # "a" for append
    text = my_file.write("supp bro")
    text = my_file.write(":)")
    print(text)  # return len(str) of last append

"""mode='w' can create new file if it doesn't exist, happy.txt file
   got created in the same dir as of script.py"""

with open('happy.txt', mode='w') as new_file:
    text1 = new_file.write("me happy now :)")
    print(text1)


---# File Paths :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

"""down below 'script2.txt' is the relative address compare to script2.py
   let's say script2.txt was in some folder 'som' relative to script2.py
   then we should write 'sum\script2.txt'.We can also give absolute address
   like 'C:\Users\nawaz\Desktop\script2.txt' which will work irrespective of
   script2.py location."""

 with open('script2.txt', mode='w') as my_file:
    text = my_file.write("supp bro")
    print(text)


# File IO Errors ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

try:
    with open("happy.txt", mode='r') as my_file:
        print(my_file.read())
except FileNotFoundError as err:
    print("File does not exist")
    raise err
except IOError as err:  # happens when computer has issue with reading or writing file
    print("IO error")
    raise err


# Exercise: Translation :::::::::::::::::::::::::::::::::::::::::::::::::::::::

"""This is the copy of code from scripttrans.py which is used to translate
english text in translate.txt to japanese."""

from translate import Translator  # downloaded this lib from pypi.org
# tran = Translator(to_lang="ja")  # how to use this translate library
# print(tran.translate("this is a pen"))

try:
    with open('translate.txt', mode = 'r') as my_file:
        tran = Translator(to_lang="ja")
        print(tran.translate(my_file.read()))
except FileNotFoundError as err:
    print("Something is Wronggg!")


---# Regular Expressions ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

"""Regex are generally used for validation and searches in python and it gives
a lot more information than just simple validation."""

import re

string = 'search this inside of this text please!'
string2 = 'this'
print('this' in string)  # just give True or False

a = re.search('this', string)  # gives an object with many info
print(a)
print(a.span())  # give index of first occurrence
print(a.start())
print(a.end())
print(a.group())  # useful for multiple searches
print(re.search('try', string))  # 'try' doesn't exist, so None

# Another way in which we first give the pattern ('this' here)
pat = re.compile('this')
b = pat.search(string)  # only have to give string, already gave pattern
print(b)
print(pat.findall(string))

print(pat.fullmatch(string))  # check whether pattern is exactly same as string
print(pat.fullmatch(string2))

print(pat.match(string))  # check whether string starts with pattern
print(pat.match(string2))


# Regular Expressions 2 ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

"""The pattern given below is called as Sets of regex([given inside this]) which is searching for a
letter from a-z or A-Z followed by anything(represented by .) and then followed by a.Hence we got 'sea'."""

import re

pattern = re.compile(r"([a-zA-Z]).([a])")  # r stands for 'raw string'
string = 'search this inside of this text please!'

a = pattern.search(string)
print(a.group())  # mind this is group not groups
print(a.group(1))
print(a.group(2))


# Regular Expressions 3 ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

"""Checking for a valid e-mail address.....
the '+' sign in r"" means the length can be as much as we want and it is written
after defining the set r"[]+".
also we write r'\.' to match specifically a dot in string, if we only write r'.' then
that will take any match(we already know this). Hence to avoid that we write '\.'"""

import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")  # copied this from internet
while True:
    string = input("Write your email: ")
    if pattern.search(string) is None:
        print("Wrong e-mail address, Type again")
    else:
        print("Submitted your e-mail :)")
        break


---# Exercise: Password Validation ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

"""Make a password checker which:
    1.  At least 8 characters which take uppercase, lowercase and numbers
    2. take @#$% as special characters only.
    3. Should end with a number."""

import re

pattern = re.compile(r"[a-zA-Z0-9@#$%]{8,}\d")  # {8,} for 1. and \d(d for digit) for 3.
while True:
    string = input("Make a password with at least 8 characters: ")
    if pattern.fullmatch(string) is None:
        print("Not Valid, Type again")
    else:
        print("Saved your password :)")
        break


# Unittest :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# copied code of main.py in desktop\testing

def do_stuff(num=0):
    try:
        if num or num == 0:
            return int(num) + 5
        return 'please enter a number'
    except ValueError as err:  # for the 2nd test
        return err

# copied code of test.py in desktop\testing

import unittest  # used to make test cases for code we write
import main  # import the file we wanna test

"""In the 2nd test we wrote assertIsInstance instead of assertEqual because 'shark' is a type of ValueError
and not equal to it.
some command to run this file are:
1. python test.py
2. python -m unittest
3. python -m unittest -v {detailed one}"""

class TestMain(unittest.TestCase):
    def setUp(self):  # used when we  need comment or default var for every single test before it runs
        print("about to test the function")

    def test_do_stuff(self):
        test_para = 10  # writing input for function in main.py
        result = main.do_stuff(test_para)  # giving input as arg in the function
        self.assertEqual(result, 15)  # assertEqual is used to check whether two param are equal

    def test_do_stuff2(self):
        """this test is for a str input"""
        test_para = "shark"
        result = main.do_stuff(test_para)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_para = None
        result = main.do_stuff(test_para)
        self.assertEqual(result, 'please enter a number')

    def test_do_stuff4(self):
        test_para = 0
        result = main.do_stuff(test_para)
        self.assertEqual(result, 5)

    def tearDown(self):  # this runs after each test
        print("cleaning up")

"""main() below is a method and not a reference to main.py file, we have to write
unittest.main() to run all test cases even if the file name was something else."""

if __name__ == '__main__':  # this is helpful when there are multiple files
    unittest.main()  # to run all test cases


---# Exercise: Testing ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# copied code of main2.py in desktop\testing

import random

def guess_game(guess, answer):  # we made it to a function so that it is easy to run tests.
    if 0 < guess < 11:
        if guess == answer:
            print("you won the guessing game! ")
            return True
    else:
        print("hey bozo, I said 1-10 ")
        return False


if __name__ == "__main__":  # if we write this in test2.py, this whole loop will run in testing which we don't want.
    gen_random = random.randint(1, 10)  # these code won't run in test because it is not main module.
    while True:
        try:
            my_number = int(input("guess a number from 1-10: "))
            if guess_game(my_number, gen_random):  # here the function above runs
                break
        except ValueError:
            print("please enter a number ")
            continue

# copied code of test2.py in desktop\testing

import unittest
import main2

class TestGame(unittest.TestCase):
    def test_game(self):
        result = main2.guess_game(5, 5)
        self.assertTrue(result)

    def test_game2(self):
        result = main2.guess_game(5, 0)
        self.assertFalse(result)

    def test_game3(self):
        result = main2.guess_game(11, 5)
        self.assertFalse(result)

    def test_game4(self):
        result = main2.guess_game(1, '11')
        self.assertFalse(result)

unittest.main()


---# Images with python :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

"""this is the copy of code from images.py(vs code) in C:\Users\nawaz\Desktop\image playground.
    Unable to install Pillow(new version of PIL) library in pycharm."""

from PIL import Image, ImageFilter


img = Image.open('.\Pokedex\oshawott.jpg')

print(img)  # we converted jpg into an instance(object) of Image
print(img.format)  # the original image was png, i later converted it to jpg
print(img.size)
print(img.mode)
print(dir(img))  # all method in Image class

"""png supports these image filters, we will get an error if we use jpg format."""

filter_img = img.filter(ImageFilter.BLUR)
filter_img.save("oshawoott_blur.png", 'png')

filter_img2 = img.filter(ImageFilter.SMOOTH)
filter_img2.save("oshawoott_smooth.png", 'png')

filter_img3 = img.filter(ImageFilter.SHARPEN)
filter_img3.save("oshawoott_sharpen.png", 'png')

filter_img4 = img.convert('L')  # convert RGB to B&W
filter_img4.save("oshawoott_b&w.png", 'png')


# Images with python 2 :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# copy of code in images2.py, in  C:\Users\nawaz\Desktop\image playground.

from PIL import Image, ImageFilter

img = Image.open('.\Pokedex\pikachu.jpg')

filtered_img = img.convert('L')
filtered_img.show()  # to show the image with filters

upside_down = filtered_img.rotate(180)  # to rotate image
upside_down.show()

filtered_img2 = img.resize((300,300))  # make sure to give a tuple in resize
filtered_img2.save("mini-pikachu.png", 'png')

box = (100,100,400, 400)
crop = img.crop(box)  # need 4 pixel location inside a tuple
crop.save("crop-pikachu.png", 'png')


# Images with python 3 ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# copy of code in images3.py, in  C:\Users\nawaz\Desktop\image playground.

from PIL import Image, ImageFilter

img = Image.open('.\Pokedex\original.jpg')
new_img = img.resize((400,300))  # resize changes the aspect ratio while compressing
new_img.save("mini-original.png", 'png')
print(new_img.size)  # size is same as given

"""thumbnail method doesn't return any value so we can't assign it.
    It modifies the object."""

img.thumbnail((400, 300))  # thumbnail try to keep the same aspect ratio while compressing
img.save("thumbnail-original.png")
print(img.size)  # size is different to keep the aspect ratio same as actual pic.


---# Exercise: JPG to PNG Pokedex Converter :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# this is the copy of code from JPGtoPNGconverter.py
import sys
import os
from PIL import Image

"""Use this command only to run this file:>>> python .\JPGtoPNGconverter.py .\Pokedex\ .\new\ <<<:
   we need that \ after writing file name."""


# step1: grab first and second argument

first = (sys.argv[1])
last = (sys.argv[2])

# step2: check if new file exist, if not create
if os.path.exists(last) == False:
    os.mkdir(last)
    pass
else:
    pass

#step3: loop through pokedex, change extension and save it in new dir
for filename in os.listdir(first):
    img = Image.open(f"{first}{filename}")
    # clean_name = os.path.splitext(filename)[0]
    """above code split filename and extension into tuple so that we can only use filename and add .png
    I just used replace method instead of above code."""
    img.save(f"{last}{filename}".replace('jpg','png'), 'png')
    print("all done")


---# PDFs with python ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# this is the copy of code pdf.py from pdf playground in Desktop.
import PyPDF2

"""Use 'rb'(read binary) mode instead of 'r' because python can read only binary and unlike
txt file pdf file can only be read by 'rb'.
'read' is the object for whole pdf and 'page' is the object for a specific page.
open tilt.pdf from adobe to see the change."""

with open('dummy.pdf', 'rb') as pdf_file:  # relative address wrt pdf.py
    reader = PyPDF2.PdfFileReader(pdf_file)
    print(reader.numPages)  # give number of pages
    page = reader.getPage(0)  # page is an object created out of read object(inheritance)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)  # addPage is required otherwise new_file has zero pages, won't open
    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)


# Exercise: PDF merger::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# this is the copy of code pdf_merger.py from pdf playground in Desktop.
import sys
import PyPDF2

"""command-->>python pdf_merger.py dummy.pdf twopages.pdf tilt.pdf"""

inputs = sys.argv[1:]  # for multiple file to merge

def pdf_merger(pdf_lst):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_lst:
        print(pdf)  # this line is not required, just to show all files in terminal
        merger.append(pdf)
    merger.write('super.pdf')

pdf_merger(inputs)


# Exercise: Watermark :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# this is the copy of code my_watermark.py from pdf playground in Desktop.
import PyPDF2

with open('super.pdf', 'rb') as old_file:
    pdf = PyPDF2.PdfFileReader(old_file)  # read content of the original file
    with open('wtr.pdf', 'rb') as watermark:
        water = PyPDF2.PdfFileReader(watermark)  # read content of the watermark
        pdf_writer = PyPDF2.PdfFileWriter()  # making new object to add all the watermarked pages
        for i in range(pdf.numPages):  # get all pages from the original PDF in a loop
            page = pdf.getPage(i)
            water_page = water.getPage(0) # take first page of wtr.pdf
            page.mergePage(water_page)  # merge each page with first page of wtr.pdf
            pdf_writer.addPage(page)
        with open('supermark.pdf', 'wb') as output:
            pdf_writer.write(output)  # return the new object

# this is the copy of code sir_watermark.py from pdf playground in Desktop.
import PyPDF2

template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
  page = template.getPage(i)
  page.mergePage(watermark.getPage(0))
  output.addPage(page)

  with open('sir_watermark.pdf', 'wb') as file:
    output.write(file)


---# Sending Emails With Python ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# this is the copy of code email_sender.py from email playground in Desktop.
import smtplib

'''SMTP stands for Simple Mail Transfer Protocol. SMTP is a set
 of communication guidelines that allow software to transmit an
  electronic mail over the internet .
  It is needed to send our mail in this program.'''

from email.message import EmailMessage

"""This code will only work if you do these things:
   1. Allow less secure app access{not recommended for personal account} for the
      account FROM which you are sending email.
   2. DO NOT use BOH(wifi).
   3. [optional]Set the timeout in smtplib.SMTP to 120, default is 4 hence the
      connection to gmail will not happen in that short amount of time."""

email = EmailMessage()
email['from'] = 'droom.vroom123@gmail.com'
email['to'] = 'droom.croom.123@gmail.com'
email['subject'] = 'Writing Python code to send mail'

email.set_content('It is working now and you are probably reading this content.')

with smtplib.SMTP(host='smtp.gmail.com', port=587,timeout=120) as smtp:
  smtp.ehlo()  # Identify yourself to an E(enhanced)SMTP server
  '''smtp.starttls()-->Put the SMTP connection in TLS (Transport Layer Security) mode.
     All SMTP commands that follow will be encrypted. You should then call ehlo() again.'''
  smtp.starttls()  #
  smtp.ehlo()
  smtp.login('droom.vroom123@gmail.com', '#12openvroom')
  smtp.send_message(email)
print('Message Sent!!!')


---# Sending Emails With Python 2 ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# this is the copy of code email_sender2.py which was used to send an html text(index.html){down below}.

"""
<!DOCTYPE html>
<html>
<head>
</head>
<body>
    You just won so much money $name
</body>
</html> """

import smtplib
from email.message import EmailMessage
from string import Template

"""pathlib.Path --> To get the html code in python, same as os.path
   but for this case it is better because it has a read method already."""

from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'droom.vroom123@gmail.com'
email['to'] = 'droom.croom.123@gmail.com'
email['subject'] = 'Writing Python code to send an html text.'

"""substitute method will replace $variable(name) in the template string.
   If we don't write html(in set_content method) the whole index.html will be sent as a text."""

email.set_content(html.substitute({'name': 'Nawaz'}),'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587,timeout=120) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.ehlo()
  smtp.login('droom.vroom123@gmail.com', '#12openvroom')
  smtp.send_message(email)
print('Message Sent!!!')


---# Password Checker Project :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# this is the copy of code basics.py from password checker in Desktop.

import requests
"""requests module allows us to connect to the url, it is like a
   browser without interface."""

"""sir will talk about API in web dev section, later.
   API stands for Application Programming Interface. An API is a
   software intermediary that allows two applications to talk to each other."""

url = 'https://api.pwnedpasswords.com/range/' + 'password123'
res = requests.get(url)
print(res)  # response 400 means it is bad request, and something wrong with API(we need 200)

# giving SHA1 hashed of the same password, still insecure
url1 = 'https://api.pwnedpasswords.com/range/' + 'CBFDAC6008F9CAB4083784CBD1874F76618D2A97'
res1 = requests.get(url1)
print(res1)

"""K-anonymity might be described as a ‘hiding in the crowd’ guarantee.
   Our password shares the first 5 character of the hashed format with other passwords in the data base
   so that we will get a list of password starting with this 5 characters and from that we can pick ours
   without telling the API what is our complete password."""

url2 = 'https://api.pwnedpasswords.com/range/' + 'CBFDA'
res2 = requests.get(url2)
print(res2)  # response 200 is good request


---# Password Checker Project 2 :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# this is the copy of code checkmypass.py from password checker in Desktop.

import requests
import hashlib  # to hash our password
import sys

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:  # we only need response 200
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res

def get_password_leaks_count(hashes, hash_to_check):
    # this function was defined after pwned_api_check function to use in it.
    hashes = (line.split(':') for line in hashes.text.splitlines())  # read about splitlines(), why is it needed
    for h, count in hashes:  # h is tail hashes of all password with same first5_char, count is time it got hacked
        if h == hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    # checking password exists in API response or not
    sha1pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1pass[:5], sha1pass[5:]
    response = request_api_data(first5_char)
    print(response)
    return get_password_leaks_count(response, tail)

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times... you should probably change it>')
        else:
            print(f'{password} was NOT found. Carry on!')
    return 'done!'

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))  # we will get done! at the end because we exiting from the main function.


# this part is just to show how we got sha1pass in pwned_api_check function:
# def pass_to_hash_steps(secret):
#     print(secret)
#     print(secret.encode('utf-8'))  # this is needed to convert into hash
#     print(hashlib.sha1(secret.encode('utf-8')))  # converted to hash object
#     print(hashlib.sha1(secret.encode('utf-8')).hexdigest())  # using hexdigest method to get hash code(hexadecimal)
#     print(hashlib.sha1(secret.encode('utf-8')).hexdigest().upper())  # need hash code in caps
# pass_to_hash_steps('123open')


# Twitter bot ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# this is the copy of code basics.py from myztm_bot[twitter] file in Desktop.

import tweepy

# to authenticate our account(go to twitter api/ app)
auth = tweepy.OAuthHandler('qI0sWgb3RSYuAf5Te0jhZumJk', 'bQCmvPM3pMY2hH8vns1KBCqXQIrQBEk6FZc2bpQlg3AEfEJKSF')
auth.set_access_token('1247507374362910721-vfbXGBKZyMfKFmj5KhmYEQVxQgeaOV', 'ez8KhQ8sjCvo4HZVnpQ5vuSnTFzodXuFpUiH0njR39vzy')

api = tweepy.API(auth)

user = api.me()

# notice how these are attribute and not method
print(user.name)
print(user.screen_name)  # twitter handle
print(user.followers_count)
# print(dir(user))  # to check all methods and attr in user class

# to get all message from home timeline
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)


# Twitter bot 2 ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# this is the copy of code generous_bot.py from myztm_bot[twitter] file in Desktop.

import tweepy
import time

auth = tweepy.OAuthHandler('qI0sWgb3RSYuAf5Te0jhZumJk', 'bQCmvPM3pMY2hH8vns1KBCqXQIrQBEk6FZc2bpQlg3AEfEJKSF')
auth.set_access_token('1247507374362910721-vfbXGBKZyMfKFmj5KhmYEQVxQgeaOV', 'ez8KhQ8sjCvo4HZVnpQ5vuSnTFzodXuFpUiH0njR39vzy')

api = tweepy.API(auth)
user = api.me()

'''We need this limit_handler function because we are constantly hitting the twitter API
 which is hitting the twitter server(only if you have 1000s of followers) and if everyone do this at
 same time then server may crash, hence we are using RateLimit so that we can ask for data for a particular
 time then again we have to wait for sometime(100ms) to get the data again.
 Remember: it's always a good practice to add limit_handler.'''

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()  # cursor is a generator
    except tweepy.RateLimitError:
        time.sleep(100)  # time in ms, so for 0.1sec the code pauses.

# Generous Bot(always follow back)
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    follower.follow()
    break


---# Twitter bot 3 ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# this is the copy of code narcissist_bot.py from myztm_bot[twitter] file in Desktop.

import tweepy
import time

auth = tweepy.OAuthHandler('qI0sWgb3RSYuAf5Te0jhZumJk', 'bQCmvPM3pMY2hH8vns1KBCqXQIrQBEk6FZc2bpQlg3AEfEJKSF')
auth.set_access_token('1247507374362910721-vfbXGBKZyMfKFmj5KhmYEQVxQgeaOV', 'ez8KhQ8sjCvo4HZVnpQ5vuSnTFzodXuFpUiH0njR39vzy')

api = tweepy.API(auth)
user = api.me()

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(100)

search_string = 'python'  # you can write your name here too
number_of_tweets = 4  # number of tweets you want to like

# Narcissist Bot( like any recent tweet in which search_string is mentioned)
for tweet in tweepy.Cursor(api.search, search_string).items(number_of_tweets):
    try:
        tweet.favorite()  # to like
        # tweet.retweet()  # to retweet(don't do)
        print("I liked that tweet")
    except tweepy.TweepError as t:
        print(t.reason)
    except StopIteration:
        break


# SMS with Python ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# this is the copy of code sms.py from sms playground file in Desktop.

from twilio.rest import Client

'''twilio is an API for sending and receiving call, sms and many more.
   Already have an account there: https://www.twilio.com/console .'''

 # copied the below code from API and added the body
account_sid = 'ACbf554a6dccdd7c9b94549d229a0195c9'
auth_token = '7ab0ce348eb432588ed1b289825a055a'
client = Client(account_sid, auth_token)

message = client.messages.create(
                                from_='+12562777610',
                                body= "sending this message via python",
                                to='+916383385969')
print(message.sid)










