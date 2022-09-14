from pprint import pprint

def dish_dict():
    with open("recipe.txt", encoding="utf-8") as file:
        cook_book = {}
        for line in file:
            dish = line.strip()
            quantity = file.readline().strip()
            recipe = []
            for line in range(int(quantity)):
                text = file.readline().split(" | ")
                recipe.append({'ingredient_name': text[0], 'quantity': text[1],
                'measure': text[2].strip()})
            cook_book[dish] = recipe
            file.readline()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    to_buy = {}
    book = dish_dict()
    for dish in dishes:
        ingredients = book.get(dish)
        if ingredients:
            for ingredient in ingredients:
                ingredient_name, quantity, measure = (ingredient['ingredient_name'],
                                                      ingredient['quantity'],
                                                      ingredient['measure'])
                ingredients_to_buy = to_buy.get(ingredient_name, {})
                ingredients_to_buy['measure'] = measure
                ingredients_to_buy['quantity'] = ingredients_to_buy.get('quantity', 0) + int(quantity) * person_count
                to_buy[ingredient_name] = ingredients_to_buy
    return to_buy



print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))