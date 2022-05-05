def flat_generator(nested_list):
    flat_list = sum(nested_list, [])
    while flat_list:
        yield flat_list.pop(0)


if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]
    for item in  flat_generator(nested_list):
        print(item)