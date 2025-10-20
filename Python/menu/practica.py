#nombre, curso, 4 notas, >= 2 o <= 7.  calcular promedio, determinar si aprobo o reprobo -> guardar en la lista si aprobo o reprobo.
#guardar en la lista -> Nombre, Curso, 4 Notas, Promedio de las 4 notas, estado (aprobado o reprobado).
registros = []

while True:
    print("===== MENU REGISTROS DE USUARIOS =====")
    print("[1] Agregar registro")
    print("[2] Eliminar registro")
    print("[3] Editar registro")
    print("[4] Mostrar registro")
    print("[5] Salida")
    
    opcion = input("Ingrese su opoción [1-5]: ")
    
    match opcion:
        case "1":
            #Agregar registro
            run       = input("Ingrese su RUN : ")
            nombre    = input("Ingrese su Nombre : ")
            curso     = input("Ingrese su Curso : ")
            
            c = 0
            print("Agrege 4 notas : ")
            for i in range(4):    #SERIA MEJOR USAR UN WHILE TRUE? INTENTARLO
                notas = float(input())
                c = notas + c
                if notas < 2 or notas > 7:
                    print("Solo notas entre 2 y 7")
                    c = 0
                    break
            promedio = c/4
            if promedio >= 4:
                estado = "APROBADO"
            else:
                estado = "DESAPROBADO"                  
            if curso == "" or nombre == "" or run == "" or c == 0:   #ESTA LINEA NO FUNCIONA BIEN NO SE POR QUE
                print("")
                print("NO debe ingresar datos en blanco...")
                break
            else:
                persona = {"RUN": run, "NOMBRE": nombre, "CURSO": curso, "NOTAS": f"{promedio:.1f}", "ESTADO": estado}
                registros.append(persona)
                print("")
                print("Se agrego registro en forma existosa... :)")
            
        case "2":
            #Eliminar registro de una lista
            buscar_run = input("Ingrese su RUN para ser eliminado : ")
            encontra = False
            for persona in registros:
                if persona["RUN"]  ==  buscar_run:
                    registros.remove(persona)
                    print("Registro eliminado con éxito...")
                    encontra = True
                    break
            if not encontra:
                print("No se encuetra registro o empleado")
                
        case "3":
            #Editar o modificar datos
            buscar_run = input("Ingrese su RUN para ser modificado : ")
            encontra = False
            c = 0
            for persona in registros:
                if persona["RUN"]  ==  buscar_run:
                    nuevo_nombre = input("Ingrese nuevo nombre : ")
                    nuevo_curso  = input("Ingrese nuevo curso : ")
                    print("Agrege 4 notas : ")
                    for i in range(4):
                        nueva_nota = float(input())
                        c = nueva_nota + c
                        if nueva_nota < 2 or nueva_nota > 7:
                            print("Solo notas entre 2 y 7")
                            break
                    promedio = c/4
                    if promedio >= 4:
                        nuevo_estado = "APROBADO"
                    elif promedio < 4:
                        nuevo_estado = "DESAPROBADO"
                    if nuevo_nombre:
                        persona["NOMBRE"] = nuevo_nombre
                        if nuevo_curso:
                            persona["CURSO"] = nuevo_curso
                            if nueva_nota:
                                persona["NOTAS"] = nueva_nota
                                if nuevo_estado:
                                    
                                    persona["ESTADO"] = nuevo_estado
                
                print("Cambios realizados con Exito...!!!")        
                encontra = True
                break
            if not encontra:
                print("No se encuetra registro o empleado para ser modifico..!!")            
                
                
        case "4":
            print("")
            print("Visualizar registro")
            print(registros)
            print("")
        case "5":
            break
        case _:
            print("")
            print("Opcion NO valida")
            print("")

print("Programa terminado.... muchas gracias....")

