def imprimir_resultados():
    print('Resultados hasta la fecha:')
    try:
        with open("data.txt", "r") as read_file:
            print(read_file.read())
    except FileNotFoundError:
        print("No hay resultados aún. El archivo 'data.txt' no existe.")

def ingresar_comentarios():
    while True:
        point = obtener_puntuacion()
        comment = obtener_comentario()
        guardar_comentario(point, comment)
        break

def obtener_puntuacion():
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5:')
        point = input()
        if point.isdecimal():
            point = int(point)
            if 1 <= point <= 5:
                return point
            else:
                print('Por favor, introduzca un valor entre el 1 y 5.')
        else:
            print('Por favor, introduzca el punto de evaluación como un número.')

def obtener_comentario():
    print('Introduzca sus comentarios:')
    return input()

def guardar_comentario(point, comment):
    post = f'Punto: {point}, Comentario: {comment}\n'
    with open("data.txt", 'a') as file_pc:
        file_pc.write(post)

if __name__ == "__main__":
    while True:
        print("Seleccione el proceso que desea aplicar:")
        print("1: Ingresar puntos de evaluación y comentarios")
        print("2: Comprueba los resultados obtenidos hasta ahora.")
        print("3: Salir")
        opcion = input()
        if opcion == '1':
            ingresar_comentarios()
        elif opcion == '2':
            imprimir_resultados()
        elif opcion == '3':
            break
        else:
            print("Opción no válida, por favor seleccione 1, 2 o 3.")
