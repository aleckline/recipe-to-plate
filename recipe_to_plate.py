# Recipe data
aglio = {
	'pasta': {'qty': 90, 'unit':'grams'},
	'olive oil': {'qty': 8, 'unit':'grams'},
	'garlic': {'qty': 10, 'unit':'grams'},
	'red pepper': {'qty': 0.2, 'unit':'tsp'},
	'chicken': {'qty': 5, 'unit':'oz'},
	'lemon': {'qty': 0.4, 'unit':'ea'},
	'pepper': {'qty': 0.4, 'unit':'tsp'},
	'burrata': {'qty': 11, 'unit':'grams'},
	'parsely': {'qty': 0.1, 'unit':'bunch'}
					}
ragu = {
	'pasta': {'qty': 90, 'unit':'grams'},
	'ground turkey': {'qty': 5, 'unit':'oz'},
	'bacon': {'qty': 10, 'unit':'grams'},
	'tomato sauce': {'qty': 8, 'unit':'oz'},
					}

recipe_book = {'aglio': aglio, 'ragu': ragu}
menu = []
for recipe in recipe_book.keys():
	menu.append(recipe.title())
print('Menu: ')
print(str(menu) + '\n')

# Receive the meal plan
meal_plan = {}
gathering_info = True
while gathering_info:
	recipe = input('What recipe are we calculating? ')
	recipe_qty = input('How many meals of ' + recipe + '? ')
	meal_plan[recipe] = recipe_qty
	another = input('Are we adding another recipe? (yes/no) ')
	print('\n')
	if another == 'no':
		gathering_info = False

print('Meal plan: ')
for meal, qty in meal_plan.items():
	print(meal.title() + ': ' + str(qty))

print('\nShopping list:')
# Create the shopping list
shopping_list = {}
for req_recipe, req_qty in meal_plan.items():
	if req_recipe in recipe_book:
		recipe_data = recipe_book[req_recipe]
		for ingredient, info in recipe_data.items():
			ingredient_quantity = round(float(info['qty'])*int(req_qty), 2)
			total_unit = f"{ingredient_quantity} {info['unit']}"
			shopping_list[ingredient] = total_unit
	else:
		print(req_recipe + ' N/A')


# Print a formmated shopping list
for key, value in shopping_list.items():
	print(key.capitalize() + ': ' + str(value))
