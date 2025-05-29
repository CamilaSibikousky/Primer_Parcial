def porcentaje_aprobados(matriz):
    """
    Calcula el porcentaje de exámenes aprobados (nota >= 6) por alumno.
    Recibe la matriz de notas y muestra un resumen individual.
    """
    # Paso 1: Recorrer cada alumno (fila) en la matriz
    for i in range(len(matriz)):
        alumno = matriz[i]  # Notas del alumno actual
        aprobados = 0       # Contador de exámenes aprobados
        
        # Paso 2: Contar cuántos exámenes aprobó el alumno
        for nota in alumno:
            if nota >= 6:
                aprobados += 1  # Incrementar contador si la nota es >= 6
        
        # Paso 3: Calcular el porcentaje de aprobación
        total_examenes = len(alumno)
        if total_examenes > 0:  # Evitar división por cero
            porcentaje = (aprobados / total_examenes) * 100
        else:
            porcentaje = 0.0  # Si no hay exámenes, porcentaje es 0%
        
        # Paso 4: Mostrar el resultado para el alumno actual
        print(f"Alumno {i + 1}: Aprobó {aprobados} de {total_examenes} exámenes → {porcentaje:.2f}%")