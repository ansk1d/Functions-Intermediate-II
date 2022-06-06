x = [[5, 2, 3], [10, 8, 9]]
x[1][0] = 15
###########################
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
students[0]['last_name'] = "Bryant"
###############################
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = "Andres"
#############################
z = [{'x': 10, 'y': 20}]
z[0]['y'] = 30
####################################################
#
# 2Iterate Through a List of Dictionaries


def iterateDictionary(list):
    for i in range(0, len(list)):
        for key, val in list[i].items():
            if key == "first_name":
                print(key, "-", val+",", end=" ")
            else:
                print(key, "-", val)


students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
iterateDictionary(students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel
##
##########################################
#
# 3 Get Values From a List of Dictionaries


def iterateDictionary2(key_name, some_list):
    for i in range(0, len(some_list)):
        print(some_list[i][key_name])

####################################
# 4Iterate Through a Dictionary with List Values


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(some_dict):
    for key in some_dict:
        print(len(some_dict[key]), key.upper())
        for i in some_dict[key]:
            print(i)
        print("")


printInfo(dojo)
