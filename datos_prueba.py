import pandas as pd
import numpy as np
import os
import random

#Configuración
periodo_actual = "2026 1A"
ruta_entrada = os.path.join('Datos BS.CSV', periodo_actual)
os.makedirs(ruta_entrada, exist_ok=True)

#Crear materias
materias = ['M_I', 'M_II', 'M_III', 'M_IV', 'M_V','M_VI','M_VII','M_VIII','M_IX','M_X']

#listas de nombres y apellidos
nombres_masculinos = ['Juan', 'Carlos', 'Luis', 'Pedro', 'Diego', 'Roberto', 'armando', 'Gonzálo']
nombres_femeninos = ['MARÍA', 'Ana', 'SOFÍA', 'Lucía', 'Valentina', 'CLARA', 'Isabella', 'Cámila']
apellidos = ['Pérez', 'Gómez', 'Rodriguez', 'Lopez', 'Martinez', 'SANCHEZ', 'Díaz', 'ÁLVAREZ', 'FERNANDEZ', 'GARCIA','iñariitú']

def generar_nombre_sucio():
    # 2. género al azar
    if random.random() < 0.5:
        lista_uso = nombres_masculinos
    else:
        lista_uso = nombres_femeninos
    
    # 3. nombres vienen de una misma lista
    n = f"{random.choice(lista_uso)} {random.choice(lista_uso)}"
    
    # apellidos generales
    a = f"{random.choice(apellidos)} {random.choice(apellidos)}"
    
    if random.random() < 0.7:
        a = a.replace('a', 'á').replace('e', 'é')
    return a, n

for materia in materias:
    data = []
    num_estudiantes = random.randint(20, 50)

    for i in range(num_estudiantes):
        id_estudiante = f"#{random.randint(1000000000, 1999999999)}"
        apellido, nombre = generar_nombre_sucio()

        #Generar notas aletaorias
        nota1 = round(random.uniform(0, 5), 1)
        nota2 = round(random.uniform(0, 5), 1)

        #estructura de columnas según materia
        fila={
            'ID': id_estudiante,
            'Last Name': apellido,
            'First Name': nombre,
            'Grade 1': nota1    
        }
        # Materias que tienen 2 notas 
        if materia not in ['M_VI', 'M_VII', 'M_IX', 'M_X']: 
            fila['Grade 2'] = nota2   
            
        data.append(fila)

    # Crear DataFrame y guardar como CSV
    df_mock = pd.DataFrame(data)
    nombre_archivo =os.path.join(ruta_entrada, f'{materia}.csv')
    df_mock.to_csv(nombre_archivo, index=False, encoding='utf-8-sig')
    print(f"Archivo creado: {nombre_archivo} con {num_estudiantes} estudiantes.")

    print(f"Datos de prueba para {materia} generados exitosamente.\n")
