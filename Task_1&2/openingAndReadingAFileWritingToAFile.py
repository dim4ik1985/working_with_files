from pprint import pprint


def get_cook_book(name_file):
    cook_book = {}
    line_ = ''
    with open(name_file) as file:
        counter = 0
        counter_dict = 0
        for line in file:
            if counter == 0 and not line.strip().isdigit():
                cook_book[line.strip()] = []
                line_ = line.strip()
            elif line.strip().isdigit():
                counter = int(line.strip())
                continue
            elif counter > 0 and line != '\n':
                cook_book[line_].append({'ingredient_name': None, 'quantity': None, 'measure': None})
                cook_book[line_][counter_dict]['ingredient_name'] = line.split('|')[0].strip()
                cook_book[line_][counter_dict]['quantity'] = line.split('|')[1].strip()
                cook_book[line_][counter_dict]['measure'] = line.split('|')[2].strip()
                counter_dict += 1
            elif line == '\n':
                counter = 0
                counter_dict = 0
                continue
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = get_cook_book('text.txt')
    dish_list = {}
    for dish in dishes:
        if dish in cook_book:
            for num_, values in enumerate(cook_book[dish]):
                if dish_list.get(values['ingredient_name']):
                    print(cook_book[dish][num_])
                    dish_list[values['ingredient_name']] = {'measure': cook_book[dish][num_]['measure'],
                                                            'quantity': (int(cook_book[dish][num_]['quantity']) + int(
                                                                cook_book[dish][num_]['quantity'])) * person_count}
                else:
                    dish_list[values['ingredient_name']] = {'measure': cook_book[dish][num_]['measure'],
                                                            'quantity': int(
                                                                cook_book[dish][num_]['quantity']) * person_count}
    return dish_list


pprint(get_cook_book('text.txt'))
pprint(get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 2))
