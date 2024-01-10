import types
from collections.abc import Iterable

#list1: list[list[str] | list[list[str | list[str]]]] = [['a','b'],['c','d','e'],[['f','g',['h','k']]]]
#list1 = [['a',100,'c'],['d','e',True]]
#list1 = [None,['a','b',100],['d','e','f'],['g','h','k']]
list1 = [
        [['a'], ['b', 50],100],
        ['d', 'e', [['f'], 100], False],
        [1, 2, None, [[[[['!']]]]], [100]]
    ]

def flat_generator(list_of_list):
    for item in list_of_list:
        if not isinstance(item, Iterable):
            yield item
            continue
        if any(isinstance(i, list) for i in item):
            yield from flat_generator(item)
        else:
            count1 = 0
            result=[]
            while count1 < len(item):
                item1=item[count1]
                yield item1
                count1 = count1 + 1


def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':

    for flat_iterator_item in flat_generator(list1):
        print(flat_iterator_item)
    test_4()