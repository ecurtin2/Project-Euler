"""

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2= 0.5
1/3= 0.(3)
1/4= 0.25
1/5= 0.2
1/6= 0.1(6)
1/7= 0.(142857)
1/8= 0.125
1/9= 0.(1)
1/10= 0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
Find the value of d &lt; 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

"""

N = 10


def repeating_divide(num, den):
    assert(den != 0)
    result = []
    repeated = []
    repeat = None
    for i in range(1, 1000):
        d = num // den
        r = num % den
        if r == 0:
            result.append(d)
            break
        else:
            result.append(d)
            num = 10 * (num - den * d)
            if num in repeated:
                repeat = result[(repeated.index(num) + 1):]
                break
            else:
                repeated.append(num)
    if len(result) > 1:
        result = ''.join(
            [str(result[0]), '.'] + [str(i) for i in result[1:]])
    else:
        result = str(result[0])
    if repeat is not None:
        repeat = ''.join(str(i) for i in repeat)
    return result, repeat

repeats = ((i, repeating_divide(1, i)[1]) for i in range(1, 1000)
           if repeating_divide(1, i)[1] is not None)

maxval = max(repeats, key=lambda x: len(x[1]))
print(maxval[0], len(maxval[1]))