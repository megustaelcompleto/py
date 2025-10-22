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
    
    opcion = input("Ingrese su opción [1-5]: ")
    
    match opcion:
        case "1":
            #Agregar registro
            print("")
            run       = input("Ingrese su RUN : ")
            nombre    = input("Ingrese su Nombre : ")
            curso     = input("Ingrese su Curso : ")
            
            n1   = float(input("Nota 1 : "))
            n2   = float(input("Nota 2 : "))
            n3   = float(input("Nota 3 : "))
            n4   = float(input("Nota 4 : "))
            
            if (2 <= n1 <= 7) and (2 <= n2 <= 7) and (2 <= n3 <= 7) and (2 <= n4 <= 7):
                promedio = round((n1+n2+n3+n4)/4, 2)
                if promedio >= 4:
                    estado = "APROBADO"
                else:
                    estado = "DESAPROBADO"
                if curso == "" or nombre == "" or run == "":
                    print("")
                    print("NO debe ingresar datos en blanco...")
                    break
                else:
                    persona = {"RUN": run, "NOMBRE": nombre, "CURSO": curso, "Nota 1": n1, "Nota 2": n2, "Nota 3": n3, "Nota 4": n4 ,"Promedio": f"{promedio:.1f}", "ESTADO": estado}
                    registros.append(persona)
                    print("")
                    print("Se agrego registro en forma existosa...")
            else:
                print("Ingresar notas del 2 al 7")
                break
        case "2":
            print("")
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
            print("")
            buscar_run = input("Ingrese su RUN para ser modificado : ")
            encontra1 = False
            
            for persona in registros:
                if persona["RUN"]  ==  buscar_run:
                    encontra1 = True
                    nuevo_nombre = input("Ingrese nuevo nombre : ")
                    nuevo_curso  = input("Ingrese nuevo curso : ")
                    print("")
                    print("Ingrese un 0 para mantener la nota original")
                    nu1 = float(input(f"Nueva nota 1 (actual: {persona["Nota 1"]}) "))
                    nu2 = float(input(f"Nueva nota 2 (actual: {persona["Nota 2"]}) "))
                    nu3 = float(input(f"Nueva nota 3 (actual: {persona["Nota 3"]}) "))
                    nu4 = float(input(f"Nueva nota 4 (actual: {persona["Nota 4"]}) "))
                    if nu1 == 0:
                        nu1 = persona["Nota 1"]
                    if nu2 == 0:
                        nu2 = persona["Nota 2"]
                    if nu3 == 0:
                        nu3 = persona["Nota 3"]
                    if nu4 == 0:
                        nu4 = persona["Nota 4"]
                    
                    if (2 <= nu1 <= 7) and (2 <= nu2 <= 7) and (2 <= nu3 <= 7) and (2 <= nu4 <= 7):
                        nuevo_promedio = round((nu1+nu2+nu3+nu4)/4, 2)
                        if nuevo_promedio >= 4:
                            nuevo_estado = "APROBADO"
                        elif nuevo_promedio < 4:
                            nuevo_estado = "DESAPROBADO"
                        if nuevo_nombre:
                            persona["NOMBRE"]   = nuevo_nombre
                        if nuevo_curso:
                            persona["CURSO"]    = nuevo_curso
                        if nuevo_estado:
                            persona["ESTADO"]   = nuevo_estado
                        if nuevo_promedio:
                            persona["Promedio"] = nuevo_promedio
                    else:
                        print("Ingrese notas del 2 al 7")
                        break
                    print("")
                    print("Cambios realizados con Exito...!!!")        
                    break
            if not encontra1:
                print("")
                print("RUN no encrontrado")
                print("")
                    
                
                
                
        case "4":
            print("")
            print("Visualizar registro")
            print("")
            for persona in registros:
                print(persona)
            print("")
        case "5":
            break
        case _:
            print("")
            print("Opcion NO valida")
            print("")

print("Programa terminado...")

