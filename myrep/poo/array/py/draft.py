meu_arrayVazio = []
print(meu_arrayVazio)

meu_array = [10, 20, 30, 40]
print(meu_array)

tamanho = len(meu_array)
print(tamanho)  

meu_array.pop()
print(meu_array)

meu_array.insert(0, 5)
print(meu_array)  

meu_array.insert(0, 5)
print(meu_array)  
meu_array.pop(0)
print(meu_array)

meu_array.insert(2, 99)  
print(meu_array)

meu_array.remove(20)  
print(meu_array)  

nomes = ["Augusto", "Senna", "Carlos"]
resultado = " - ".join(nomes)
print(resultado)

n = 10
meu_array = list(range(0, n + 1))
print(meu_array)

import random  

meu_array = [random.randint(0, 100) for _ in range(10)]
print(meu_array)

print(meu_array[0])  
print(meu_array[2])  
print(meu_array[-1])

for valor in meu_array:
    print(valor)

meu_array = [5, 10, 15, 20, 25]
for i in range(len(meu_array)):
    print(f"Índice {i}: valor = {meu_array[i]}")

x = 15 
encontrado = False

for elemento in meu_array:
    if elemento == x:
        encontrado = True
        break 
if encontrado:
    print(f"O elemento {x} foi encontrado no array!")
else:
    print(f"O elemento {x} não está no array.")

x = 15

if x in meu_array:
    print(f"O elemento {x} está no array!")
else:
    print(f"O elemento {x} não está no array.")

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)

print(pares)

numeros = [1, 2, 3, 4, 5]
quadrados = [n ** 2 for n in numeros]
print(quadrados)

numeros = [10, 20, 30, 30, 40, 30, 50]
x = 30
numeros = [n for n in numeros if n != x]
print(numeros)

import random


numeros = [10, 20, 30, 20, 40, 50]

print("Lista original:", numeros)

# ------------------ BUSCA ------------------
print("\n=== BUSCA ===")

print("20 está na lista?", 20 in numeros)
if 30 in numeros:
    print("Índice do 30:", numeros.index(30))


print("Quantidade de vezes que 20 aparece:", numeros.count(20))

# ------------------ REMOÇÃO ------------------
print("\n=== REMOÇÃO ===")


if 20 in numeros:
    numeros.remove(20)
    print("Depois do remove(20):", numeros)

removido = numeros.pop()
print("Elemento removido com pop():", removido)
print("Depois do pop():", numeros)


temp = numeros.copy()
temp.clear()
print("Depois do clear():", temp)

# ------------------ ORDENAÇÃO ------------------
print("\n=== ORDENAÇÃO ===")

numeros = [30, 10, 50, 20]
print("Antes de ordenar:", numeros)


numeros.sort()
print("Depois do sort():", numeros)

numeros2 = [30, 10, 50, 20]
print("Com sorted():", sorted(numeros2))
print("Original após sorted():", numeros2)

# ------------------ EMBARALHAMENTO ------------------
print("\n=== EMBARALHAMENTO ===")

numeros = [1, 2, 3, 4, 5]
random.shuffle(numeros)  # no local
print("Depois do shuffle():", numeros)

numeros2 = [1, 2, 3, 4, 5]
embaralhada = random.sample(numeros2, len(numeros2))  # nova lista embaralhada
print("Com sample():", embaralhada)
print("Original após sample():", numeros2)
