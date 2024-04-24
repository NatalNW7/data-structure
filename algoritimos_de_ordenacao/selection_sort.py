def selection_sort(vetor):
    vetor_length = len(vetor)

    for section in range(vetor_length):
        min_value_position = section

        for index in range(section + 1, vetor_length):
            if vetor[min_value_position] > vetor[index]:
                min_value_position = index

        temp = vetor[section]
        vetor[section] = vetor[min_value_position] 
        vetor[min_value_position] = temp

    print(vetor)

selection_sort([15,34,8,3,50,60])
selection_sort([15,34,8,3])
selection_sort([10,9,8,7,6,5,4,3,2,1])