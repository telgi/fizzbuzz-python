from nose.tools import *
from fizzbuzz.game import Fizzbuzz

def test_multiples_of_3():
    fizzbuzz = Fizzbuzz()

    assert_equal(fizzbuzz.play(3), 'Fizz')
    assert_equal(fizzbuzz.play(6), 'Fizz')
    assert_equal(fizzbuzz.play(9), 'Fizz')

def test_multiples_of_5():
    fizzbuzz = Fizzbuzz()

    assert_equal(fizzbuzz.play(5), 'Buzz')
    assert_equal(fizzbuzz.play(10), 'Buzz')
    assert_equal(fizzbuzz.play(20), 'Buzz')

def test_multiples_of_3_and_5():
    fizzbuzz = Fizzbuzz()

    assert_equal(fizzbuzz.play(15), 'FizzBuzz')
    assert_equal(fizzbuzz.play(30), 'FizzBuzz')
    assert_equal(fizzbuzz.play(45), 'FizzBuzz')

def test_all_other_numbers():
    fizzbuzz = Fizzbuzz()

    assert_equal(fizzbuzz.play(1), 1)
    assert_equal(fizzbuzz.play(8), 8)
    assert_equal(fizzbuzz.play(13), 13)
