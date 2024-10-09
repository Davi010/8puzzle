import random

def criando_matriz():
    lista = [1, 2, 3, 4, 5, 6, 7, 8]
    random.shuffle(lista)
    lista.append(0)
    desafio = [lista[i:i + 3] for i in range(0, 9, 3)]
    return desafio

def gerar_matriz(desafio):
    for linha in desafio:
        print(linha)

def caminhos_possiveis(desafio):
    l, c = next((i + 1, j + 1) for i in range(3) for j in range(3) if desafio[i][j] == 0)
    caminhos = []

    if l > 1:
        caminhos.append("Cima")
    if l < 3:
        caminhos.append("Baixo")
    if c > 1:
        caminhos.append("Esquerda")
    if c < 3:
        caminhos.append("Direita")

    return caminhos

def mover(desafio, movimento):
   
    for i in range(3):
        for j in range(3):
            if desafio[i][j] == 0:
                zero_pos = (i, j)

    novo_desafio = [linha[:] for linha in desafio] 
    if movimento == "Cima":
        novo_desafio[zero_pos[0]][zero_pos[1]], novo_desafio[zero_pos[0] - 1][zero_pos[1]] = novo_desafio[zero_pos[0] - 1][zero_pos[1]], novo_desafio[zero_pos[0]][zero_pos[1]]
    elif movimento == "Baixo":
        novo_desafio[zero_pos[0]][zero_pos[1]], novo_desafio[zero_pos[0] + 1][zero_pos[1]] = novo_desafio[zero_pos[0] + 1][zero_pos[1]], novo_desafio[zero_pos[0]][zero_pos[1]]
    elif movimento == "Esquerda":
        novo_desafio[zero_pos[0]][zero_pos[1]], novo_desafio[zero_pos[0]][zero_pos[1] - 1] = novo_desafio[zero_pos[0]][zero_pos[1] - 1], novo_desafio[zero_pos[0]][zero_pos[1]]
    elif movimento == "Direita":
        novo_desafio[zero_pos[0]][zero_pos[1]], novo_desafio[zero_pos[0]][zero_pos[1] + 1] = novo_desafio[zero_pos[0]][zero_pos[1] + 1], novo_desafio[zero_pos[0]][zero_pos[1]]

    return novo_desafio

def busca_profundidade(desafio, caminho=[], passos=set(), profundidade=0, limit=20):
    if profundidade >= limit:
        return None, None

    estado = str(desafio)
    if estado in passos:
        return None, None
    
    passos.add(estado)


    if desafio == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
        return caminho, desafio
    
    #print("Matriz atual:")
    #gerar_matriz(desafio)  

    for movimento in caminhos_possiveis(desafio):
        novo_estado = mover(desafio, movimento)
        solucao, matriz_final = busca_profundidade(novo_estado, caminho + [movimento], passos, profundidade + 1, limit)
        if solucao:
            return solucao, matriz_final

    passos.remove(estado)
    return None, None

matriz_inicial = criando_matriz()
print("Matriz inicial:")
gerar_matriz(matriz_inicial)


solucao, matriz_resolvida = busca_profundidade(matriz_inicial)
if solucao:
    print("\nSolução Encontrada!")
    print("Movimentos:", solucao)
    print("\nMatriz Solucionada:")
    gerar_matriz(matriz_resolvida)
else:
    print("Sem solução encontrada no limite da profundidade que é 20.")
