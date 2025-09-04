import time

def tiene_duplicados_lineal(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False

#Pruebas con diferentes tamaños de arreglos
sizes = [0, 0, 100000]

for n in sizes:
    arr = list(range(n)) #Arreglo sin duplicados para forzar el peor caso

    start_time = time.time()
    tiene_duplicados_lineal(arr)
    end_time = time.time()

    print(f"Búsqueda de duplicados en un arreglo de {n} elementos: {end_time - start_time:.6f} segundos")