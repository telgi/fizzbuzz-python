try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Fizzbuzz in Python, using TDD',
    'author': 'Terence Allitt',
    'url': 'https://github.com/telgi/fizzbuzz-python',
    'download_url': 'git@github.com:telgi/fizzbuzz-python.git',
    'author_email': 'tallitt88@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['fizzbuzz'],
    'scripts': [],
    'name': 'fizzbuzz'
}

setup(**config)
