cook_book = {}

def create_dict_from_file(file_name):
  with open(file_name, encoding = 'utf8') as book:
    for dish in book:
      dish = book.readline().lower().strip()
      num = book.readline().strip()
      ingridient_list = []
      cook_book.setdefault(dish, ingridient_list)
      for ingridient in range(int(num)):
        ingridient = book.readline().lower().strip().split(' | ')
        ingridient = {'ingredient_name' : ingridient[0], 'quantity' : ingridient[1], 'measure' : ingridient[2]}
        ingridient_list.append(ingridient)

create_dict_from_file('recipes.txt')
print(cook_book)
