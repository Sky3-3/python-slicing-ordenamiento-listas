# Proyecto Python: Operaciones Avanzadas, Ordenamiento y Rebanado de Listas

Este repositorio contiene un proyecto práctico desarrollado en Python enfocado en la aplicación de métodos avanzados para la gestión de listas mutables. El script implementa lógicas de ordenamiento interno, funciones de medición de longitud, conteo de frecuencias específicas de elementos y el uso de técnicas de Slicing (rebanado) mediante índices positivos y negativos para segmentar conjuntos de datos médicos.

---

## Código Python del Proyecto

El programa realiza una serie de análisis estadísticos y de segmentación sobre colecciones emparejadas de costos de seguros y pacientes:

```python
# Colecciones de datos de entrada independientes
names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul", "Priscilla"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0, 8320.0]

# Consolidación de registros emparejados (Costo, Nombre)
medical_records = list(zip(insurance_costs, names))

# Medición y extracción del estado inicial
num_medical_records = len(medical_records)
first_medical_record = medical_records[0]

# Ordenamiento in-place (Por defecto evalúa el primer elemento de la tupla: el costo)
medical_records.sort()

# Segmentación por Slicing avanzado
cheapest_three = medical_records[:3]     # Primeros tres registros (menor costo)
priciest_three = medical_records[-3:]    # Últimos tres registros (mayor costo)
ocurrences_paul = names.count("Paul")    # Conteo de frecuencia de un elemento específico

# Impresión de métricas principales en consola
print("There are " + str(num_medical_records) + " medical records.")
print("Here is the first medical record: " + str(first_medical_record))
print("Here are the medical records sorted by insurance cost: " + str(medical_records))
print("Here are the three cheapest insurance costs in our medical records: " + str(cheapest_three))
print("Here are the three most expensive insurance costs in our medical records: " + str(priciest_three))
print("There are " + str(ocurrences_paul) + " individuals with the name Paul in our medical records.")

# --- Práctica Extra: Ordenamiento alfabético y corte intermedio ---
records_medical_order = list(zip(names, insurance_costs))
records_medical_order.sort()  # Al iniciar con 'names', ordena alfabéticamente
middle_five_records = records_medical_order[3:7]  # Extracción de la sección central

print("Registro medicos ordenados " + str(records_medical_order))
print("Estos son los 5 registros medicos del medio " + str(middle_five_records))

```

---

## Simulación de la Segmentación de Datos (Slicing)

Al ejecutar el método `.sort()`, los elementos se reordenan de menor a mayor. Las técnicas de rebanado extraen subconjuntos específicos de la lista basándose en sus posiciones indexadas.

### 1. Extracción de Extremos en Lista Ordenada por Costo (`medical_records`)

| Índice Lógico | Valor del Costo | Paciente Asociado | Segmento Asignado |
| --- | --- | --- | --- |
| `[0]` | 2750.0 | Nikita | Pertenece a `cheapest_three` (`[:3]`) |
| `[1]` | 4816.0 | Sara | Pertenece a `cheapest_three` (`[:3]`) |
| `[2]` | 5054.0 | Paul | Pertenece a `cheapest_three` (`[:3]`) |
| ... | ... | ... | ... |
| `[-3]` | 12064.0 | Paul | Pertenece a `priciest_three` (`[-3:]`) |
| `[-2]` | 13262.0 | Mohamed | Pertenece a `priciest_three` (`[-3:]`) |
| `[-1]` | 14724.0 | Valentina | Pertenece a `priciest_three` (`[-3:]`) |

### 2. Extracción Central en Lista Ordenada Alfabéticamente (`records_medical_order`)

Al aplicar el rebanado `[3:7]`, el intérprete incluye el índice de inicio (3) pero excluye el índice de parada (7), devolviendo exactamente 4 registros intermedios:

| Índice del Segmento | Nombre (Criterio de orden) | Costo Vinculado | Estado en `middle_five_records` |
| --- | --- | --- | --- |
| `[3]` | Emily | 6072.0 | Incluido (Posición inicial) |
| `[4]` | Jide | 5360.0 | Incluido |
| `[5]` | Mohamed | 13262.0 | Incluido |
| `[6]` | Nikita | 2750.0 | Incluido (Posición final) |
| `[7]` | Paul | 5054.0 | Excluido por límite de rango |

---

## Conceptos Técnicos Aplicados

* **Método `.sort()**`: Operación que reordena los elementos de una lista de manera interna (*in-place*). Cuando la lista contiene tuplas, el ordenamiento se realiza comparando los primeros elementos de cada tupla de forma secuencial.
* **Slicing (Rebanado `[inicio:fin]`)**: Sintaxis que permite extraer una subdivisión de una lista sin modificar la estructura original. Omitir el inicio (`[:3]`) indica que se arranca desde la posición cero. Utilizar valores negativos (`[-3:]`) instruye al motor a contar desde el final de la lista hacia atrás.
* **Método `.count()**`: Función integrada que recorre la colección para realizar un conteo lineal de las ocurrencias que coinciden de forma exacta con el objeto pasado como argumento.
* **Función `len()**`: Operador que devuelve un número entero que representa la cantidad total de elementos contenidos dentro de una estructura iterable.


¿Te parece bien si ahora pasamos a armar las listas temáticas en tu cuenta de GitHub y el repositorio indexador central de tu perfil?

```
