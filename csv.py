import csv
from helpers import generate_ID

header = ["ID", "nombre", "precio", "cantidad"]

def guardar_csv(lista, path, include_header=True):
    try:
        with open(path, "w", newline="") as f:
            writer = csv.writer(f)
            if include_header:
                writer.writerow(header)
            for product in lista:
                writer.writerow([
                    product["ID"],
                    product["nombre"],
                    product["precio"],
                    product["cantidad"]
                ])
        print(f"Producto cargado con exito: {path}")
    except Exception as e:
        print("Error con el archivo:", e)

def cargar_csv(path):
    lista = []
    with open(path, "r") as f:
        reader = csv.reader(f)
        next(reader, None)
        for fila in reader:
            product_id, name, price, quantity = fila
            lista.append({
                    "ID" : generate_ID(),
                    "nombre": name,
                    "precio": price,
                    "cantidad": quantity
                })
    return lista
