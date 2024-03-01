def recursao(i):
    print("Recursão")

    i += 1
    if i == 5:
        return
    
    recursao(i)

def soma(n):
    if n == 0:
        return 0
    
    return n + soma(n-1)

def fat(m):
    if m == 0:
        return 1
    
    return m * fat(m-1)

def potencia(base, expoente):
    if expoente == 0:
        return 1
    
    return base * potencia(base, expoente - 1)

print(fat(6))
print("-------------")
print(potencia(2, 2))
print("-------------")
print(potencia(2, 3))
print("-------------")
print(potencia(2, 4))
print("-------------")
print(soma(5))
print("-------------")
recursao(0)


