#2D List

#lista dentro de lista
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0][0])                  #[] Linha [] Coluna        #tanto a linha quanto a coluna começam por 0 na matriz
print("")


#nested for loop
for row in number_grid:
    for col in row:
        print(col)
