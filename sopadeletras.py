def exist(board: list, word: str) -> bool:
    limit = len(board)
    limit2 = len(board[0])
    if not board or len(board[0]) * len(board) < len(word):
        return False
    for i, c1 in enumerate(board):
        for j, c in enumerate(board[i]):
            if word[0] == c:
                # print(i,j)
                #paso none para tener un path limpio, siempre se inicia desde la primer letra
                if encontrarpalabra(i, j, word, 0, board, None):
                    return True

    return False


def encontrarpalabra(index1, index2, word, indexletter, grid, path):
    limit = len(grid)
    limit2 = len(grid[0])
    if not path:
        path = list()
    ##agrego una pila para validar el camino que ya recorrio
    path.append([index1, index2])
    print(path)
    # --- aqui puedes checar el path que se va generando
    if indexletter + 1 == len(word):
        return True

    nextletter = word[indexletter + 1]
    #exploro las opciones son ocho casillas las que rodean y sigo explorando las opciones validas solo hago return si es verdadera la secuencia del path para no parar de explorar
    if index2 + 1 < limit2 and [index1, index2 + 1] not in path and grid[index1][index2 + 1] == nextletter:
        if encontrarpalabra(index1, index2 + 1, word, indexletter + 1, grid, path):
            return True
    if index1 + 1 < limit and [index1 + 1, index2] not in path and grid[index1 + 1][index2] == nextletter:
        if encontrarpalabra(index1 + 1, index2, word, indexletter + 1, grid, path):
            return True

    if index1 - 1 >= 0 and [index1 - 1, index2] not in path and grid[index1 - 1][index2] == nextletter:
        if encontrarpalabra(index1 - 1, index2, word, indexletter + 1, grid, path):
            return True

    if index2 - 1 >= 0 and [index1, index2 - 1] not in path and grid[index1][index2 - 1] == nextletter:
        if encontrarpalabra(index1, index2 - 1, word, indexletter + 1, grid, path):
            return True

    if index2 - 1 >= 0 and index1 + 1 < limit and [index1 + 1, index2 - 1] not in path and grid[index1 + 1][index2 - 1] == nextletter:
        if encontrarpalabra(index1 + 1, index2 - 1, word, indexletter + 1, grid, path):
            return True

    if index2 - 1 >= 0 and index1 - 1 >= 0 and [index1 -1, index2 - 1] not in path and grid[index1 - 1][index2 - 1] == nextletter:
        if encontrarpalabra(index1 -1, index2 - 1, word, indexletter + 1, grid, path):
            return True

    if index2 + 1 < limit2 and index1 - 1 >= 0 and [index1 - 1, index2 + 1] not in path and grid[index1 - 1][index2 + 1] == nextletter:
        if encontrarpalabra(index1 - 1, index2 + 1, word, indexletter + 1, grid, path):
            return True

    if index2 + 1 < limit2 and index1 + 1 < limit and [index1 + 1, index2 + 1] not in path and grid[index1 + 1][index2 + 1] == nextletter:
        if encontrarpalabra(index1 + 1, index2 + 1, word, indexletter + 1, grid, path):
            return True
    #si el camino no es valido lo quito de la pila
    path.pop()

lettergrid = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
word_to_search = "ABCEFSADEESE"
print(exist(lettergrid, word_to_search))
#assert True == exist(lettergrid, word_to_search)

lettergrid = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
"""
Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""
word_to_search = "ABCCED"
print(exist(lettergrid, word_to_search))
#assert True == exist(lettergrid, word_to_search)
word_to_search = "SEE"
print(exist(lettergrid, word_to_search))
#assert True == exist(lettergrid, word_to_search)
word_to_search = "ABCB"
print(exist(lettergrid, word_to_search))
#assert False == exist(lettergrid, word_to_search)