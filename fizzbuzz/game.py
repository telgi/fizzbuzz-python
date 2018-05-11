class Fizzbuzz(object):

    def __init__(self):
        pass

    def play(self, number):
        if number % 3 == 0:
            return 'Fizz'
        elif number % 5 == 0:
            return 'Buzz'
