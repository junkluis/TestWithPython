


''' Funcion quick_sort
    La funcion recibe un arreglo de numeros enteros
    y devuelve el arreglo ordenado de forma ascendente.
    @autor: Luis Zuñiga
'''
def quick_sort(array):
    less = []
    equal = []
    greater = []

    if type(array) is str:
        return "No puedo orderna palabras"

    elif type(array) is int:
        return -1

    elif type(array) is list:

        if len(array) > 1:
            pivot = array[0]
            for x in array:
                if x < pivot:
                    less.append(x)
                if x == pivot:
                    equal.append(x)
                if x > pivot:
                    greater.append(x)
            return quick_sort(less)+equal+quick_sort(greater)
        else:
            return array



#Usando mi funcion para ordenar arreglos
