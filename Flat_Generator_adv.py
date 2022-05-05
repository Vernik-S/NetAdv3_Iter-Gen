def flat_generator_adv(nested_list):
    while nested_list:
        el = nested_list[0]
        if not isinstance(el, list):
            yield nested_list.pop(0)
        else:
            nested_list = [*nested_list[0]] + nested_list[1:]


if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c', ['d', ['e']]],
        ['f', 'h', False],
        [1, 2, None],
    ]
    for item in  flat_generator_adv(nested_list):
        print(item)