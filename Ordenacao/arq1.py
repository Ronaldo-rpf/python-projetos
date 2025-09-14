
#-------------------------------------------------------------------------------------------------------

def main():
    size = int(input("Qual o tamanhao do vetor que sera ordenado?\n"))
    vet = []
    print("Digite os valores que estarao no vetor:\n")
    for i in range(size):
        vet.append(int(input(f"Posicao {i+1}: ")))
    
    print("Deseja usar qual forma de ordenacao?")
    print("1 - BubbleSort\n2 - MergeSort\n3 - QuickSort")
    escolha = int(input())

    match escolha:
        case 1:
            print("Voce escolheu o BubbleSort.")
            print("Vetor antes da ordenacao:")
            imprimeVetor(vet, size)
            bubbleSort(vet, size)
            print("\nVetor apos a ordenacao:")
            imprimeVetor(vet, size)
        case 2:
            print("Voce escolheu o MergeSort.")
            print("Vetor antes da ordenacao:")
            imprimeVetor(vet, size)
            mergeSort(vet, 0, size-1)
            print("\nVetor apos a ordenacao:")
            imprimeVetor(vet, size)        
        case 3:
            print("Voce escolheu o QuickSort.")
            print("Vetor antes da ordenacao:")
            imprimeVetor(vet, size)
            quickSort(vet, 0, size-1)
            print("\nVetor apos a ordenacao:")
            imprimeVetor(vet, size)
        


    print("Fim do Programa!!!")

#-------------------------------------------------------------------------------------------------------

def imprimeVetor(vet, size):
    for i in range(size):
        print(f"{vet[i]} ", end='')
    print()

#-------------------------------------------------------------------------------------------------------

def bubbleSort (vet, size):
    aux: int
    for i in range(size-1):
        for j in range(size-1-i):
            if vet[j] > vet[j+1]:
                aux = vet[j]
                vet[j] = vet[j+1]
                vet[j+1] = aux

#-------------------------------------------------------------------------------------------------------

def mergeSort (vet, esq, dir):
    if esq >= dir:
        return
    
    mid = (esq + dir) // 2
    mergeSort(vet, esq, mid)
    mergeSort(vet, mid + 1, dir)
    merge(vet, esq, mid, dir)


def merge (vet, esq, mid, dir):
    vetAux = []
    i = esq
    j = mid + 1

    while i <= mid and j <= dir:
        if vet[i] > vet[j]:
            vetAux.append(vet[j])
            j += 1

        else:
            vetAux.append(vet[i])
            i += 1

    while i <= mid:
        vetAux.append(vet[i])
        i += 1

    while j <= dir:
        vetAux.append(vet[j])
        j += 1

    for x in range(len(vetAux)):
        vet[esq + x] = vetAux[x]

    return 

#-------------------------------------------------------------------------------------------------------

def quickSort (vet, esq, dir):
    if esq >= dir:
        return
    
    indexPivo = particiona(vet, esq, dir)
    quickSort(vet, esq, indexPivo - 1)
    quickSort(vet, indexPivo + 1, dir)


def particiona (vet, esq, dir) -> int:
    pivo = vet[dir]
    i = esq - 1
    aux: int

    for j in range(esq, dir):
        if (vet[j] <= pivo):
            i += 1
            aux = vet[i]
            vet[i] = vet[j]
            vet[j] = aux

    aux = vet[i + 1]
    vet[i + 1] = vet[dir]
    vet[dir] = aux
    return (i + 1)

#-------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
