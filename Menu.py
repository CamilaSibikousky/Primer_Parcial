
# Funciones auxiliares (ya implementadas)

def es_entero(valor):
    """Valida si un string es un número entero positivo"""
    if valor == "":
        return False
    for caracter in valor:
        if caracter not in "0123456789":
            return False
    return True

def cargar_matrix_notas():
    """Carga la matriz de notas con validaciones"""
    # (Implementación previa)
    pass

def porcentaje_aprobados(matriz):
    """Calcula porcentaje de aprobados por alumno"""
    # (Implementación previa)
    pass

def mejor_promedio(matriz):
    """Encuentra al alumno con mejor promedio """
    # (Implementación previa)
    pass

def buscar_nota(matriz, nota_buscada):
    """Busca una nota en la matriz"""
    # (Implementación previa)
    pass


# Menú principal


def main():
    matriz_notas = []  # Matriz que almacenará todas las notas
    notas_cargadas = False  # Bandera para verificar si hay datos cargados

    while True:
        print(" MENÚ PRINCIPAL ".center(50, "="))
        print("1. Cargar notas de alumnos")
        print("2. Calcular porcentaje de aprobados")
        print("3. Encontrar mejor promedio")
        print("4. Buscar nota específica")
        print("5. Salir")
        print("="*50)

        opcion = input("Seleccione una opción (1-5): ")

        # Validación básica de la opción
        if not es_entero(opcion) or int(opcion) not in range(1, 6):
            print("¡Error! Ingrese un número entre 1 y 5.")
            continue

        opcion = int(opcion)

        # Opción 1: Cargar notas
        if opcion == 1:
            matriz_notas = cargar_matrix_notas()
            notas_cargadas = True
            print("\n¡Notas cargadas correctamente!")

        # Opciones 2-4 requieren notas cargadas
        elif not notas_cargadas:
            print("¡Primero debe cargar las notas (Opción 1)!")
            continue

        # Opción 2: Porcentaje de aprobados
        elif opcion == 2:
            porcentaje_aprobados(matriz_notas)

        # Opción 3: Mejor promedio
        elif opcion == 3:
            indice, promedio = mejor_promedio(matriz_notas)
            print(f"\nEl mejor promedio es del Alumno {indice + 1}: {promedio:.2f}")

        # Opción 4: Buscar nota
        elif opcion == 4:
            while True:
                nota = input("Ingrese la nota a buscar (1-10): ")
                if es_entero(nota):
                    nota = int(nota)
                    if 1 <= nota <= 10:
                        break
                    else:
                        print("¡La nota debe estar entre 1 y 10!")
                else:
                    print("¡Ingrese un número entero válido!")

            resultados = buscar_nota(matriz_notas, nota)
            if resultados:
                print("\nPosiciones donde aparece la nota:")
                for fila, columna in resultados:
                    print(f"- Alumno {fila + 1}, Examen {columna + 1}")
            else:
                print("\nLa nota no se encontró en la matriz.")

        # Opción 5: Salir
        elif opcion == 5:
            print("\n¡Programa terminado!")
            break

# Ejecutar el programa
if __name__ == "__main__":
    main()