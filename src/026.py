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