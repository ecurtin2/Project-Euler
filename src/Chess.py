import numpy as np

N = 4

board = np.arange(N**2).reshape((N, N))

idx = np.concatenate(np.indices(board.shape).T)

moves = {
     'upleft': np.array((-1, 2))
    ,'upright': np.array((1, 2))

    ,'rightup': np.array((2, 1))
    ,'rightdown': np.array((2, -1))

    ,'downright': np.array((1, -2))
    ,'downleft': np.array((-1, -2))

    ,'leftdown': np.array((-2, -1))
    ,'leftup': np.array((-2, 1))
}
print(idx)
