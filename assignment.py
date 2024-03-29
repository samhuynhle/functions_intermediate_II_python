# # 1. Update Values in Dictionaries and Lists
# x = [ [5,2,3], [10,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# # Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# x[1][0] = 15
# # Change the last_name of the first student from 'Jordan' to 'Bryant'
# students[0]['last_name']='Bryant'
# # In the sports_directory, change 'Messi' to 'Andres'
# sports_directory['soccer'][0]='Messi'
# # Change the value 20 in z to 30
# z[0]['y']=30

# print(x[1][0])
# print(students[0]['last_name'])
# print(sports_directory['soccer'][0])
# print(z[0]['y'])

# 2. Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of dictionaries,
# the function loops through each dictionary in the list and prints each key and the associated value.
# For example, given the following list:

# students = [
#          {'first_name':  'Michael', 'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'},
#          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#          {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]
# def iterateDictionary(some_list):
#     for some_lists_index in some_list:
#         print(f"first_name - {some_lists_index['first_name']}, last_name - {some_lists_index['last_name']}")
    # I use some_lists_index as the variable name for the for loop because I am at first sifting through a list of dictionaries. some_lists_index is sifting through the
    # lists' index, which are the individual dictionaries.
    # some_lists_index['first_name'] is how I am pulling the value from each dictionary. I'm getting the value by calling the key of the specific dictionary.

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# iterateDictionary(students)

# Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name,
# the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:

# def iterateDictionary2(key_name, some_list):
#     for some_lists_index in some_list:
#         print(some_lists_index[key_name])
# iterateDictionary2('first_name', students)
# iterateDictionary2('last_name', students)

# Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, 
# prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for some_key in some_dict:
        print(len(some_dict[some_key]))
        for some_value in some_dict[some_key]:
            print(some_value)
printInfo(dojo)

# function printInfo has one defined paramater, some_dict, which will take a dictionary in as an argument.
# We are passing in the dictionary, dojo, into the function printInfo().
# The first for loop in function printInfo will pull the key's of the dictionary, dojo.
# Within every loop, the code is printing the length of the list, which is the value of the key.
# Wtithin every loop, there is a nest for loop, which will print the values of the list.