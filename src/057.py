from fractions import Fraction


def expansions(n):
    half = Fraction(1, 2)

    for _ in range(n):
        half = Fraction(1, 2 + half)
        yield 1 + half

num = sum(1 for i in expansions(1000) if len(str(i.numerator)) > len(str(i.denominator)))
print(num)

