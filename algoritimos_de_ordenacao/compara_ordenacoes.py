import random 

from datetime import datetime
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from selection_sort import selection_sort
from shell_sort import shell_sort
from quick_sort import quick_sort

elementos = []
for _ in range(998):
    elementos.append(round(random.uniform(0, 1)))


startTime = datetime.now()
bubble_sort(elementos.copy())
print('bubble_sort:', datetime.now() - startTime)

startTime = datetime.now()
insertion_sort(elementos.copy())
print('insertion_sort:', datetime.now() - startTime)

startTime = datetime.now()
shell_sort(elementos.copy())
print('shell_sort:', datetime.now() - startTime)

startTime = datetime.now()
merge_sort(elementos.copy())
print('merge_sort:', datetime.now() - startTime)

startTime = datetime.now()
selection_sort(elementos.copy())
print('selection_sort:', datetime.now() - startTime)

startTime = datetime.now()
quick_sort(elementos.copy(), 0, len(elementos) - 1)
print('quick_sort:', datetime.now() - startTime)