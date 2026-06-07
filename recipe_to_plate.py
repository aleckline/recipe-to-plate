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

# Receive the meal plan
message = input('What are you eating this week? ')
meals = input('How many meals are you eating this week? ')


# Create the shopping list
shopping_list = {}
for ingredient, info in aglio.items():
	ingredient_quantity = round(float(info['qty'])*int(meals), 2)
	total_unit = f"{ingredient_quantity} {info['unit']}"
	shopping_list[ingredient] = total_unit


# Print a formmated shopping list
for key, value in shopping_list.items():
	print(key.capitalize() + ': ' + str(value))
