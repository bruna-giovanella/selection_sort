
lista = input('informe uma lista de números (separados por ,): ')
lista = lista.replace(' ','')
lista = lista.split(',')
lista = [int(x) for x in lista]

def insertion_sort(lista):

    for i in range(len(lista)):
        valor = lista[i]
        indice_anterior = i - 1

        while indice_anterior >= 0 and lista[indice_anterior] > valor:
            lista[indice_anterior+1] = lista[indice_anterior]
            indice_anterior -= 1
            lista[indice_anterior+1] = valor
    return lista

print(insertion_sort(lista))  


