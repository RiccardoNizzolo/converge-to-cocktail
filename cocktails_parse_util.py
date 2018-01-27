import re
from fractions import Fraction

ingredient_parts_re = re.compile(r"([\d \/]*) (.*)")


""" usage:

    import cocktails_parse_util as cp
    print(cp.get_ingredients("rum:1 1/2 ounces,lime juice:3/4 ounce,grenadine:2 dashes,"))
    > [('rum', 42.524249999999995), ('lime juice', 21.262124999999997), ('grenadine', 1.25)]
    print(cp.get_ingredientsline_grams("rum:1 1/2 ounces,lime juice:3/4 ounce,grenadine:2 dashes,"))
    > rum:42.524249999999995,lime juice:21.262124999999997,grenadine:1.25
"""
def get_grams(amount, unit):
    """ returns the weight in grams (water density assumed) """
    return {
      'ounce': lambda x: x * 28.3495,
      'ounces': lambda x: x * 28.3495,
      'dash': lambda x: x * 5 / 8, # 1/8 teaspoon
      'dashes': lambda x: x * 5 / 8, # 1/8 teaspoon
      'tablespoons': lambda x: x * 15, # 1 tablespoon = 3 teaspoons
      'pinch': lambda x: x * 0.25,
      'cup': lambda x: x * 0.25, # 1 cup is 0.25l
      'cups': lambda x: x * 0.25, # 1 cup is 0.25l
      'teaspoons': lambda x: x * 5, # 5gr
      'whole': lambda x: x, # can't do much here
      'teaspoon': lambda x: x * 5, # 5gr
      'pint': lambda x: x * 0.568, # 1 british pint is 0.568 liters
      'tablespoon': lambda x: x * 15 # 1 tablespoon = 3 teaspoons
    }[unit](amount)

def get_decimal(fraction_str):
    number = float(0)
    for num in fraction_str.split(" "):
        number = number + float(Fraction(num))
    return number

def get_ingredients(line):
    # split ',' to get each ingredient separated
    ingredients = []
    for ingredient_str in line.split(","):
        if len(ingredient_str.split(":")) > 0 and len(ingredient_str)>0:
            # ingredient name always left to ':'
            ingr_name = ingredient_str.split(":")[0]
            
            ingr_right_part = ingredient_str.split(":")[1]
            match = ingredient_parts_re.match(ingr_right_part)
            amount = get_decimal(match.groups()[0])
            unit = match.groups()[1]
            amount = get_grams(amount,unit)
            ingredients.append((ingr_name, amount))
    return ingredients

def get_ingredientsline_grams(line):
    ingredients = get_ingredients(line)
    return ','.join([ingr_name + ':' + str(ingr_amount) for ingr_name, ingr_amount in ingredients])

