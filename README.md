# Fizzbuzz in Python

## Aim

Test ability to code in Python by using TDD to build a simple game of 'Fizzbuzz'

## Technologies

**Python** for development
**Nosetests** for testing

## Installation

Run `git clone git@github.com:telgi/fizzbuzz-python.git`

## Usage

Open `python` in the terminal:

```
from fizzbuzz.game import Fizzbuzz

fizzbuzz = Fizzbuzz()

i = 1

while i <= 100:
    fizzbuzz.play(i)
    i += 1
```

## Running Tests

Run `python -m "nose"`

## Approach

1. Return 'Fizz' for multiples of 3' [X]
2. Return 'Buzz' for multiples of 5' [X]
3. Return 'FizzBuzz' for multiples of 3 and 5' [X]
4. Return 'number' for other numbers not multiples of 3 or / and 5 [X] 
