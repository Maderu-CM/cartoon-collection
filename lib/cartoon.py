def roll_call_dwarves(dwarf_names):
    for i, name in enumerate(dwarf_names, start=1):
        print(f"{i}. {name}")

#test
dwarf_names = ["Doc", "Dopey", "Bashful", "Grumpy"]
roll_call_dwarves(dwarf_names)

def summon_captain_planet(planeteer_calls):
    return [call.capitalize() + '!' for call in planeteer_calls]

#test
planeteer_calls = ["earth", "wind", "fire", "water", "heart"]
captain_planet_calls = summon_captain_planet(planeteer_calls)
print(captain_planet_calls)


def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

# test
short_words = ["puff", "go", "two"]
result_short = long_planeteer_calls(short_words)
print(result_short)  

assorted_words = ["two", "go", "industrious", "bop"]
result_assorted = long_planeteer_calls(assorted_words)
print(result_assorted)  

def find_the_cheese(ingredients):
    cheese_types = ["cheddar", "gouda", "camembert"]
    
    for ingredient in ingredients:
        if ingredient in cheese_types:
            return ingredient
    
    return None

# test
snacks = ["crackers", "gouda", "thyme"]
result_snacks = find_the_cheese(snacks)
print(result_snacks) 

soup = ["tomato soup", "cheddar", "oyster crackers", "gouda"]
result_soup = find_the_cheese(soup)
print(result_soup) 

ingredients = ["garlic", "rosemary", "bread"]
result_ingredients = find_the_cheese(ingredients)
print(result_ingredients) 


