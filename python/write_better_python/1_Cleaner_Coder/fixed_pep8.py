import pep8


def foo_bar(arg1, arg2, arg3, arg4):
    return arg1, arg2, arg3, arg4


def bar(*args):
    return 2 + 2


class Treehouse:
    def one(self):
        return 1

    def two(self):
        return 2


alpha, beta, charlie, delta = foo_bar(
    "a long string",
    "a longer string",
    "yet another long string",
    "and other crazy string"
)


one = 1
three = 3
fourteen = 14

print(alpha)
print(fourteen)

print(Treehouse().two())


checker = pep8.Checker('fixed_pep8.py')
checker.check_all()
