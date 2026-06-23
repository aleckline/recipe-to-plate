# Recipe data
aglio = {
	'pasta': {'qty': 113, 'unit':'grams'},
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
	'pasta': {'qty': 113, 'unit':'grams'},
	'ground turkey': {'qty': 5, 'unit':'oz'},
	'bacon': {'qty': 10, 'unit':'grams'},
	'carrots': {'qty': 10, 'unit':'grams'},
	'celery': {'qty': 10, 'unit':'grams'},
	'onion': {'qty': 10, 'unit':'grams'},
	'milk': {'qty': 1, 'unit':'oz'},
	'white wine': {'qty': 1, 'unit':'oz'},
	'pepper': {'qty': 0.4, 'unit':'tsp'},
	'tomato sauce': {'qty': 8, 'unit':'oz'},
	}

cookies = {
	'flour': {'qty': 285, 'unit': 'grams', 'price': 0.92},
	'corn starch': {'qty': 20, 'unit': 'grams', 'price': 0.12},
	'salt': {'qty': 1, 'unit': 'tsp', 'price': 0.04},
	'baking soda': {'qty': 1, 'unit': 'tsp', 'price': 0.01},
	'butter': {'qty': 6, 'unit': 'oz', 'price': 3.06},
	'brown sugar': {'qty': 200, 'unit': 'grams', 'price': 0.88},
	'granulated sugar': {'qty': 100, 'unit': 'grams', 'price': 0.47},
	'eggs': {'qty': 2, 'unit': 'ea', 'price': 0.68},
	'vanilla': {'qty': 2, 'unit': 'tsp', 'price': 1.50},
	'chocolate chips': {'qty': 2, 'unit': 'oz', 'price': 1.40},
	}

queso_blanco = {
	'whole milk': {'qty': 16, 'unit': 'oz'},
	'yellow onion': {'qty': 30, 'unit': 'grams'},
	'serrano pepper': {'qty': 15, 'unit': 'grams'},
	'poblano pepper': {'qty': 20, 'unit': 'grams'},
	'chipotle pepper in adobo': {'qty': 5, 'unit': 'grams'},
	'garlic': {'qty': 3, 'unit': 'grams'},
	'cornstarch': {'qty': 24, 'unit': 'grams'},
	'water': {'qty': 15, 'unit': 'grams'},
	'sour cream': {'qty': 8, 'unit': 'oz'},
	'monterey jack cheese': {'qty': 8, 'unit': 'oz'},
	'sharp white cheddar': {'qty': 4, 'unit': 'oz'},
	'tomato': {'qty': 10, 'unit': 'grams'},
	'salt': {'qty': 3, 'unit': 'grams'}
	}

black_beans = {
	'black beans': {'qty': 6, 'unit': '15 oz cans'},
	'olive oil': {'qty': 2, 'unit': 'tbsp'},
	'onion': {'qty': 1, 'unit': 'ea'},
	'garlic': {'qty': 30, 'unit': 'grams'},
	'cumin': {'qty': 2, 'unit': 'tsp'},
	'dried oregano': {'qty': 1.5, 'unit': 'tsp'},
	'bay leaves': {'qty': 2, 'unit': 'ea'},
	'salt': {'qty': 1.5, 'unit': 'tsp'},
	'adobo sauce': {'qty': 1, 'unit': 'tbsp'},
	'lime juice': {'qty': 3, 'unit': 'ea'},
	}

breakfast_burritos = {
	'eggs': {'qty': 2, 'unit':'ea'},
	'egg whites': {'qty': 50, 'unit':'g'},
	'sausage': {'qty': 1, 'unit':'ea'},
	'cheese': {'qty': 18, 'unit':'grams'},
	'onion': {'qty': 20, 'unit':'g'},
	'torilla': {'qty': 1, 'unit':'ea'},
	}

pizza = {
	'flour': {'qty': 92, 'unit':'g'},
	'salt': {'qty': 2.1, 'unit':'g'},
	'instant yeast': {'qty': .5, 'unit':'g'},
	'olive oil': {'qty': 9.5, 'unit':'grams'},
	'water': {'qty': 68.5, 'unit':'g'},
	'tomato sauce': {'qty': 2, 'unit':'oz'},
	'mozzarella': {'qty': 2, 'unit':'oz'},
	'basil': {'qty': 3, 'unit':'ea'},
	}


# Nutrition data
class Nutrition():
	"""Nutrition information"""
	
	def __init__(self, calories, carbs, fat, protein):
		"""Initialize nutrition attributes"""
		self.calories = calories
		self.carbs = carbs
		self.fat = fat
		self.protein = protein
		
aglio_nutrition = Nutrition(675, 87, 17, 43)
ragu_nutrition = Nutrition(836, 101, 26, 43)


# Calculate price
def get_price(recipe_name):
	"""Calculate recipe price"""
	recipe_price = 0
	for info in recipe_name.values():
		recipe_price = recipe_price + info['price']
	return recipe_price


# Display the recipe book
recipe_book = {
	'aglio': aglio, 'ragu': ragu, 'cookies': cookies, 
	'queso blanco': queso_blanco, 'black beans': black_beans,
	'breakfast burritos': breakfast_burritos, 'pizza': pizza}
	
menu = []
for recipe in recipe_book.keys():
	menu.append(recipe.title())
print('Menu: ')
print(str(menu) + '\n')


# Receive the meal plan
meal_plan = {}
gathering_info = True
while gathering_info:
	recipe = input('What recipe are we cooking? ')
	recipe_qty = input('How many meals of ' + recipe + '? ')
	meal_plan[recipe] = recipe_qty
	another = input('Are we adding another recipe? (yes/no) ')
	print('\n')
	if another == 'no':
		gathering_info = False


# Print the meal plan
print('Meal plan: ')
for meal, qty in meal_plan.items():
	print(meal.title() + ': ' + str(qty))


# Create the shopping list
print('\nShopping list:')
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

print('\n')


# Recipe instructions
class Instructions:
	
	def __init__(self, step_1, step_2, step_3, step_4, step_5, step_6):
		"""Initialize nutrition attributes"""
		self.step_1 = step_1
		self.step_2 = step_2
		self.step_3 = step_3
		self.step_4 = step_4
		self.step_5 = step_5
		self.step_6 = step_6
	
	def print_instructions(self):
		print(self.step_1)
		print(self.step_2)
		print(self.step_3)
		print(self.step_4)
		print(self.step_5)
		print(self.step_6)


ragu_instructions = Instructions(
	'Fry bacon, then veggies', 
	'Add meat, and once brown, add wine',
	'Add tomato sauce, simmer for 2 hours, then add milk',
	'Salt and pepper to taste',
	'no step 5',
	'no step 6'
	)

cookies_instructions = Instructions(
	'Melt butter', 
	'Combine flour, corn starch, salt, and baking soda',
	'Separately combine the melted butter and brown and white sugar,',
	'Add eggs and vanilla to wet ingredients',
	'Combine all ingredients and add chocolate chips',
	'Refrigerate, then cook at 350F for 12 minutes. Add salt'
	)

queso_blanco_instructions = Instructions(
	'Simmer milk, onion, ',
	'peppers, and garlic for 5 minutes', 
	'Add corn starch and water, and cook until thickened',
	'Lower heat, add sour cream, and cheeses gradually',
	'Add tomato and salt to taste',
	'no step 6',
	)

black_beans_instructions = Instructions(
	'Heat oil over medium heat',
	'Add onion with salt, then garlic',
	'Add cumin, dried oregano, black pepper, and bay leaves',
	'Add 3 cans of drained beans and 3 full cans',
	'Add adobo sauce, simmer for 20 minutes, mash beans to thicken',
	'finish with lime juice and salt'
	)
