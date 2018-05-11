from nose.tools import *
from fizzbuzz.game import Fizzbuzz

def test_multiples_of_3():
    fizzbuzz = Fizzbuzz()

    assert_equal(fizzbuzz.play(3), 'Fizz')
