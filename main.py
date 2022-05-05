from FlatIterator import FlatIterator
from FlatGenerator import flat_generator
from Flat_Iterator_adv import flat_iterator_adv
from Flat_Generator_adv import flat_generator_adv


if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]

    for item in FlatIterator(nested_list):
        print(item)

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)

    print(20*"*")
    for item in  flat_generator(nested_list):
        print(item)



    very_nested_list = [
        ['a', 'b', 'c', ['d', ['e']]],
        ['f', 'h', False],
        [1, 2, None],
    ]

    print(20 * "*")
    for item in flat_iterator_adv(very_nested_list):
        print(item)

    flat_list = [item for item in flat_iterator_adv(very_nested_list)]
    print(flat_list)

    print(20 * "*")
    for item in  flat_generator_adv(nested_list):
        print(item)