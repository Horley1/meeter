import json
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
#import overpy
import math
from geopy.distance import geodesic

class Cafe():
    def __init__(self, a, b):
        self.a = self.__ids(a)
        self.b = self.__ids(b)

    def __ids(self, nm):
        dict2 = json.load(open('dic2.json', 'r'))
        arr = dict2.keys()
        a = process.extract(nm, arr, limit=1)
        dictt = list(dict2[a[0][0]].keys())
        return int(dict2[a[0][0]][dictt[0]])

    def gen_pos(self):
        a = self.a
        b = self.b
        tab = json.load(open('saving1.json', 'r', encoding = "ISO-8859-1"))
        dict1 = json.load(open('dic1.json', 'r', encoding = "ISO-8859-1"))
        dict2 = json.load(open('dic2.json', 'r', encoding = "ISO-8859-1"))
        places = json.load(open('cafes.json', 'r', encoding = "ISO-8859-1"))
        hh = json.load(open('json.json', 'r',  encoding = "ISO-8859-1"))
        n, nc, ind, hel, minc, minc2, p = 241, 367, 0, 0, 10000, 10000, 10

        for i in range(n, nc):
            if abs(tab[i][a] - tab[i][b]) < p:
                hel =tab[i][b]+tab[i][a]
                if hel < minc:
                    minc = hel
                    ind1 = i
                    f_min = tab[i][a]
                    sc_min = tab[i][b]

        for j in range(n):
            if tab[ind1][j] < minc2:
                minc2 = tab[ind1][j]
                mini_ind = j
        return [places[ind1 - 241], dict1[str(mini_ind)], f_min, sc_min]


