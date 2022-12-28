import requests
from PIL import Image
import urllib.request

# Find_recipe function first creating url with api_key and api_id. I’m getting data in json format and this function returning ‘hits’ in data.
# All recipe is in ‘hits’.


def find_recipe(ingredient):
    app_id = 'cb30915d'
    app_key = '5d7addd9e73ab26dba52a5f49ce33d9c'
    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key)
                          )
    data = result.json()
    return data['hits']

# this function shorting recipes to weight


def sort_weight():
    ingredient = input('Which ingredient would like to search please enter it:')
    # I call the function with whatever data the user has entered
    results = find_recipe(ingredient)
    # I need a list because there is more than one data, for this I create a new list.
    recipe_weight = []
    for weight in results:
        recipe_weight.append(weight['recipe']['totalWeight'])

    print(recipe_weight)
    print(sorted(recipe_weight))
    print(list(reversed(sorted(recipe_weight))))


#sort_weight()

# this function ask the user a lot of ingredient and calculate to calories.This function works as long as the user wants to enter data
# If the user does not write the recipe names correctly, it tells the user


def calculate_calories():
    answer = 'yes'
    calories = 0
    while answer == 'yes':
        recipe_calories = {}
        ingredient = input('Which ingredient would like to search please enter it:')
        results = find_recipe(ingredient)

        for meal in results:
            print('Recipe Label: ' + str(meal['recipe']['label']) + ' ----- ' +
                  'Recipe Calories: ' + str(meal['recipe']['calories']))
            recipe_calories[meal['recipe']['label']] = meal['recipe']['calories']
        choose_recipe = input('Which recipe would like choose please write recipe name:')

        if choose_recipe in recipe_calories:
            calorie = recipe_calories[choose_recipe]
            calories = calories + calorie
        else:
            print("You didn't write correctly.")

        answer = input('Do you want to add other recipe calories? : yes or no')
    print("Total Calories : " + str(calories))


#calculate_calories()

# this function ask the user some questions and fetches data according to user's requests
# this function is interesting piece of code in my project


def find_best_recipes():
    ingredient = input('Which ingredient would like to search please enter it:')
    dish_type = input('Which dish type are you looking for?')
    meal_type = input('Which meal type are you looking for?')
    cuisine_type = input('Which cuisine type are you looking for?')

    results = find_recipe(ingredient)

    count = 0

    for result in results:
        data = {
            'Recipe_Label': str(result['recipe']['label']),
            'Dish_Type': str(result['recipe']['dishType'][0]),
            'Meal_Type': str(result['recipe']['mealType'][0]),
            'Cuisine_Type': str(result['recipe']['cuisineType'][0]),
            'Recipe_Image': str(result['recipe']['image'])
        }

        if dish_type in data['Dish_Type'] and meal_type in data['Meal_Type'] and cuisine_type in data['Cuisine_Type']:
            print("Recipe Name : "+data['Recipe_Label'])
            urllib.request.urlretrieve(data['Recipe_Image'], 'abc.png')
            img = Image.open('abc.png')
            input("Please press enter to see the recipe's picture.")
            img.show()
            count = count + 1

    if count == 0:
        print("There isn't recipe")


find_best_recipes()
