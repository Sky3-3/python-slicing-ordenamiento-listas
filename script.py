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
