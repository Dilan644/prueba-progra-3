from FUNCIONES_DILAN_BARRIOS_005V import *
BD = []
print("!Bienvenido a TODOAHORRO¡")
while True:
    menu()
    op1 = int(input("Ingrese una opcion: "))
    if op1 == 1:
        registrar_cliente(BD)
    elif op1 == 2:
        listar_clientes(BD)
    elif op1 == 3:
        registrar_compra(BD)
    elif op1 == 4:
        guardar_compra(BD)
    elif op1 == 5:
        print("Adios")
        break
    else:
        print("la opcion ingresada no existe")