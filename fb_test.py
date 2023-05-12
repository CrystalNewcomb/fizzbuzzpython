import unittest
from fb import fizz_buzz, fizz_buzz_list, fizz_buzz_dict


class TestFizzBuzzNum(unittest.TestCase):
    def test_fb_num(self):
        thing = fizz_buzz(30)
        assert thing[0] == 'FizzBuzz'
        assert thing[3] == 'Fizz'
        assert thing[5] == 'Buzz'
        assert thing[1] == 'Taco'

    def test_fb_list(self):
        thing = fizz_buzz_list([7, 9, 5, 11, 12, 13, 30, 67])
        assert thing[6] == 'FizzBuzz'
        assert thing[1] == 'Fizz'
        assert thing[2] == 'Buzz'
        assert thing[0] == 'Taco'

    def test_fb_dict(self):
        thing = fizz_buzz_dict({'a': 7, 'b': 9, 'c': 10, 'd': 30})
        assert thing[3] == 'FizzBuzz'
        assert thing[1] == 'Fizz'
        assert thing[2] == 'Buzz'
        assert thing[0] == 'Taco'
