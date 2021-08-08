n=241
tab = [[0] * n for i in range(n)]
for k in range(n): 
    for i in range(n):
        for j in range(n): 
            tab[i][j] = min(tab[i][j], tab[i][k] + tab[k][j])
for i in range(n):
        for j in range(n): 
            print(tab[i][j], end=" ")
        print("\n")