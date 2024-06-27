import csv


def read_file(filename: str) -> list[dict]:
    """Читает данные из CSV файла и преобразует их в список словарей.

    :param filename: Название файла, содержащего данные.
    :return: Список словарей с данными о домах.
    """

    my_file = open(filename, 'r', encoding='utf-8')
    reader = csv.DictReader(my_file)
    my_list_ = list(reader)
#   print("Dictionary after typecasting:")
    for i in my_list_:
        #    print(i)
        for key, value in i.items():
            if key == 'floor_count':
                i[key] = int(value)
            if key == 'heating_value':
                i[key] = float(value)
            if key == 'area_residential':
                i[key] = float(value)
            if key == 'population':
                i[key] = int(value)
#            print(f"{key}, {value}, {type(i[key])}")
    return my_list_


def classify_house(floor_count: int) -> str:
    """Классифицирует дом на основе количества этажей.

    Проверяет, является ли количество этажей целым числом и положительным значением.
    Возвращает категорию дома в зависимости от количества этажей.

    :param floor_count: Количество этажей в доме.
    :return: Категория дома в виде строки: "Малоэтажный", "Среднеэтажный" или "Многоэтажный".
    """
    if not isinstance(floor_count, int):
        raise TypeError('not a number')
    if floor_count <= 0:
        raise ValueError('positive number expected')
    if floor_count <= 5:
        return 'Малоэтажный'
    else:
        if floor_count <=16:
            return 'Среднеэтажный'
        else:
            return 'Многоэтажный'


def get_classify_houses(houses: list[dict]) -> list[str]:
    """Классифицирует дома на основе количества этажей.

    :param houses: Список словарей с данными о домах.
    :return: Список категорий домов.
    """
    categories = []
    for i in houses:
        #    print(i)
        for key, value in i.items():
            if key == 'floor_count':
                cat = classify_house(value)
                categories.append(cat)
    return categories


def get_count_house_categories(categories: list[str]) -> dict[str, int]:
    """
    Подсчитывает количество домов в каждой категории.

    :param categories: Список категорий домов.
    :return: Словарь с количеством домов в каждой категории.
    """
    category_count = {}
    for cat in categories:
        if cat in category_count:
            category_count[cat] += 1
        else:
            category_count[cat] = 1

    return category_count

def min_area_residential(houses: list[dict]) -> str:
    """Находит адрес дома с наименьшим средним количеством квадратных метров жилой площади на одного жильца.

    :param houses: Список словарей с данными о домах.
    :return: Адрес дома с наименьшим средним количеством квадратных метров жилой площади на одного жильца.
    """
    min_area = houses[0]['area_residential'] / houses[0]['population']
    address = houses[0]['house_address']
    for i in houses:
        if i['area_residential']/i['population'] < min_area:
            min_area = i['area_residential']/i['population']
            address = i['house_address']
    return address


if __name__ == "__main__":
    my_list = read_file('housing_data.csv')
    categories_ = get_classify_houses(my_list)
    my_dict_ = get_count_house_categories(categories_)
    print(my_dict_)
    address_ = min_area_residential(my_list)
    print(address_)
