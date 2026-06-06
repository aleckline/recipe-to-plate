aglio = {
	'pasta, g': '90',
	'olive oil, g':'8',
	'garlic, g':'10',
	'red pepper, tsp':'.2',
	'chicken, oz': '5',
	'lemon, ea':'.4',
	'pepper, tsp':'.4',
	'burrata, g': '11',
	'parsely, bunch':'0.1',
					}


message = input('What are you eating this week? ')
meals = input('How many meals are you eating this week? ')

shopping_list = {}
for ingredient, quantity in aglio.items():
	ingredient_total = float(quantity)*int(meals)
	shopping_list[ingredient] = ingredient_total
for key, value in shopping_list.items():
	print(key.capitalize() + ': ' + str(value))
