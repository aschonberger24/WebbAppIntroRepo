from ClassApp.models import Recipe
from NewApp.settings import BASE_DIR, DATA_ADDED


def import_from_menu():
    import csv
    # with open('/Users/Avery/Desktop/S2-Spring_2023/Webb_Apps_Programming/NewApp/static/ClassApp/dataframe_upload.csv',
    with open(str(BASE_DIR)+'/static/ClassApp/dataframe_upload.csv', 'r') as csvfile:
        #/Users/tanmayebhatia/Desktop/Columbia/Web_App_programming_S2023/Pycharm_Projects/WebbAppIntroRepo
        reader = csv.reader(csvfile)
        all_recipes = []
        # this_recipe = Recipe()
        for row in reader:
            this_recipe = Recipe(id_num=row[0], title=row[1], ingredients=';;'.join(row[2].split("', '")),
                                 instructions=row[3], image=row[4])
            this_recipe.ingredients = this_recipe.ingredients.replace("['", '')
            this_recipe.ingredients = this_recipe.ingredients.replace("']", '')
            all_recipes.append(this_recipe)
        print(this_recipe)
        # to save to database: this_recipe.save()
    #to save entire list to database:
    if DATA_ADDED == "FALSE":
        for i in all_recipes[1:12000]:
            i.save()
    return all_recipes[5:]


def get_recipe_options(input_ingredients, all_recipes):
    user_ingredients = input_ingredients.lower().split(', ')
    exempt_ingredients = get_exempt_ingredients()
    recipe_list = list()
    
    
    # suggested_list = list()
    for one_recipe in all_recipes:                          # "one_recipe" is each recipe
        ingredient_list = one_recipe.ingredients.lower().split(';;')  # split the ingredients string at ;;
        ingredient_score = 0                                # initialize ingredient score
        registered_ingredients = []                         # initialize list of registered ingredients
        for one_ingredient in ingredient_list:              # iterate through all ingredients in the recipe
            appended_flag = 0                               # lower the appended flag

            # DETERMINE IF USER HAS ALL THE INGREDIENTS FOR A RECIPE
            for user_ingredient in user_ingredients:
                # parts = user_ingredient.split()             # separate user ingredients into words
                # real_ingredient = parts[len(parts) - 1]     # ingredient name is last part of user ingredient

                if user_ingredient in one_ingredient:       # if the user ingredient is a recipe ingredient
                    ingredient_score += 1                   # increment the ingredient score
                    registered_ingredients.append(user_ingredient)  # add the ingredient to registered ingredients list
                    appended_flag = 1                       # raise the appended flag if the ingredient is there
                    # print(user_ingredient)

            if appended_flag == 0:                          # if appended flag is lowered, ingredient is not available
                raw_ingredient = one_ingredient.split()  # raw_ingredient is split name of the needed ingredient
                if len(raw_ingredient) != 0:
                    # print(';' + raw_ingredient[len(raw_ingredient) - 1] + ';')
                    for i in raw_ingredient:
                        if i in exempt_ingredients:
                            ingredient_score += 1
                            # print(i)
                    # if raw_ingredient[len(raw_ingredient) - 1] in exempt_ingredients:  # if the ingredient is exempt
                        # ingredient_score += 1                   # increment the ingredient score

        # CHECK THAT USER HAS INGREDIENTS
        if ingredient_score == len(ingredient_list):  # if the ingredient score is the number of ingredients
            recipe_list.append(one_recipe)  # add the recipe to the list of approved recipes
    print("THIS IS THE COUNT "+str(len(recipe_list)))

    return recipe_list


def get_exempt_ingredients():
    exempt_ingredients_list = ['salt', 'pepper', 'spray', 'basil', 'oil', 'butter', 'vinegar', 'sugar', 'flour',
                               'garlic']
    return exempt_ingredients_list

"""
from ClassApp.models import Currency

def get_currency_list():
    currency_list = list()
    import requests
    from bs4 import BeautifulSoup
    url = "https://thefactfile.org/countries-currencies-symbols/"
    response = requests.get(url)
    if not response.status_code == 200:
        return currency_list
    soup = BeautifulSoup(response.content)
    data_lines = soup.find_all('tr')
    for line in data_lines:
        try:
            detail = line.find_all('td')
            currency = detail[2].get_text().strip()
            iso = detail[3].get_text().strip()
            if (currency,iso) in currency_list:
                continue
            currency_list.append((currency,iso))
        except:
            continue
    return currency_list

def add_currencies(currency_list):
    for currency in currency_list:
        currency_name = currency[0]
        currency_symbol = currency[1]
        try:
            c = Currency.objects.get(iso=currency_symbol)
        except:
            c = Currency(long_name=currency_name, iso=currency_symbol)
            c.name = currency_name
            print(c) #c.save()  #To test out the code, replace this by print(c)
    return"""


