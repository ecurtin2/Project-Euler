import numpy as np


class Vertex(object):

    def __init__(self, value, i_row, i_col):
        self.value = value
        self.row = i_row
        self.col = i_col
        self.loc = (i_row, i_col)
        self.connected = set()

    def connect(self, vertices):
        try:
            for v in vertices:
                self.connected.add(v)
        except TypeError:
                self.connected.add(vertices)

    def __str__(self):
        return "Vertex Value = {}, connected to {}".format(self.value, tuple(v.value for v in self.connected))


class ArrayGraph(object):
    """Weighted directed graph for 2D numpy array"""

    def __init__(self, ary, down=True, right=True, left=False, up=False):
        self.vertices = np.empty(ary.shape, dtype=Vertex)
        self.M, self.N = ary.shape
        for i in range(self.M):
            for j in range(self.N):
                self.vertices[i, j] = Vertex(ary[i, j], i_row=i, i_col=j)

        if down:
            for i in range(self.M - 1):
                for j in range(self.N):
                    self.vertices[i, j].connect(self.vertices[i + 1, j])
        if right:
            for i in range(self.M):
                for j in range(self.N - 1):
                    self.vertices[i, j].connect(self.vertices[i, j + 1])
        if up:
            for i in range(1, self.M):
                for j in range(self.N):
                    self.vertices[i, j].connect(self.vertices[i - 1, j])
        if left:
            for i in range(self.M):
                for j in range(1, self.N):
                    self.vertices[i, j].connect(self.vertices[i, j - 1])

    def minimum_path_val(self, start=(0, 0), destination=None, method='dijkstra', *args, **kwargs):
        min_funcs = {'dijkstra' : self._dijkstra}
        return min_funcs[method](start, destination, *args, **kwargs)

    def _dijkstra(self, start=(0, 0), destination=None):
        if destination is None:
            destination = (self.M - 1, self.N - 1)
        distances = np.full_like(self.vertices, fill_value=1e7, dtype=int)
        current = self.vertices[start]
        distances[start] = current.value
        unvisited = np.full_like(self.vertices, fill_value=True, dtype=bool)

        while True:
            smallest_temp = (None, 1e7)
            for v in current.connected:
                temp = distances[current.loc] + v.value
                if temp < distances[v.loc]:
                    distances[v.loc] = temp
                if temp < smallest_temp[1]:
                    smallest_temp = (v, temp)

            unvisited[current.loc] = False
            if current == self.vertices[destination]:
                return distances[destination]

            temp = distances + np.logical_not(unvisited) * 10**7
            current = self.vertices[np.unravel_index(temp.argmin(), distances.shape)]

    def __str__(self):
        l = []
        for v in np.nditer(self.vertices, flags=('refs_ok',)):
            l.append(str(v))
        return '\n'.join(l)