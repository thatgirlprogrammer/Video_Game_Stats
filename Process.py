def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list


def get_number(option_value, type_val=float):
    try:
        option_value = type_val(option_value)
    except ValueError:
        return get_number(input('Not a number. Enter a number'), int)
    return option_value
