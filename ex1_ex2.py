from pprint import pprint
# Читаем рецепты из файла и возвращаем словарь блюд
def read_cook_book(file_path):
    cook_book = {}

    # Файл автоматически закроется после выхода из блока with
    with open(file_path, 'r', encoding='utf-8') as file:
        # Читаем очередную строку с названием блюда
        for line in file:
            dish_name = line.strip()

            # Пропускаем пустые строки между рецептами
            if not dish_name:
                continue
        
            ingredient_count = int(file.readline().strip())     # В строке количество ингредиентов
            ingredients = []                                    # Спиок ингередиентов для каждого блюда

            # Читаем ровно столько строк, сколько указано ингредиентов
            for _ in range(ingredient_count):
                # Название ингредиента, кол-во, шт/мл 
                ingredient_name, quantity, measure = file.readline().strip().split('|')
                
                # Собираем ингредиетны в список, записываем его под название блюда
                ingredient = {
                    'ingredient_name': ingredient_name.strip(),
                    'quantity': int(quantity),
                    'measure': measure.strip(),
                }
                ingredients.append(ingredient)      # Добавляем словарь одного ингередиента в список
            
            cook_book[dish_name] = ingredients      # Сохраняем словарь под названием блюда
    return cook_book

def get_shop_list_by_dishes(dishes, person, cook_book):
    shop_list = {}          # Общий словарь покупок для всех выбранных блюд

    for dish_name in dishes:
        # Получаем список ингередиентов блюда
        for ingredient in cook_book[dish_name]:
            ingredient_name = ingredient['ingredient_name']
            quantity = ingredient['quantity'] * person
            measure = ingredient['measure']

            # Повторяющийся ингередиент добавляем к уже накопившемуся кол-ву
            if ingredient_name in shop_list:
                shop_list[ingredient_name]['quantity'] += quantity
            else:
                # Если такого не было, то запишем этот ингредиент
                shop_list[ingredient_name] ={
                    'measure': measure,
                    'quantity': quantity,
                }

    return shop_list
  
def main():
    cook_book = read_cook_book('recipes.txt')
    shop_list = get_shop_list_by_dishes(
        ['Запеченный картофель', 'Омлет'],
        2,
        cook_book,
    )

    pprint(shop_list, sort_dicts=False, width=120)

main()