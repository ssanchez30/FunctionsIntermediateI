# 1. Update Values in Dictionaries and Lists

x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

# 1.1 Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15
print(x)

# 1.2 Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0].update({'last_name': 'Bryant'})
print(students)

# 1.3. In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

# 1.4 Change the value 20 in z to 30
z[0]['y'] = 30
print(z)

print("**************End Exercise 1 **********************")


students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary(dictionary):
    for i in range(len(dictionary)):
        for key, value, in dictionary[i].items():
            print(f"{key} - {value},")


iterateDictionary(students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;

print("\n*** BONUS ***")
def iterateDictBonus(dictionary):
    for valor in dictionary:
        print(f"first_name - {valor['first_name']}, last_name - {valor['last_name']}")

iterateDictBonus(students)

# bonus to get them to appear exactly as below!)
#first_name - Michael, last_name - Jordan
#first_name - John, last_name - Rosales
#first_name - Mark, last_name - Guillen
#first_name - KB, last_name - Tonel


print("**************End Exercise 2 **********************")


def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        print(some_list[i][key_name])


iterateDictionary2('last_name', students)

print("**************End Exercise 3 **********************")

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(some_dict):
    for key in some_dict:
        print(f"{len(some_dict[key])} {key.upper()}")
        for i in range(0, len(some_dict[key]), 1):
            print(some_dict[key][i])
        print("")


printInfo(dojo)

print("**************End Exercise 4 **********************")