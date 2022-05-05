class FlatIterator:


    def __init__(self, nested_list):
        self.flat_list = []
        self.flat_list = sum(nested_list, [])



    def __iter__(self):


        return self


    def __next__(self):
        if self.flat_list:
            return self.flat_list.pop(0)
        else:
            raise StopIteration



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
