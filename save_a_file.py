import requests

# ask the user to enter an ingredient that they want to search for
ingredient = input("Which ingredient would like to search please enter it:")

# create url with api_key and api_id
ingredient_url = 'https://api.edamam.com/search?q={}&app_id=cb30915d&app_key=5d7addd9e73ab26dba52a5f49ce33d9c'.format(ingredient)

response = requests.get(ingredient_url)
ingredients = response.json()
# This code takes the data according to the content entered by the user and prints the name and calories of the recipes belonging to that
# content to the file and reads them from that file and prints them to the screen.

for s in ingredients['hits']:
    # print('Recipe Label: ' + s['recipe']['label'] + " -- " + 'Recipe Calories: ' + str(s['recipe']['calories']))
    # write to 'recipe_calories.txt file
    with open('recipe_calories.txt', 'a+', encoding="utf-8") as recipe_calories:
        recipe_calories.write(str('Recipe Label: ' + s['recipe']['label'] + " -- " + 'Recipe Calories: ' + str(s['recipe']['calories']) + "\n"))
print("Write to file has been completed, please check the file named ingredient_file.")

# read recipe_calories.txt file
with open('recipe_calories.txt', 'r', encoding="utf-8") as recipe_calories:
    read_file = recipe_calories.read()
print(read_file)
