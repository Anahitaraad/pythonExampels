travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]
# 🚨 Do NOT change the code above
# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇
diction = {}
def add_new_country(country,visits,cities) :
    diction['country'] = country
    diction['visits'] = visits
    diction['cities'] = cities
    travel_log.append(diction)

add_new_country('italy', 2, ['milan', 'rome'])
print(travel_log)

# diction['country'] = input('which country?')
# diction['visits'] = input(f'how many times have u been there?')
# diction['cities'] = list(input(f'which cities have u visited?').split(','))