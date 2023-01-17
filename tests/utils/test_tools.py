from app.utils.tools import itemgetter_with_dots, mask

from tests.utils.fixtures import *


def test_itemgetter_with_dots():
    assert itemgetter_with_dots(test_dict, '1.a.11') == 'aa'
    assert itemgetter_with_dots(test_dict, '1.b.22') == 22
    assert itemgetter_with_dots(test_dict, '1.b.33') is None
    assert itemgetter_with_dots(test_dict, '1.b.33', default=1) == 1
    assert itemgetter_with_dots(test_dict, '1.b.22', default=1) == 22


def test_mask():
    test_str = '01234567'
    assert mask(test_str, [1, 2]) == '0**34567'
    assert mask(test_str, [-3, -4]) == '0123**67'
    assert mask(test_str, [7, 8]) == '0123456*'
    assert mask(test_str, [-8, -9]) == '*1234567'
