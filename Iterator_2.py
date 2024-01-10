

from collections.abc import Iterable


#list1: list[list[str] | list[list[str | list[str]]]] = [['a','b'],['c','d','e'],[['f','g',['h','k']]]]
#list1 = [['a',100,'c'],['d','e',True]]
#list1 = [['a','b','c'],['d','e','f'],['g','h','k']]
list1 = [
        [['a'], ['b', 50],100],
        ['d', 'e', [['f'], 100], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]


class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list


    def unwrap_list1(self,mylist, result):

        if any(isinstance(i, list) for i in mylist):
            for value in mylist:
                if not isinstance(value, Iterable):
                    result.append(value)

                else:
                    self.unwrap_list1(value, result)
        else:
            count1 = 0
            while count1 < len(mylist):
                result.append(mylist[count1])
                count1 = count1 + 1


    def __iter__(self):
        self.result = []
        #self.item1 = None
        self.count = 0
        self.unwrap_list1(self.list_of_list, self.result)


        return self

    def __next__(self):


        if self.count == len(self.result):
            raise StopIteration
        self.item1 = self.result[self.count]
        self.count = self.count + 1
        return self.item1


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':

    for flat_iterator_item in FlatIterator(list1):
        print(flat_iterator_item)


    test_3()


