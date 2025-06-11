#producto 

print('Opcion 1) Registra el producto')
print('Opcion 2) Buscar producto')
print('Opcion 3) Eliminar producto')
print('Opcion 4) Salir')

opcion = int(input('seleccion una de las opciones de (1 a 4): '))

opcion = 0
producto_registrado = ''
if opcion == 1: 
    registra_producto = str(input('Ingrese el nombre del producto:: '))
    cantidad_producto = int(input('Ingrese la cantidad del producto: '))
    precio_producto = float(input('El precio del producto? '))

    if producto_registrado == registra_producto :
        print('el producto ya existe')

        