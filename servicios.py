from helpers import generate_ID ,string_input, int_input, float_input

def agregar_producto (lista):
    product_info = {
        "ID" : generate_ID(),
        "nombre" : string_input("Nombre del producto: "),
        "cantidad" : int_input("Cantidad del producto: "),
        "precio" : float_input("Precio del producto: "),
    }
    lista.append(product_info)
    return product_info

def mostrar_inventario (lista):
    return print(lista)

def buscar_producto (lista):
    search_product = string_input("Nombre del producto: ")
    for product in lista:
        if product["nombre"] == search_product:
            print(f"Producto encontrado:\n{product}")
        return product

def actualizar_producto(lista):
    product_found = buscar_producto(lista)
    input_key_answer = string_input("Clave del producto: ")
    input_product_new_value = string_input("Nombre nuevo del producto: ")
    product_found[input_key_answer] = input_product_new_value   
    return product_found

def eliminar_producto (lista):
    product_to_delete = string_input("Nombre del producto a eliminar")
    for product in lista:    
        if product["nombre"] == product_to_delete:
            print(product_to_delete)
            lista.remove(product)
    print(lista)
    return product_to_delete

def calcular_estadisticas (lista):
    products_amount = 0
    price_all_prodcuts = 0
    product_more_expensive = 0
    product_major_stock = 0
    for product in lista:
        products_amount += product["cantidad"]
        price_all_prodcuts += product["cantidad"] * product["precio"]
        if product["precio"] > product_more_expensive:
            product_more_expensive = product["precio"]        
        if product["cantidad"] > product_major_stock:
            product_major_stock = product["cantidad"] 

    return [products_amount,price_all_prodcuts,product_more_expensive,product_major_stock,]