class flat_iterator_adv:


    def __init__(self, nested_list, recu=True):
        self.flat_list = []
        if recu:
            self.flat_req(nested_list)
        else:
            self.lst = nested_list
            self.flat_bubble()

    def flat_req(self, lst):
        for item in lst:
            if not isinstance(item, list):
                self.flat_list.append(item)
            else:
                self.flat_req(item)

    def flat_bubble(self):
        while self.lst:
            el = self.lst[0]
            if not isinstance(el, list):
                self.flat_list.append(self.lst.pop(0))
            else:
                self.lst = [*self.lst[0]] + self.lst[1:]




    def __iter__(self):


        return self


    def __next__(self):
        if self.flat_list:
            return self.flat_list.pop(0)
        else:
            raise StopIteration



if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c',['d',['e']]],
        ['f', 'h', False],
        [1, 2, None],
    ]


    for item in flat_iterator_adv(nested_list):
        print(item)

    flat_list = [item for item in flat_iterator_adv(nested_list, False)]
    print(flat_list)
