
countries = ['Finland', 'Germany', 'Sweden', 'Ireland', 'Turkey']

output = list(filter(lambda country: 'and' in country.lower(), countries))

print(output)

countries = ['Finland', 'Germany', 'Sweden', 'Ireland', 'Turkey']

print("--------------------------------------------------------------------------")

def contains_and(country):
    return 'and' in country.lower()

filtered_countries = list(filter(contains_and, countries))

print(filtered_countries)
