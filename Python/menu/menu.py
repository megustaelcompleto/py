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
            run    = input("Ingrese su RUN : ")
            nombre = input("Ingrese nombre de usurio : ")
            edad   = input("Ingrese su edad : ")
            
            if run == "" or nombre == "" or edad == "":
                print("")
                print("NO debe ingresar datos en blanco...")
            else:
                persona = {"RUN": run, "NOMBRE": nombre, "EDAD": edad}
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
                  print("Elimado registro con existo....")
                  encontra = True
                  break
            if not encontra:
                print("No se encuetra registro o empleado")
                
        case "3":
            #Editar o modificar datos
            buscar_run = input("Ingrese su RUN para ser modificado : ")
            encontra = False
            for persona in registros:
              if persona["RUN"]  ==  buscar_run:
                  nuevo_nombre = input("Ingrese nuevo nombre : ")
                  nuevo_edad   = input("Ingrese nueva edad : ")
                  if nuevo_nombre:
                      persona["NOMBRE"] = nuevo_nombre
                  if nuevo_edad:
                      persona["EDAD"] = nuevo_edad
                  
                  print("Cambios realizados con Exito...!!!")        
                  encontra = True
                  break
            if not encontra:
                print("No se encuetra registro o empleado para ser modifico..!!")            
                
                
        case "4":
            print("")
            print("Visualizar registro")
            print("")
        case "5":
            break
        case _:
            print("")
            print("Opcion NO valida")
            print("")

print("Programa terminado.... muchas gracias....")

