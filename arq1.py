
#-------------------------------------------------------------------------------------------------------

def main():
    size = int(input("Qual o tamanhao do vetor que sera ordenado?\n"))
    vet = []
    print("Digite os valores que estarao no vetor:\n")
    for i in range(size):
        vet.append(int(input(f"Posicao {i+1}: ")))
    
    imprimeVetor(vet, size)
    bubbleSort(vet, size)
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

if __name__ == "__main__":
    main()

#-------------------------------------------------------------------------------------------------------