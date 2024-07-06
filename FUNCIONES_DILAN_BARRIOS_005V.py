def menu():
    print("""1. Registrar Cliente
2. Listar Clientes Registrados
3. Registrar Compra
4. Listar Compras de un Cliente
5. Salir del programa""")
    
def registrar_cliente(bd):
    nombre = input("Ingrese el nombre del cliente: ").upper()
    apellido = input("Ingrese el apellido del cliente: ").upper()
    correo = input("Ingrese el correo electronico del cliente: ").upper()
    id_cliente = len(bd) + 1
    bd.append(
        {
            "nombre": nombre,
            "apellido": apellido,
            "correo": correo,
            "ID": id_cliente,
            "compra": []
        }
        )
    print("\n!El cliente se agrego exitosamente¡\n")

def listar_clientes(bd):
    print("\nLos clientes registrados son:\n")
    print("ID Nombre\t\tCorreo")
    for cliente in bd:
        print(f'{cliente["ID"]} {cliente["nombre"]} {cliente["apellido"]}\t\t{cliente["correo"]}')
    print("\n!Lista creada con exito¡\n")
def registrar_compra(bd):
    id = int(input("Ingrese el ID del cliente: "))
    for cliente in bd:
        if cliente["ID"] == id:
            monto_total = 0
            fecha = input("ingrese la fecha de su compra (AAAA-MM-DD): ")
            monto_total = int(input("Ingrese el total de su compra: "))
            puntos_compra = monto_total * 0.01
            cliente["compra"].append(
                {
                    "fecha": fecha,
                    "monto": monto_total,
                    "puntos": puntos_compra
                }
            )
    print("\n!Compra agregada con exito¡\n")

def guardar_compra(bd):
    id = int(input("Ingrese el ID del cliente: "))
    for cliente in bd:
        if cliente["ID"] == id:
            texto = f'ID CLIENTE: {id}\n\nNOMBRE CLIENTE:{cliente["nombre"]} {cliente["apellido"]}\n'
            texto += f'Fecha Compra\tMonto total\tPuntos\n'
            p_totales = 0
            for compra in cliente["compra"]:
                texto += f'{compra["fecha"]}\t\t{compra["monto"]}\t\t{compra["puntos"]}\n'
                p_totales += compra["puntos"]
            texto += f'\nPUNTOS TOTALES A CANJEAR: {p_totales} Pesos'
            with open(f"RESUMEN_CLIENTE_ID_{id}.txt","w", encoding= 'utf-8') as archivo:
                archivo.write(texto)
                print("\n!Archivo creado¡\n")
            break
        else:
            print(f"El ID {id} no se encuentra en la BD.")