import requests
from pprint import pprint

# greeting to user
print("Welcome to Edamam Search Project!")

# ask the user to enter an ingredient that they want to search for
ingredient = input("Which ingredient would like to search please enter it:")

# create url with api_key and api_id
ingredient_url = 'https://elif.com/search?q={}&app_id=cb30915d&app_key=5d7addd9e73ab26dba52a5f49ce33d9c'.format(ingredient) 
# I'm sending request to url
response = requests.get(ingredient_url)

# check credential
if response.status_code == 200:
    print('Your credentials have been verified')

# if your credentials have been verified, I'm getting data from api in json
    ingredients = response.json()
    # If the ingredient I am looking for is not in the response from Api
    if ingredients['count'] == 0:
        print("We are sorry we don't have {}".format(ingredient))
    # If the ingredient I am looking for is in the response from Api
    else:
        print("We have this {}".format(ingredient))
        pprint(ingredients)
# if your credentials haven't been correct
elif response.status_code == 401:
    print('Your credentials have not been verified. Please check your credentials.')

else:
    print('There is something wrong.')
