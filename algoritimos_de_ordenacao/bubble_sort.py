def bubble_sort(vetor):
    vetor_length = len(vetor)

    for section in range(vetor_length):
        for index in range(vetor_length - section -1): 
            next_index = index+1

            if vetor[index] > vetor[next_index]:
                temp = vetor[next_index]
                vetor[next_index] = vetor[index]
                vetor[index] = temp
    
    print(vetor)


bubble_sort([10,9,8,7,6,5,4,3,2,1])