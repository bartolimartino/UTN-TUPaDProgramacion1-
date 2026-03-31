#Tp integrador – Repetitivas- Condicionales y Secuenciales.
# Alumno: Martino Bartoli

# Ejercicio 1— “Caja del Kiosco”



nombre = input("Ingrese su nombre: ")

while not nombre.isalpha():
    print("Su nombre solo debe contener letras, intente de nuevo.")
    nombre = input("nombre: ")

cantidad_productos = input("ingrese la cantidad de productos: ")

while not cantidad_productos.isdigit() or cantidad_productos == "0":
    print("ingrese un numero entero positivo valido.")
    cantidad_productos = input("productos: ")

cantidad_productos = int(cantidad_productos)

total = 0
total_descuento = 0

for cont in range(1, cantidad_productos + 1):
    precio = input(f"Ingrese el precio del producto {cont}°: ")
    while not precio.isdigit() or precio == "0":
        print("ingrese un numero entero positivo valido.")
        precio = input("precio: ")
    precio = int(precio)

    descuento = input(f"¿el producto {cont}° tiene descuento? S/N: ").upper()
    while descuento not in ("S", "N"):
        print("Ingrese una opcion valida.")
        descuento = input("¿Tiene descuento? S/N: ").upper() 

    total += precio

    if descuento == "S":
        total_descuento += precio * 0.90   
    else:
        total_descuento += precio

ahorro = total - total_descuento
promedio = total_descuento / cantidad_productos

print(f"\nTotal sin descuentos: ${total}")
print(f"Total con descuentos: ${total_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")



# Ejercicio 2 — “Acceso al Campus y Menú Seguro”

usuario = "Alumno"
contraeña = "python123"
Activo = False

for cont in range(1,4):
    usuario = input(f"intento:{cont}/3° Ingrese su usuario: ")
    contraeña = input(f"intento:{cont}/3° Ingrese su contraseña: ")
    if usuario != "Alumno" or contraeña != "python123":
        print("Error: credenciales invalidas.")

    if usuario == "Alumno" and contraeña == "python123":
        print("Acceso concedido")
        Activo = True
        break
else:
    print("Cuenta bloqueada")


if Activo:
    seleccion = 0
    while seleccion != "4":
        print("1°- Ver estado de la inscripcion")
        print("2°- Cambio de Clave")
        print("3°- Frase motivacional")
        print("4°- Salir")

        seleccion = input("Seleccione una opcion: ")
        while not seleccion.isdigit() or not seleccion in("1","2","3","4"):
            seleccion = input("Error: Debe selecionar un numero dentro de las opciones disponibles: ")

        if seleccion == "1":
            print("Inscripto")
            print("")        

        if seleccion == "2":
            contraseña_nueva = input("Ingrese la contraseña nueva (minimo 6 caracteres): ")
            while len(contraseña_nueva) < 6:
                contraseña_nueva = input("Error: minimo 6 caracteres: ")
        
            confirmacion = input("Vuelva a ingresar la contraseña para validar: ")
            while confirmacion != contraseña_nueva:
                confirmacion = input("Las contraseñas no coinciden, vuelva a intentarlo: ")
        
            contraeña = contraseña_nueva  
            print("La contraseña ha sido actualizada")

        if seleccion == "3":
            print("Roma no se construyo en un dia")

        if seleccion == "4":
            Activo = False
           


# Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”
l1unes = "libre"   
l2unes = "libre"
l3unes = "libre"
l4unes = "libre"
m1artes = "libre"
m2artes = "libre"
m3artes = "libre"

id = input("Ingrese su nombre: ")
while not id.isalpha():
    id = input("Error: El nombre solo debe contener letras, intente de nuevo: ")

Eleccion = "0"
while Eleccion != "5":
    print("1°- Reservar turno")
    print("2°- Cancelar turno (por nombre)")
    print("3°- Ver agenda del día")
    print("4°- Ver resumen general")
    print("5°- Cerrar sistema")

    Eleccion = input("Ingrese el numero correspondiente a su consulta (1/5): ")
    while not Eleccion.isdigit() or Eleccion not in ("1","2","3","4","5"):
        Eleccion = input("Debe ingresar un numero dentro del rango valido 1/5: ")

    if Eleccion == "1":
        
        turno = input("Seleccione dia: 1 = Lunes, 2 = Martes: ")
        while not turno.isdigit() or turno not in ("1","2"):
            turno = input("Debe ingresar 1 o 2: ")

        
        Name = input("Ingrese el nombre del paciente: ")
        while not Name.isalpha():
            Name = input("Error: solo letras, intente de nuevo: ")

        
        if turno == "1":
            if l1unes == "libre":      
                l1unes = Name           
                print(f"Turno reservado: Lunes 1 - {Name}")
            elif l2unes == "libre":
                l2unes = Name
                print(f"Turno reservado: Lunes 2 - {Name}")
            elif l3unes == "libre":
                l3unes = Name
                print(f"Turno reservado: Lunes 3 - {Name}")
            elif l4unes == "libre":
                l4unes = Name
                print(f"Turno reservado: Lunes 4 - {Name}")
            else:
                print("No hay turnos disponibles para el lunes")

        elif turno == "2":              
            if m1artes == "libre":
                m1artes = Name
                print(f"Turno reservado: Martes 1 - {Name}")
            elif m2artes == "libre":
                m2artes = Name
                print(f"Turno reservado: Martes 2 - {Name}")
            elif m3artes == "libre":
                m3artes = Name
                print(f"Turno reservado: Martes 3 - {Name}")
            else:
                print("No hay turnos disponibles para el martes")

    if Eleccion == "2":
        cancelar_nombre = input("nombre del paciente: ")
        while not cancelar_nombre.isalpha():
            cancelar_nombre = input("Ingrese el correcto unicamente con letras: ")

        dia_elegido = input("ingrese el dia del turno 1: Lunes o 2: Martes: ")
        while not dia_elegido.isdigit() or not dia_elegido in("1","2"):
            dia_elegido = input("Ingrese uno de los dias validos 1: Lunes o 2: Martes: ")

        if dia_elegido == "1":
            if l1unes == cancelar_nombre:
                l1unes = "libre"
            elif l2unes == cancelar_nombre:
                l2unes = "libre"
            elif l3unes == cancelar_nombre:
                l3unes = "libre"
            elif l4unes == cancelar_nombre:
                l4unes = "libre"
            else:
                print("No se encontro un paciente el lunes")
           
        if dia_elegido == "2":
            if m1artes == cancelar_nombre:
                m1artes = "libre"
            elif m2artes == cancelar_nombre:
                m2artes = "libre"
            elif m3artes == cancelar_nombre:
                m3artes = "libre"
            else:
                print("No se encontro un paciente el Martes")

    if Eleccion == "3":
        agenda = input("Ingrese el dia del cual quiera ver la agenda 1: lunes o 2: martes: ")
        while not agenda.isdigit() or not agenda in ("1","2"):
            agenda = input("ingrese un dia valido 1: lunes o 2: martes, para revisar la agenda: ")

        if agenda == "1":
            print("turnos del dia (Lunes)")
            print("")
            if l1unes == "libre":
                print("lunes 1°- libre")
            else:
                print(f"lunes 1°- {l1unes}")
            
            if l2unes == "libre":
                print("lunes 2°- libre")
            else:
                print(f"lunes 2°- {l2unes}")
            
            if l3unes == "libre":
                print("lunes 3°- libre")
            else:
                print(f"lunes 3°- {l3unes}")
            
            if l4unes == "libre":
                print("lunes 4°- libre")
            else:
                print(f"lunes 4°- {l4unes}")

        
        if agenda == "2":
            print("turnos del dia (martes)")
            print("")
            if m1artes == "libre":
                print("martes 1°- libre")
            else:
                print(f"martes 1°- {m1artes}")            

            if m2artes == "libre":
                print("martes 2°- libre")
            else:
                print(f"martes 2°- {m2artes}")            

            if m3artes == "libre":
                print("martes 3°- libre")
            else:
                print(f"martes 3°- {m3artes}")

    if Eleccion == "4":
            ocupados_lunes = 0
            if l1unes != "libre":
                ocupados_lunes += 1
            if l2unes != "libre":
                ocupados_lunes += 1
            if l3unes != "libre":
                ocupados_lunes += 1
            if l4unes != "libre":
                ocupados_lunes += 1

            
            ocupados_martes = 0
            if m1artes != "libre":
                ocupados_martes += 1
            if m2artes != "libre":
                ocupados_martes += 1
            if m3artes != "libre":
                ocupados_martes += 1

            
            disponibles_lunes = 4 - ocupados_lunes
            disponibles_martes = 3 - ocupados_martes

            print(f"Lunes - ocupados: {ocupados_lunes}, disponibles: {disponibles_lunes}")
            print(f"Martes - ocupados: {ocupados_martes}, disponibles: {disponibles_martes}")

            
            if ocupados_lunes > ocupados_martes:
                print("El dia con mas turnos ocupados es el Lunes")
            elif ocupados_martes > ocupados_lunes:
                print("El dia con mas turnos ocupados es el Martes")
            else:
                print("Empate")

# Ejercicio 4 — “Escape Room: La Bóveda”

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = "" 

Mib = input("Ingrese el nombre del agente: ")
while not Mib.isalpha():
    Mib = input("Error: el nombre solo debe contener letras: ")
forzar_seguido = 0
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not (alarma and tiempo <= 3):
    print(f"Agente: {Mib} ")
    print(f"Energia: {energia} | tiempo: {tiempo} | cerraduras abiertas: {cerraduras_abiertas}")
    print("")
    print("1°- Forzar la cerradura (-20 energia, -2 de tiempo)")
    print("2°- Hackear el panel, (-10 energia, -3 de tiempo)")
    print("3°- Descansar (+15 energia, -1 de tiempo)")
    opcion = input("Seleccione una opcion: ")
    while not opcion.isdigit() or not opcion in("1","2","3"):
        opcion = input("Debe ingresar un numero que corresponda con las opciones disponibles: ")

    if opcion == "1":
        forzar_seguido += 1
        energia -= 20
        tiempo -= 2

        if forzar_seguido == 3:
            alarma = True
            forzar_seguido = 0
            print("¡La cerradura se trabo! Se activo la alarma")
        elif energia < 40:
            print("¡la energia esta por debajo del 40%!, hay un alto riesgo de alarma.")
            riesgo = input("Ingrese un numero del 1 al 3: ")
            while not riesgo.isdigit() or not riesgo in("1","2","3"):
                riesgo = input("Error: debe ingresar un numero dentro del rango valido 1/3: ")
            if riesgo in ("1","2"):
                print("Se abrio una cerradura")
                cerraduras_abiertas += 1
            if riesgo == "3":  
                alarma = True
        else:
            cerraduras_abiertas += 1
            print("Se abrio una cerradura")

    if opcion == "2":
        forzar_seguido = 0
        energia -= 10
        tiempo -= 3
        print("Hackeo en progreso")
        for i in range(4):
            codigo_parcial += "H"
            print(f"paso {i+1}/4 - codigo: {codigo_parcial}  ")
        if len (codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("Cerradura abierta por hackeo")

    if opcion == "3":
        forzar_seguido = 0
        energia += 15
        tiempo -= 1

        if energia > 100:
            energia = 100

        if alarma == True:
            energia -= 10
            

if cerraduras_abiertas == 3:
    print("VICTORIA")

elif energia <= 0 or tiempo <= 0:
    print("DERROTA")

elif alarma and tiempo <= 3:
    print("DERROTA POR BLOQUEO")



# Ejercicio 5 — “Escape Room:"La Arena del Gladiador"

print("¡BIENVENIDO A LA ARENA DEL GLADIADOR!")
print("")
gladiador = input("Ingrese el nombre de su guerrero: ")
while not gladiador.isalpha():
    gladiador = input("Error: Ingrese un nombre que contenga unicamente letras: ")

vida_del_gladiador = 100 
vida_del_enemigo = 100
pociones_de_vida = 3 
daño_base_pesado = 15 
daño_base_enemigo = 12 
turno_gladiador = True
dano_final = 0

while vida_del_gladiador > 0 and vida_del_enemigo > 0:
    print(f"Turno de {gladiador}")
    print("1°- Ataque pesado")
    print("2°- Rafaga veloz")
    print("3°- Curar")
    choise = input("Elija una opcion para su turno: ")
    while not choise.isdigit() or not choise in("1","2","3"):
        choise = input("Error: Elija un numero que corresponda a las acciones disponibles: ")

    if choise == "1":
        if vida_del_enemigo < 20:
            dano_final = daño_base_pesado * 1.5
            vida_del_enemigo -= dano_final
            print(f"Golpe critico, ha realizado {dano_final} puntos de daño")
        else:
            vida_del_enemigo -= daño_base_pesado
            print(f"Atacaste y infligiste {daño_base_pesado} puntos de daño")
    if choise == "2":
        for j in range(3):
            vida_del_enemigo -= 5
            print("Golpe conectado por 5 de daño")
    if choise == "3":
        if pociones_de_vida > 0:
            vida_del_gladiador += 30
            pociones_de_vida -= 1
            print(f"Usaste una pocion, ahora te quedan {pociones_de_vida} pociones y tienes: {vida_del_gladiador} puntos de vida")
        else:
            print("¡No tienes pociones!")

    if vida_del_enemigo > 0:        
        print("¡Turno de tu enemigo!")
        vida_del_gladiador -= daño_base_enemigo
        print(f"El enemigo te ataco!, sufriste: {daño_base_enemigo} puntos de daño!")
        
if vida_del_gladiador > 0:
    print(f"¡EL GLADIADOR {gladiador} A TRIUNFADO!")
else:
    print(f"El gladiador {gladiador} a caido en batalla")
            
