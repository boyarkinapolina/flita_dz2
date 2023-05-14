import numpy as np
import graphviz

match input("Direction y|n\n"):      #Установление направленности графа
    case 'y':
        doctest = graphviz.Digraph()
    case 'n':
        doctest = graphviz.Graph()
    case _:
        print("Unknown command")
        exit()

matrix_incedence = []
nodes = 0
with open("matrix.txt") as matrix_f:  #Прочитывание и считывание матрицы из текстового файла
    for string in matrix_f:
        nodes += 1
        line = string.split()
        matrix_incedence.append(line)


for i in range(nodes):      # Добавление вершин по узлам
    doctest.node(str(i + 1))

arr = np.array(matrix_incedence, str)     # Записывание матрицы и затем ф-ия транспонирования
matrix = arr.transpose()

print(matrix)

set_edges = []  #Добавление ребер в граф
for s_nodes in matrix:
    node1 = True
    for i in range(len(s_nodes)):
        for j in range(i + 1, len(s_nodes)):
            if s_nodes[i] == s_nodes[j] == '1':
                set_edges.append(str(i + 1) + str(j + 1))
                node1 = False
    if node1 == True:
        for i in range(len(s_nodes)):
            if s_nodes[i] == '1':
                set_edges.append(str(i + 1) + str(i + 1))

doctest.edges(list(set_edges))

# Вывод
doctest.render('doctest-output/round-table.gv.pdf', view=True)