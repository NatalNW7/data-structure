def shell_sort(vetor):
    vetor_len = len(vetor) 
    intervalo = vetor_len // 2

    while intervalo > 0:
        for index in range(intervalo, vetor_len):
            temp = vetor[index]
            temp_index = index

            while (temp_index >= intervalo) and (vetor[temp_index - intervalo] > temp):
                vetor[temp_index] = vetor[temp_index - intervalo]
                temp_index -= intervalo
            vetor[temp_index] = temp
        intervalo //=2

    return vetor

if "__main__" == __name__:
    shell_sort([15,34,8,3,50,60])
    shell_sort([15,34,8,3])
    shell_sort([10,9,8,7,6,5,4,3,2,1])