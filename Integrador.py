archivo="paises.csv"

def inicializar_archivo():
    f = open(archivo, "a", encoding="utf-8")
    f.close()
    
    with open (archivo, "r", encoding="utf-8") as f:
        lineas = f.readlines()
        
        if len(lineas) == 0:
            with open(archivo, "w", encoding="utf-8") as fw:
                fw.write("nombre,poblacion,superficie,continente\n")
            print("Archivo paises.csv creado correctamente")
        else:
            print("Archivo paises.csv encontrado")

def cargar_paises():

    paises=[]
    
    with open(archivo, "r", encoding="utf-8") as f:
        encabezado = next(f)
        for linea in f:
            linea = linea.strip()
            if linea == "":
                continue

            partes = linea.split(",")
            if len(partes) != 4:
                print(f"Línea con formato incorrecto: {linea}")
                continue

            nombre, poblacion, superficie, continente = partes

           
            if not poblacion.isdigit() or not superficie.isdigit():
                print(f"Error en los datos de: {nombre}")
                continue

            pais = {
                "nombre": nombre,
                "poblacion": int(poblacion),
                "superficie": int(superficie),
                "continente": continente
            }

            paises.append(pais)

    return paises

def guardar_paises(paises):

    with open (archivo,"w", encoding="utf-8") as f:
        f.write("nombre,poblacion,superficie,continente,\n")
        for p in paises:
            linea= f"{p['nombre']},{p['poblacion']},{p['superficie']},{p['continente']}\n"
            f.write(linea)

#DARIO:

# def agregar_paises
# def actualizar_pais
# def buscar_pais

def mostrar_lista(paises):
    
    for p in paises:
        print(f"{p['nombre']} - {p['poblacion']} hab - {p['superficie']} km² - {p['continente']}")

def obtener_nombre(p):
    return p["nombre"]

def obtener_poblacion(p):
    return p["poblacion"]

def obtener_superficie(p):
    return p["superficie"]

def ordenar_por_nombre(paises):
    paises.sort(key=obtener_nombre)
    mostrar_lista(paises)


def ordenar_por_poblacion(paises):
    paises.sort(key=obtener_poblacion)
    mostrar_lista(paises)


def ordenar_por_superficie(paises, descendente=False):
    paises.sort(key=obtener_superficie, reverse=descendente)
    mostrar_lista(paises)

#DARIO:
# def mostrar_estadisticas

def menu():
    paises = cargar_paises()

    while True:
        print("\nMENÚ ")
        print("1. Agregar país")
        print("2. Buscar país")
        print("3. Ordenar por nombre")
        print("4. Ordenar por población")
        print("5. Ordenar por superficie (descendente)")
        print("6. Mostrar estadísticas")
        print("7. Salir")

        opcion = input("Seleccione una opción: ").strip()

        match opcion:
            case "1":
                agregar_pais(paises)
            case "2":
                buscar_pais(paises)
            case "3":
                ordenar_por_nombre(paises)
            case "4":
                ordenar_por_poblacion(paises)
            case "5":
                ordenar_por_superficie(paises, descendente=True)
            case "6":
                mostrar_estadisticas(paises)
            case "7":
                print("Muchas gracias, hasta pronto.")
                break
            case _:
                print("Opción inválida.Intente nuevamente.")

#######Finalizado#########

