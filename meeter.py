import json
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import networkx as nx
import matplotlib.pyplot as plt

class GraphVisualization:
   
    def __init__(self):
          
        # visual is a list which stores all 
        # the set of edges that constitutes a
        # graph
        self.visual = []
          
    # addEdge function inputs the vertices of an
    # edge and appends it to the visual list
    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)
          
    # In visualize function G is an object of
    # class Graph given by networkx G.add_edges_from(visual)
    # creates a graph with a given list
    # nx.draw_networkx(G) - plots the graph
    # plt.show() - displays the graph
    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        plt.show()


def ids(nm, ln, k):
    global dict2
    arr = dict2.keys()
    a = process.extract(nm, arr, limit=1)
    print(a)
    print(k)
    print(dict2[a[0][0]])
    if k == 0:
        dictt = list(dict2[a[0][0]].keys())
        return int(dict2[a[0][0]][dictt[0]])
    else:
        return int(dict2[a[0][0]][ln])        

f = open("D:\dict2.json", "r")
js = json.loads(f.readline())
sf = open("D:\map.json", "rb")
dic = json.load(sf)
dic2 = open("D:\dic2.json", "rb")
dict2 = json.load(dic2)
dic3 = open("D:\dic1.json", "rb")
dict3 = json.load(dic3)
keys = js.keys()
savingg = open("D:\saving.json", "w")
G = GraphVisualization()
tab = [[200] * 243 for i in range(243)]
for elem in keys:
    for j in range(len(js[elem])):
        #print(js[elem][j])
        if js[elem][j][1] != -1:
            tab[js[elem][j][0]][js[elem][j][0] + 1] = int(js[elem][j][1])
            tab[js[elem][j][0] + 1][js[elem][j][0]] = int(js[elem][j][1])
            G.addEdge(js[elem][j][0], js[elem][j][0] + 1)
k = -1
for elem in dic['connections']:
    mass = []
    for conn in elem:
        k += 1
        if str(int(conn['lineId'])) == '14' or str(int(conn['lineId'])) == '13':
            mass = []
            break
        else:
            print(conn)
            mass.append(ids(conn['name'], str(int(conn['lineId'])), k))
    k = -1
    if mass == []:
        continue
    if len(mass) == 2:
        tab[mass[0]][mass[1]], tab[mass[1]][mass[0]] = 4, 4
        G.addEdge(mass[0], mass[1])
    else:
        tab[mass[0]][mass[1]], tab[mass[1]][mass[0]], tab[mass[2]][mass[0]], tab[mass[0]][mass[2]], tab[mass[1]][mass[2]], tab[mass[2]][mass[1]] = 4, 4, 4, 4, 4, 4
        G.addEdge(mass[0], mass[1])
        G.addEdge(mass[1], mass[2])
        G.addEdge(mass[2], mass[0])
print(k)
G.visualize()
n=243
###
for k in range(n): 
    for i in range(n):
        for j in range(n): 
            tab[i][j] = min(tab[i][j], tab[i][k] + tab[k][j])
json.dump(tab, savingg)
savingg.close()
'''        
for i in range(n):
        for j in range(n): 
            print(tab[i][j], end=" ")
        print("") #

ind=0 #
hel=0
minc=10000
a=221 #
b=8 #
for i in range (n):
    hel=abs(tab[i][a]-tab[i][b]) + max(tab[i][b], tab[i][a])
    if hel<minc:
        minc=hel
        ind=i
        f_min = tab[i][a]
        sc_min = tab[i][b]
print(dict3[str(ind)])
print(f_min)
print(sc_min)
print(tab[26][221])
print(tab[26][8])'''