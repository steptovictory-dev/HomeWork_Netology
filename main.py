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

def main():
    cook_book = read_cook_book('recipes.txt')
    # print(cook_book)
    pprint(cook_book, sort_dicts=False, width=120)

main()