from math import sqrt


def n_rects_total(N, M):
    return (N * (N + 1) // 2) * (M * (M + 1) // 2)


target = 4.1235 * 10 ** 6
N_max = int(1 / 2 * (sqrt(4 * (2*target) + 1) - 1))   # Highest value of N where n_rects_total(N, 1) <= 2 * target
vals = ((N, M, n_rects_total(N, M)) for N in range(1, N_max + 1) for M in range(1, N + 1))
min_val = min(vals, key=lambda x: abs(x[2] - target))
print("Closest to target {} is {} x {} with area {}.".format(target, min_val[0], min_val[1], min_val[2]))