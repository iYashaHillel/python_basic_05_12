import requests
import functools

API_KEY = '783c9a2e93f249c5ae9cd977dad46b7c'


@functools.lru_cache()
def get_recipes(ingredients: str, limit: int = 10):
    url = 'https://api.spoonacular.com/recipes/findByIngredients'
    params = {
        'ingredients': ingredients,
        'number': limit,
        'apiKey': API_KEY,
    }
    resp = requests.get(url, params=params)
    if not 200 <= resp.status_code <= 299:
        print(f'Error: {resp.content}')

    output = ''
    for recipe in resp.json():
        output += f'Name: {recipe["title"]}\n'
        missed_ingredients = '\n'.join([x['name'] for x in recipe['missedIngredients']])
        output += f'Missed ingredients:\n{missed_ingredients}\n\n'
    return output


ingredients = input('Enter ingredients (e.g. apples,flour,sugar): ')
print(get_recipes(ingredients))
print(get_recipes(ingredients))
print(get_recipes(ingredients))
