import typing as tp

def do_floyd(adj_matrix: tp.List[tp.List[int]]) -> tp.List[tp.List[int]]:
    for k in range(n): 
        for i in range(n):
            for j in range(n): 
                adj.matrix[i][j] = min(adj.matrix[i][j], adj.matrix[i][k] + adj.matrix[k][j])
    pass

class ShortPathFinder:
    def __init__(self, short_path_matrix: tp.List[tp.List[int]]):
        self._short_path_matrix = short_path_matrix
       


    @classmethod
    def from_adj_matrix(cls, adj_matrix: tp.List[tp.List[int]]):
        short_path_matrix = do_floyd(adj_matrix)
        return cls(short_path_matrix)

    @classmethod
    def from_text_file(cls, path_to_file: str):
        # TODO: load short_path_matrix from file
        return cls(short_path_matrix)


    def get_shortest_distance(self, fr: int, to: int):
        ind=0 #индекс нужной станции
hel=0
minc=999999999
for i in range (n):
    hel=abs(_short_path_matrix[i][fr]-_short_path_matrix[i][to])+_short_path_matrix[i][fr]+_short_path_matrix[i][to]
    if hel<minc:
        minc=hel
        ind=i
        pass



def main():
    path_finder = ShortPathFinder.from_text_file('cached_short_path_matrix.txt')


    path_finder.get_shortest_distance(0, 1)
    path_finder.get_shortest_distance(2, 3)
    a = [[1, 2, 4], [1,2,3], [5, 6, 7]]
    cls = ShortPathFinder.from_adj_matrix(a)
    pass

if __name__ == '__main__':
    main()