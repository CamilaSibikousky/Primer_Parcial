# Función para verificar si un string es un número entero positivo
def es_entero(valor):
    """
    Verifica si el string 'valor' contiene SOLO dígitos numéricos (0-9).
    Retorna True si es entero positivo o False si no.
    """
    # Paso 1: Si el string está vacío, no es un número
    if valor == "":
        return False
    
    # Paso 2: Revisa cada carácter del string uno por uno
    for caracter in valor:
        # Si algún carácter no es un dígito (0-9), retorna False
        if caracter not in "0123456789":
            return False
    
    # Si todos los caracteres son dígitos, retorna True
    return True


# Función principal para cargar la matriz de notas
def cargar_matrix_notas():
    """
    Carga una matriz donde:
    - Cada fila es un alumno.
    - Cada columna es una nota de examen.
    Valida que las notas sean enteros entre 1 y 10.
    """

    # Paso 1: Pedir cantidad de alumnos (n)
    while True:
        n = input("Ingrese la cantidad de alumnos: ")
        # Verificar si 'n' es un número entero
        if es_entero(n):
            n = int(n)  # Convertir a entero
            # Asegura que sea mayor a cero
            if n > 0:
                break  # Sale del bucle si es válido
            else:
                print("Error!!! Debe  ser mayor a 0.")
        else:
            print("Error!!! Ingrese un número entero válido.")

    # Paso 2: Pedir cantidad de exámenes (m) 
    while True:
        m = input("Ingrese la cantidad de exámenes por alumno: ")
        if es_entero(m):
            m = int(m)
            if m > 0:
                break
            else:
                print("Error!!! Debe ser mayor a 0.")
        else:
            print("Error!!! Ingrese un número entero válido.")

    # Paso 3: Crear la matriz de notas 
    matriz = []  # Matriz vacía para guardar todas las notas

    # Para cada alumno (fila):
    for i in range(n):
        # Crear una fila de 'm' ceros
        fila = [0] * m
        print(f"\nAlumno {i + 1}:")

        # Para cada examen (columna):
        for j in range(m):
            while True:
                nota = input(f"Ingrese la nota del examen {j + 1}: ")
                # Verificar si la nota es un número entero
                if es_entero(nota):
                    nota_int = int(nota)  # Convierte a entero
                    # Validar que esté entre 1 y 10
                    if 1 <= nota_int <= 10:
                        fila[j] = nota_int  # Guarda nota en la posición j
                        break  # Esto hace que salga del bucle while
                    else:
                        print("La nota debe estar entre 1 y 10.")
                else:
                    print("Error!!! Ingrese un número entero.")

        # Agregar la fila del alumno a la matriz
        matriz = matriz + [fila]

    # Retornar la matriz completa
    return matriz



