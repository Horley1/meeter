n=241 #вершин в графе
tab = [[0] * n for i in range(n)]
#тут надо заполнить таблицу
for k in range(n): 
    for i in range(n):
        for j in range(n): 
            tab[i][j] = min(tab[i][j], tab[i][k] + tab[k][j])
for i in range(n):
        for j in range(n): 
            print(tab[i][j], end=" ")
        print("\n") # вывод надо в txt
ind=0 #индекс нужной станции
hel=0
a=1 #станция а
b=2 #станция b
for i in range n:
    help=abs(tab[i][a]-tab[i][b])+(tab[i][b]+tab[i][a]
    if help<c
        c=hel
        ind=i
