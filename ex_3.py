def read_files(file_names):
    files_data = []

    for file_name in file_names:
        # Откроем файл только на чтение
        with open(file_name, 'r', encoding='utf-8') as file:
            # Получим список всех строк файла
            lines = file.readlines()

        # Сохраняем имя, кол-во строк и содержимое вместе
        files_data.append({
            'file_name': file_name,
            'line_count': len(lines),
            'lines': lines,
        })
    return files_data

def merge_files(files_data, result_path):
    # Сортировка от меньшего к большему
    sorted_files = sorted(
        files_data,
        key=lambda file_data: file_data['line_count'],
    )

    with open(result_path, 'w', encoding='utf-8') as result:
        for file_data in sorted_files:
            # Добавляем две служебные строчки
            result.write(f'{file_data['file_name']}\n')
            result.write(f'{file_data['line_count']}\n')

            # Запишем строки исходные
            result.writelines(file_data['lines'])

            # Если последняя строка не имела переноса, добавим его
            if file_data['lines']:
                if not file_data['lines'][-1].endswith('\n'):
                    result.write('\n')
            
def main():
    files_data = read_files(['1.txt', '2.txt', '3.txt'])     # По условию, заранее знаем название файлов 
    merge_files(files_data, 'result.txt')
    print('Результат работы программы записан в result.txt')

main()