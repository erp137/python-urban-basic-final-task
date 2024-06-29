import csv


def read_file(filename: str) -> list[dict]:
    """Читает данные из CSV файла и преобразует их в список словарей.

    :param filename: Название файла, содержащего данные.
    :return: Список словарей с данными о домах.
    """

    with open(filename, encoding='utf-8') as my_file:
        reader = csv.DictReader(my_file)
        my_houses = list(reader)
        for house in my_houses:
            house['floor_count'] = int(house['floor_count'])
            house['heating_value'] = float(house['heating_value'])
            house['area_residential'] = float(house['area_residential'])
            house['population'] = int(house['population'])
    return my_houses


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
        return "Малоэтажный"
    elif floor_count <= 16:
        return "Среднеэтажный"
    else:
        return "Многоэтажный"


def get_classify_houses(houses: list[dict]) -> list[str]:
    """Классифицирует дома на основе количества этажей.

    :param houses: Список словарей с данными о домах.
    :return: Список категорий домов.
    """
    return [classify_house(house['floor_count']) for house in houses]


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
    for house in houses:
        if house['area_residential']/house['population'] < min_area:
            min_area = house['area_residential']/house['population']
            address = house['house_address']
    return address


if __name__ == "__main__":
    my_list = read_file('housing_data.csv')
    categories_ = get_classify_houses(my_list)
    my_dict_ = get_count_house_categories(categories_)
    print(my_dict_)
    address_ = min_area_residential(my_list)
    print(address_)
