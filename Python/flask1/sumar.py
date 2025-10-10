#Esta línea importa funciones específicas del módulo Flask, que necesitas para crear y controlar tu aplicación web. 
from flask import Flask, render_template, request 

#Crea una instancia de la aplicación web Flask. Es decir, esta línea inicia tu sitio web en Python. 
app = Flask(__name__) 

#Esta línea asocia una función en Python con una URL. Es lo que se llama una ruta en Flask. 
#Significa: “Cuando un usuario visita la página principal (/), ejecuta la función que está justo debajo de esta línea.” 
@app.route('/', methods=['GET', 'POST']) 

#Es una definición de función en Python. 
#def → palabra clave de Python para definir una función. 
#sumar → es el nombre de la función. 
def sumar(): 

    #None es una palabra clave en Python que representa la ausencia de valor o “nada”. 
    resultado = None 

    #El formulario o la página fue enviada usando el método POST 
    if request.method == 'POST': 

        #try: le dice a Python: 
        #“Intenta ejecutar este bloque de código. 
        #y si ocurre un error, no te detengas ni muestres un mensaje feo: mejor ve al bloque except: y haz algo con ese error.” 
        try: 
            num1 = float(request.form.get('num1', 0)) 
            num2 = float(request.form.get('num2', 0)) 
            resultado = num1 + num2 

        #Esta línea atrapa errores específicos que ocurren cuando intentas convertir algo a un tipo de dato, y ese algo no es válido. 
        except ValueError: 
            resultado = "Por favor ingresa números válidos." 

    #Esta línea le dice a Flask que devuelva una página HTML (sumar.html) al navegador, 
    #y además le pasa datos para que se muestren en esa página. 
    return render_template('sumar.html', resultado=resultado) 

#Ejecuta el código dentro de este bloque solo si estás ejecutando este archivo directamente. 
if __name__ == '__main__': 
    app.run(debug=True)