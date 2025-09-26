nombre = "Chanchito" 
apellido = "Feliz" 
nombre_completo = nombre + " " + apellido  
longitud = len(nombre_completo) 
apellido_mayuscula = apellido.upper() 
apellido_minuscula =  apellido.lower() 
posicion = nombre_completo.find("Feliz") 
nombre_reemplazo = nombre_completo.replace("Feliz", "Contento") 
edad = 25 
frase = f"Mi nombres es {nombre} {apellido} y tengo {edad} años." 
print(frase) 
print(nombre_completo) 
print(longitud) 
print(apellido_mayuscula) 
print(apellido_minuscula) 
print(posicion) 
print(nombre_reemplazo)


a = 10 
b = 20 
print(a == b)   # False 
print(a != b)   # True 
print(a < b)    # True 
print(a > b)    # False 
print(a <= 10)  # True 
print(b >= 15)  # True

# Variables de ejemplo 
x = 10 
y = 5 
# AND 
print(x > 5 and y < 10)    # True  (ambas son verdaderas) 
print(x > 15 and y < 10)   # False (una es falsa) 
# OR 
print(x > 5 or y > 10)     
print(x < 5 or y > 10)     
# NOT 
print(not(x > 5))          
# True  (una es verdadera) 
# False (ambas son falsas) 
# False (porque x > 5 es True, y not True → False)