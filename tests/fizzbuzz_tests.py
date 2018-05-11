from nose.tools import *
from fizzbuzz.game import Fizzbuzz

def test_multiples_of_3():
    fizzbuzz = Fizzbuzz()

    assert_equal(fizzbuzz.play(3), 'Fizz')

def test_multiples_of_5():
    fizzbuzz = Fizzbuzz()

    assert_equal(fizzbuzz.play(5), 'Buzz')

def test_multiples_of_3_and_5():
    fizzbuzz = Fizzbuzz()

    assert_equal(fizzbuzz.play(15), 'FizzBuzz')

def test_all_other_numbers():
    fizzbuzz = Fizzbuzz()

    assert_equal(fizzbuzz.play(1), 1)
