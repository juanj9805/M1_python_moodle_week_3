from servicios import agregar_producto, mostrar_inventario, buscar_producto, actualizar_producto, eliminar_producto, calcular_estadisticas
from helpers import principal_menu_input, options

list_inventory = [
    {'ID': 'a087a3ae-f2d7-45e0-89ba-de5b4841d1bq', "nombre": "tennis", "precio": 90000, "cantidad": 10},
    {'ID': 'a087a3ae-f2d7-45e0-89ba-de5b4841d2bw', "nombre": "shirt", "precio": 40000, "cantidad": 50},
    {'ID': 'a087a3ae-f2d7-45e0-89ba-de5b4841d3be', "nombre": "cap", "precio": 35000, "cantidad": 20},
    {'ID': 'a087a3ae-f2d7-45e0-89ba-de5b4841d4br', "nombre": "jean", "precio": 80000, "cantidad": 60},
    {'ID': 'a087a3ae-f2d7-45e0-89ba-de5b4841d5bt', "nombre": "necklace", "precio": 300000, "cantidad": 8},
    {'ID': 'a087a3ae-f2d7-45e0-89ba-de5b4841d6by', "nombre": "watch", "precio": 500000, "cantidad": 5},
]

follow = True

while follow:
    principal_choice = principal_menu_input()
    if principal_choice == 1:
        agregar_producto(list_inventory)
    elif principal_choice == 2:
        mostrar_inventario(list_inventory)
    elif principal_choice == 3:
        buscar_producto(list_inventory)
    elif principal_choice == 4:
        actualizar_producto(list_inventory)
    elif principal_choice == 5:
        eliminar_producto(list_inventory)
    elif principal_choice == 6:
        follow_analitics = True
        while follow_analitics:
            statistics_data = calcular_estadisticas(list_inventory)
            choice = options()
            if choice == 1:
                print(statistics_data[0])
            elif choice == 2:
                print(statistics_data[1])
            elif choice == 3:
                print(statistics_data[2])
            elif choice == 4:
                print(statistics_data[3])
            elif choice == 5:
                follow_analitics = False
    elif principal_choice == 7:
        follow = False