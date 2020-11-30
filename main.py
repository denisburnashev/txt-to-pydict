cook_book = {}

with open('recipes.txt') as book:
    for dish in range(1):
        dish = book.readline().strip()

    for num in range(1):
        num = book.readline().strip()
        ingridient_list = []
        cook_book.setdefault(dish, ingridient_list)
        for ingridient in range(int(num)):
            ingridient = book.readline().strip().split(' | ')
            ingridient = {'ingredient_name': ingridient[0], 'quantity': ingridient[1], 'measure': ingridient[2]}
            ingridient_list.append(ingridient)

    for dish in range(2):
        dish = book.readline().strip()

    for num in range(1):
        num = book.readline().strip()
        ingridient_list = []
        cook_book.setdefault(dish, ingridient_list)
        for ingridient in range(int(num)):
            ingridient = book.readline().strip().split(' | ')
            ingridient = {'ingredient_name': ingridient[0], 'quantity': ingridient[1], 'measure': ingridient[2]}
            ingridient_list.append(ingridient)

    for dish in range(2):
        dish = book.readline().strip()

    for num in range(1):
        num = book.readline().strip()
        ingridient_list = []
        cook_book.setdefault(dish, ingridient_list)
        for ingridient in range(int(num)):
            ingridient = book.readline().strip().split(' | ')
            ingridient = {'ingredient_name': ingridient[0], 'quantity': ingridient[1], 'measure': ingridient[2]}
            ingridient_list.append(ingridient)

    for dish in range(2):
        dish = book.readline().strip()

    for num in range(1):
        num = book.readline().strip()
        ingridient_list = []
        cook_book.setdefault(dish, ingridient_list)
        for ingridient in range(int(num)):
            ingridient = book.readline().strip().split(' | ')
            ingridient = {'ingredient_name': ingridient[0], 'quantity': ingridient[1], 'measure': ingridient[2]}
            ingridient_list.append(ingridient)

print(cook_book)
