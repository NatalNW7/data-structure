def insertion_sort(vetor):
    vetor_length = len(vetor)

    for index in range(1, vetor_length):
        maked_value = vetor[index]

        before_index = index-1
        while (before_index >= 0) and (maked_value < vetor[before_index]):
            vetor[before_index + 1] = vetor[before_index]
            before_index-=1
        
        vetor[before_index+1] = maked_value

        
    return vetor

if "__main__" == __name__:
    insertion_sort([15,34,8,3,50,60])
    insertion_sort([15,34,8,3])
    insertion_sort([10,9,8,7,6,5,4,3,2,1])