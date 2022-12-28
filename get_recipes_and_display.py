import requests
from pprint import pprint

# ask the user to enter an ingredient that they want to search for
ingredient = input("Which ingredient would like to search please enter it:")

# create url with api_key and api_id
ingredient_url = 'https://api.edamam.com/search?q={}&app_id=cb30915d&app_key=5d7addd9e73ab26dba52a5f49ce33d9c'.format(ingredient)

response = requests.get(ingredient_url)
ingredients = response.json()
# how many recipe are there with that ingredient
print('There are {} recipes about {}'.format(len(ingredients), ingredient))
# I'm getting all recipes with that ingredient
for s in ingredients['hits']:
    pprint(s['recipe'])
