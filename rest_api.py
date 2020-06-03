# requests IS A EXTERNALLY DOWNLOADED CODE PACKAGE
import requests
# GET REQUEST
# BUILD TARGET URL(= PATH+ARGUMENTS)
# WILL RECEIVE JSON FILE WHICH I NEED TO PARSE INTO DICTIONARY

path = 'http://api.postcodes.io/postcodes/'
arguments = 'N17HZ'

target_url = path + arguments
print(target_url)

# GET REQUEST
response = requests.get(target_url)

# PRINTS RESPONSE AND STATUS CODE
print(response)

# PRINTS AS JSON FILE/DICTIONARY
print(response.json())
response_dict = response.json()

# JSON FILE HAS NESTED DICTIONARY 'results'
response_results = response_dict['result']

# ITERATE THROUGH NESTED DICT 'results'
for key, value in response_results.items():
    print(f'{key}: {value}')

