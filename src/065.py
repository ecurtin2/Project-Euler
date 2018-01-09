from fractions import Fraction
import itertools as it


def convergent(start, seq, N_terms):
    num, den = 1, 0
    if N_terms == 1:
        return start
    elif N_terms > 1:
        sequence = tuple(it.islice(seq, N_terms - 1))
        for val in reversed(sequence):
            num, den = den + num * val, num
        return Fraction(start, 1) + Fraction(den, num)


seq = it.chain.from_iterable((1, 2 * k, 1) for k in it.count(1))
frac = convergent(2, seq, 100)
print(sum(int(digit) for digit in str(frac.numerator)))