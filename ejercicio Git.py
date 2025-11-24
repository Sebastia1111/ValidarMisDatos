#----------------------------FUNCIONALES----------------------------
def mostrar_asientos(asientos): #1)
    contador = 0
    for i, j in asientos.items():
        if j == '❌':
            print(f'[{j}]', end= ' ') # si esta ocupado imprime el valor
        else:
            print(f'[{i}]', end= ' ') # si esta disponible imprime la clave
        contador += 1
        if contador % 5 == 0: # si es multiplo de 5 se salta el reglon
            print()

def registrar_cliente(clientes, nombre, rut, telefono): #2)
    clientes.append({
        'Nombre del cliente': nombre,
        'RUT': rut,
        'Teléfono': telefono
    })
def comprar_entrada(asiento): #3)
    if not asiento in asientos:
        return False
    if asientos[asiento] == '❌':
        return False
    else:
        asientos.update({
            asiento: '❌'
        })
    return True
def mostrar_historial_ventas(): #4)
    if len(historial_ventas) == 0:
        print('No se ha realizado ninguna venta.')
        return False
    print("\n--------------VENTAS--------------\n")
    for i in historial_ventas:
        print(f"RUT: {i['rut']}\n"
              f"Asiento: {i['asiento']}\n"
              f"Precio: ${i['precio']}")
    print(f'\nTotal Vendido: ${precio_acumulado}')
def buscar_cliente(cliente, busqueda): #5)
    for i in cliente:
        if i['RUT'] == busqueda:
            for j in i.values():
                print(j)
def cancelar_reserva(): #6)
    return
#---------------------------NO FUNCIONALES---------------------------
def validar_rut(rut):
    if len(rut) == 1:
        return False
    if rut[-2] != '-': # [-2] es la penultima posición: XXXX-X
        return False
    if len(rut) != 10: #10 ya que el '-' también cuenta
        return False
    for i in rut[:8]: # [:8] significa del elemento 8 hacia la izquierda
        if i < '0' or i > '9': # validar que sean números
            return False
    DV = rut[-1]
    es_K = DV == 'K'
    es_numero = (DV >= '0' and DV <= '9')
    if not (es_numero or es_K):
        return False
    return True
    
def validar_texto(texto):
    if texto == '':
        return False # si no tiene nada -> False
    for i in texto:
        if i >= 'A' and i <= 'Z': # Acepta mayusculas
            continue
        if i >= 'a' and i <= 'z': # Acepta minusculas
            continue
        return False # si no es letra -> False
    return True
        
def validar_numero(texto_numero):
    if texto_numero == '':
        return False
    for i in texto_numero:
        if i < '0' or i > '9':
            return False
    return True


asientos = {
    'A1': '✅', 'A2': '✅', 'A3': '✅', 'A4': '✅', 'A5': '✅', 
    'B1': '✅', 'B2': '✅', 'B3': '✅', 'B4': '✅', 'B5': '✅', 
    'C1': '✅', 'C2': '✅', 'C3': '✅', 'C4': '✅', 'C5': '✅', 
    'D1': '✅', 'D2': '✅', 'D3': '✅', 'D4': '✅', 'D5': '✅', 
    'E1': '✅', 'E2': '✅', 'E3': '✅', 'E4': '✅', 'E5': '✅'
}
asientos_ocupados = {}

clientes = []
historial_ventas = []
lista_rut = []

PRECIO = 3500
entradas_vendidas = 0
precio_acumulado = 0
while True:
    print('\n---------------MENU---------------\n' \
    '1. Mostrar asientos disponibles\n' \
    '2. Registrar cliente\n' \
    '3. Comprar entrada\n' \
    '4. Mostrar historial de ventas\n' \
    '5. Buscar cliente por RUT\n' \
    '6. Cancelar reserva\n' \
    '7. Salir\n')
    opcion_menu = int(input(' >> '))
#----------------------------------------------1----------------------------------------------
    if opcion_menu == 1:
        mostrar_asientos(asientos)
        continue

#----------------------------------------------2----------------------------------------------
    elif opcion_menu == 2:
        nombre_cli = input('Escriba su nombre: ').capitalize()
        while not validar_texto(nombre_cli): # si NO retorna True y retorna False
            print('Error. Por favor utilice solo letras sin espacios.')
            nombre_cli = input('Escriba su nombre: ')
        rut_cli = input('Escriba su RUT en el siguiente formato:\n' \
                        '             XXXXXXXX-X\n' \
                        ' >> ').upper()
        while not validar_rut(rut_cli):
            print('Error. Por favor escriba el RUT acorde al formato pedido.')
            rut_cli = input(' >> ').upper()
        lista_rut.append(rut_cli)
        numero_telefono = input('Ingrese su número de teléfono (9 dígitos): ')
        while not validar_numero(numero_telefono) or len(numero_telefono) != 9:
            print('Por favor. Ingrese un número válido sin letras y de 9 dígitos.')
            numero_telefono = input(' >> ')
        registrar_cliente(clientes, nombre_cli, rut_cli, numero_telefono)
        continue

#----------------------------------------------3----------------------------------------------
    elif opcion_menu == 3:
        comparar_rut = input('Ingrese el RUT del cliente: ')
        while not validar_rut(comparar_rut):
            print('Error. Por favor escriba el RUT acorde al formato pedido.')
            comparar_rut = input(' >> ')
        while not comparar_rut in lista_rut:
            print('RUT no encontrado en nuestros clientes.')
            comparar_rut = input('Por favor escriba otro RUT: ')
        print('Lista de asientos disponibles:')
        mostrar_asientos(asientos)
        asiento_cli = input('Ingrese el asiento deseado: ').upper()
        while not comprar_entrada(asiento_cli):
            asiento_cli = input('Por favor. Ingrese un asiento válido: ').upper()
        historial_ventas.append({
            'rut': comparar_rut,
            'asiento': asiento_cli,
            'precio': PRECIO
        })
        entradas_vendidas += 1
        precio_acumulado += PRECIO
        continue

#----------------------------------------------4----------------------------------------------
    elif opcion_menu == 4:
        mostrar_historial_ventas()
        continue

#----------------------------------------------5----------------------------------------------
    elif opcion_menu == 5:
        comparar_rut = input('Ingrese el RUT del cliente: ')
        while not validar_rut(comparar_rut):
            print('Error. Por favor escriba el RUT acorde al formato pedido.')
            comparar_rut = input(' >> ')
        while not comparar_rut in lista_rut:
            print('RUT no encontrado en nuestros clientes.')
            comparar_rut = input('Por favor escriba otro RUT: ')
        buscar_cliente(clientes, comparar_rut)
        continue

#----------------------------------------------6----------------------------------------------
    elif opcion_menu == 6:
        continue

#----------------------------------------------7----------------------------------------------
    elif opcion_menu == 7:
        break