#This is the shortcut way of creating a NEW LIST
name='Bellah'
lst=[i for i in name]
print(type(lst))
print(lst)

#generating a list of numbers
numbers=[i for i in range(21)]
print(numbers)

multiply=[i*10 for i in range(11)]
print(multiply)

tuples_list=[(i,i*i) for i in range(11)]
print(tuples_list)

dict_list=[{i,i*10} for i in range(6)]
print(dict_list)
print(type(dict_list))

#List comprehension can be combined with if expression
even_numbers=[i for i in range(21) if i%2==0]
print(even_numbers)

odd_numbers=[i for i in range(21) if i%2!=0]
print(odd_numbers)

#filter out positive even numbers
def filter_positive(nums):
    positive_even_numbers=[i for i in nums if i%2==0 and i>0]
    return positive_even_numbers
nums=[-8,-7,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
print(filter_positive(nums))

# Flattening a three dimensional array
list_of_lists=[[1,2,3],[4,5,6],[7,8,9]]
flattened_list=[number for row in list_of_lists for number in row]
print(flattened_list)


#Lambda Function
#This is a small anonymous function without a name
add_two_nums=lambda a,b : a+b
print(add_two_nums(2,3))

#self invoking lambda fctn
print((lambda a,b : a+b)(2,4))

square=lambda x,y: x*(y*y)
print(square(2,4))

cube= lambda x:x**3
print(cube(5))

#multiple variables
multiple_variables=lambda a,b,c: a**2-3 *b +4*c
print(multiple_variables(2,5,10))


#Lambda Function inside another Function
def power (x):
    return lambda n:x**n
cube=power(2)(3)
print(cube)
two_power_of_five = power(2)(5) 
print(two_power_of_five) 


             #EXERCISES
# Filter only negative and zero in the list using list comprehension
def filter_numbers():
 numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
 only_negative_and_zero=[number for number in numbers if number<=0]
 return only_negative_and_zero
print(filter_numbers())

# Flatten the following list of lists of lists to a one dimensional list :
def flatten():
 list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
 flattened_list=[number  for sublist in  list_of_lists for row in sublist for number in row]
 return flattened_list
print(flatten())
# Using list comprehension create the following list of tuples:

# [(0, 1, 0, 0, 0, 0, 0),
# (1, 1, 1, 1, 1, 1, 1),
# (2, 1, 2, 4, 8, 16, 32),
# (3, 1, 3, 9, 27, 81, 243),
# (4, 1, 4, 16, 64, 256, 1024),
# (5, 1, 5, 25, 125, 625, 3125),
# (6, 1, 6, 36, 216, 1296, 7776),
# (7, 1, 7, 49, 343, 2401, 16807),
# (8, 1, 8, 64, 512, 4096, 32768),
# (9, 1, 9, 81, 729, 6561, 59049),
# (10, 1, 10, 100, 1000, 10000, 100000)]
result = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(result)


# Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flatten = [[country.upper(), country[:3].upper(), city.upper()] for sublist in countries for (country, city) in sublist]
print(flatten)

 # output:
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]


# Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [{'country': 'FINLAND', 'city': 'HELSINKI'},
# {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
# {'country': 'NORWAY', 'city': 'OSLO'}]
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dictionaries = [{'country': country.upper(), 'city': city.upper()} for sublist in countries for (country, city) in sublist]
print(dictionaries)



# Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# output
# ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']

concat=[(i +' '+ n) for sublist in names for (i,n) in sublist ]
print(concat)


# Write a lambda function which can solve a slope or y-intercept of linear functions.
slope=lambda m,x,c: (m*x)+c
print(slope(1,2,3))