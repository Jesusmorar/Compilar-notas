import pandas as pd
import os
#Establecer ruta de destino
periodo_actual="2026 1A"
ruta_entrada= os.path.join('Datos BS.CSV',periodo_actual)
carpeta_destino= 'Resultados'
nombre_archivo= 'Notas_primer_corte.xlsx'
ruta_final= os.path.join(carpeta_destino,nombre_archivo)

#crear lista de materias
materias = ['M_I', 'M_II', 'M_III', 'M_IV', 'M_V','M_VI','M_VII','M_VIII','M_IX','M_X']

#función para quitar tildes manteniendo la ñ

def limpiar_tildes(texto):
    if not isinstance (texto,str):return texto
    reemplazos= {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
    'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U'}
    for acento, limpio in reemplazos.items():
        texto=texto.replace(acento, limpio)
    return texto

#utilizar pd.excel para crear un solo archivo con varias páginas
with pd.ExcelWriter(ruta_final, engine='xlsxwriter') as writer:

    for materia in materias:   
        try:
            archivo_leer= os.path.join(ruta_entrada, f'{materia}.csv')
            df= pd.read_csv(archivo_leer)

            col_id= df.columns[0]
            col_lastname= df.columns[1]
            col_firsname= df.columns[2]
            col_grade1= df.columns[3]
            col_grade2= df.columns[4] if len(df.columns)> 4 else None

            df= df.fillna(0)
            df[col_id] = df[col_id].astype(str).str.replace('#', '',regex=False)
            df[col_id] = df[col_id].astype(int)
            
            #aplicar fución creada
            df[col_lastname]= df[col_lastname].apply(limpiar_tildes).str.title()
            df[col_firsname]= df[col_firsname].apply(limpiar_tildes).str.title()
            
            nombre_completo= df[col_lastname]+" "+df[col_firsname]
            df.insert(1,'Nombre completo',nombre_completo)
            df= df.drop(columns=[col_lastname,col_firsname])

            #definir notas
            if materia== 'M_VIII':
                df['Grade 1st hurdle'] = ((df[col_grade1]*0.4)+(df[col_grade2]*0.6)).round(2)
            
            elif materia in ['M_VI', 'M_VII', 'M_IX', 'M_X']:
                df['Grade 1st hurdle'] = df[col_grade1].round(2)
                
            else:
                df['Grade 1st hurdle'] = ((df[col_grade1]*0.5)+(df[col_grade2]*0.5)).round(2)
            
            #limpieza de columnas
            columnas_finales = [col_id, 'Nombre completo', col_grade1]
            if col_grade2 in df.columns and materia not in ['CAR', 'IE', 'PNL', 'PV']:
                columnas_finales.append(col_grade2) # type: ignore
            columnas_finales.append('Grade 1st hurdle')
            df = df[columnas_finales]
            
            #organizar alfabeticamente
            df_sorted = df.sort_values(by='Nombre completo', ascending=True)

            #exportar a excel
            df_sorted.to_excel(writer,sheet_name=materia, index=False)

            worksheet= writer.sheets[materia]
            ancho_nombre= df_sorted['Nombre completo'].astype(str).map(len).max()+1
            worksheet.set_column(1,1, ancho_nombre)
            worksheet.set_column(0,0, 12)

            print(f" Hoja '{materia}' añadida al archivo.")
        
        except Exception as e:
            print (f"No se pudo procesar la materia{materia}:{e}")

print("\n---¡Arhivo 'Notas_primer_corte.xlsx' generado con todas las hojas---")