def partition(vetor, begin, end):
    pivot = vetor[end]
    position = begin - 1

    for index in range(begin, end):
        if vetor[index] <= pivot:
            position +=1
            vetor[position], vetor[index] = vetor[index], vetor[position]
    vetor[position + 1], vetor[end] = vetor[end], vetor[position + 1]

    return position + 1


def quick_sort(vetor, begin, end):
    if begin < end:
        position = partition(vetor, begin, end)
        # sort left
        quick_sort(vetor, begin, position - 1)
        # sort right
        quick_sort(vetor, position + 1, end)

    return vetor

if "__main__" == __name__:
    vetor1 = [15,34,8,3,50,60]
    vetor2 = [15,34,8,3]
    vetor3 = [10,9,8,7,6,5,4,3,2,1]
    print(quick_sort(vetor1, 0, len(vetor1) - 1))
    print(quick_sort(vetor2, 0, len(vetor2) - 1))
    print(quick_sort(vetor3, 0, len(vetor3) - 1))