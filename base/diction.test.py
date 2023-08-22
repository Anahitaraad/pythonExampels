student_scores = {
    'harry': 81,
    'ron': 78,
    'hermion': 99,
    'draco': 64,
    'neville': 62
}

print(student_scores)
new_dictionary = {}
for key, value in student_scores.items():
    if value<100 and value>= 91 :
        new_dictionary[key] ='outstanding'
    if value < 90 and value >= 81:
        new_dictionary[key] = 'exceeds'
    if value < 80 and value >= 71:
        new_dictionary[key] = 'acceptable'
    if value <= 70 :
        new_dictionary[key] = 'failed'

print(new_dictionary)
