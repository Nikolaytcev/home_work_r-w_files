# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 15:30:08 2022

@author: LocalAdmin
"""

def cook_book(file):
    cook_book = {}
    dishes = []
    with open(file, 'r', encoding="utf-8") as file:
        for line in file:
            if ' |' not in line.strip() and line.strip().isdigit() == False and line != '\n':
                l = line.strip()
                dishes.append(l)
                cook_book[l] = []
            elif ' |' in line.strip():
                cook_book[l] += [{'ingredient_name': line.strip().split(' | ')[0],
                                  'quantity': int(line.strip().split(' | ')[1]),
                                  'measure': line.strip().split(' | ')[2]}]
    return cook_book, dishes

def get_shop_list_by_dishes(dishes, person_coun):
    ingredients = {}
    for i in dishes:
        for j in cook_book.get(i):
            if j.get('ingredient_name') not in ingredients:
                ingredients[j.get('ingredient_name')] = {'quantity': j.get('quantity') * person_coun,
                    'measure': j.get('measure')}
            else:
                new_quantity = ingredients.get(j.get('ingredient_name')).get('quantity') + j.get('quantity') * person_coun
                ingredients[j.get('ingredient_name')] = {'quantity': new_quantity,
                    'measure': j.get('measure')}
    return ingredients
        
    
cook_book, dishes = cook_book('recipes.txt')
ingredients = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print(cook_book)
print(ingredients)