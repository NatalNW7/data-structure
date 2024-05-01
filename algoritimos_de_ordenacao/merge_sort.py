def merge_sort(vetor):
    if len(vetor) > 1:
        div = len(vetor) // 2
        left = vetor[:div].copy()
        right = vetor[div:].copy()

        merge_sort(left)
        merge_sort(right)

        index_left = index_right = index = 0

        # sort left and right
        while index_left < len(left) and index_right < len(right):
            if left[index_left] < right[index_right]:
                vetor[index] = left[index_left]
                index_left +=1
            else:
                vetor[index] = right[index_right]
                index_right +=1
            index +=1

        # final sort
        while index_left < len(left):
            vetor[index] = left[index_left]
            index_left +=1
            index +=1

        while index_right < len(right):
            vetor[index] = right[index_right]
            index_right +=1
            index +=1

    return vetor

if "__main__" == __name__:
    print(merge_sort([15,34,8,3,50,60]))
    print(merge_sort([15,34,8,3]))
    print(merge_sort([10,9,8,7,6,5,4,3,2,1]))
