python_dictionary = {
    'Bug': 'An error in a program that prevents the program from running as expected',
    'Function': 'A piece of code that you can easily call over and over again'
                     }
print(python_dictionary)
python_dictionary['Function'] = 'Value has been changed '
print(python_dictionary)
# Retrieving items from a dictionary/ Index.
print(python_dictionary['Bug'])
# Adding new items to the dictionary.
python_dictionary["Loop"] = 'The action of doing something over and over again'
print(python_dictionary)
# Create an empty dictionary
new_dic = {}
# Wipe an existing dictionary
python_dictionary = {}
print(python_dictionary)
# Edit an item in a dictionary
python_dictionary["Loop"] = "Changed"
print(python_dictionary)
# print(programming_dictionary)
# Loop though a dictionary
for key in python_dictionary:
    print(key)

for key, value in python_dictionary.items():
    print(key)
    print(value)

values_of_python_dic = python_dictionary.values()
print(values_of_python_dic)
print(python_dictionary.values())
#Nesting
capitals = {
    "Italy": ["Milan","Rome", "Napoli"],
    "Sweden": "Karlskrona"
}
print(capitals)

# Nesting a list in a dictionary
capitals["Italy"].append("Fredrik")
print(capitals["Italy"])

# Nesting Dictionary in a Dictionary
capitals = {
    "Italy": {"cities_visited": ["Milan", "Rome", "Napoli"]},
    "Sweden": "Karlskrona"
}
print(capitals)
# Challenge, I want you to try and change the Italy entry so that it contains another dictionary.
# Fo the nested dictionary use the key cities_visited

# Nesting Dictionary in a List
dic_in_list = [{"Italy": "Milan",
                "Sweden": "Stockholm",
                "Iran": "Tehran"
                },
               {'Alaa': "Teacher",
                "Anna": "Student"}
               ]
print(dic_in_list[1]["Anna"])