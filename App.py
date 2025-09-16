#from flask import Flask, request, jsonify  # Importamos Flask, request y jsonify
#import mysql.connector  # Librería para conectar Python con MySQL

#app = Flask(__name__)  # Inicializamos la aplicación Flask

## Configuración de la base de datos
#db_config = {
#    "host": "10.9.120.5",        # Dirección IP del servidor MySQL
#    "user": "rellenita",         # Usuario de MySQL
#    "password": "rellenita1234", # Contraseña de MySQL
#    "database": "Rellenitas",    # Nombre de la base de datos
#    "port": 8080                 # Puerto en el que está escuchando MySQL
#}

## mensaje de bienvenida
#@app.route("/", methods=["GET"])  # Ruta principal con método GET
#def home():  # Función que responde en la ruta "/"
#    return jsonify({"message": "API funcionando. Usá /users para obtener datos."})  # Devuelve un JSON


## GET - Obtener todos los clientes
#@app.route("/cliente", methods=["GET"])  # Ruta GET para obtener clientes
#def get_clientes():  # Función para obtener clientes
#    try:  # Manejo de errores
#        conn = mysql.connector.connect(**db_config)  # Conectar a MySQL
#        cursor = conn.cursor(dictionary=True)  # Crear cursor que devuelve diccionarios

#        cursor.execute("SELECT * FROM Clientes")  # Ejecutar consulta SQL
#        results = cursor.fetchall()  # Obtener todos los resultados

#        cursor.close()  # Cerrar cursor
#        conn.close()  # Cerrar conexión

#        return jsonify(results)  # Devolver resultados como JSON
#    except Exception as e:  # Capturar error
#        return jsonify({"error": str(e)}), 500  # Devolver error en JSON


## POST - Insertar un cliente
#@app.route("/clientes", methods=["POST"])  # Ruta POST para agregar clientes
#def add_cliente():  # Función para insertar cliente
#    try:  # Manejo de errores
#        data = request.get_json()  # Obtener JSON del request
#        nombre = data.get("Nombre")  # Extraer campo Nombre
#        apellido = data.get("Apellido")  # Extraer campo Apellido
#        dni = data.get("DNI")  # Extraer campo DNI

#        conn = mysql.connector.connect(**db_config)  # Conectar a MySQL
#        cursor = conn.cursor()  # Crear cursor

#        cursor.execute(  # Ejecutar consulta INSERT
#            "INSERT INTO Clientes (Nombre, Apellido, DNI) VALUES (%s, %s, %s)",
#            (nombre, apellido, dni)  # Parámetros seguros
#        )
#        conn.commit()  # Guardar cambios

#        cursor.close()  # Cerrar cursor
#        conn.close()  # Cerrar conexión

#        return jsonify({"message": "Cliente agregado correctamente 🚀"}), 201  # Respuesta JSON
#    except Exception as e:  # Captura de errores
#        return jsonify({"error": str(e)}), 500  # Respuesta de error


## POST - Insertar un cliente (versión detallada con validaciones y logs)
#@app.route("/clientes2", methods=["POST"])  # Ruta POST alternativa
#def add_cliente2():  # Función para insertar cliente con validación
#    try:  # Manejo de errores
#        print("Iniciando solicitud POST")  # Mensaje en consola
#        data = request.get_json()  # Obtener JSON

#        if not data:  # Si no se recibió JSON
#            return jsonify({"error": "No se recibió el JSON."}), 400  # Respuesta error

#        nombre = data.get("Nombre")  # Obtener Nombre
#        apellido = data.get("Apellido")  # Obtener Apellido
#        dni = data.get("DNI")  # Obtener DNI

#        if not nombre or not apellido or not dni:  # Validar datos
#            return jsonify({"error": "Faltan datos. Nombre, Apellido y DNI son obligatorios."}), 400

#        print(f"Recibidos: Nombre: {nombre}, Apellido: {apellido}, DNI: {dni}")  # Log datos recibidos

#        conn = mysql.connector.connect(**db_config)  # Conectar a MySQL
#        print("Conexión exitosa a MySQL.")  # Mensaje consola

#        cursor = conn.cursor()  # Crear cursor

#        cursor.execute(  # Ejecutar INSERT
#            "INSERT INTO Clientes (Nombre, Apellido, DNI) VALUES (%s, %s, %s)",
#            (nombre, apellido, dni)  # Parámetros
#        )
#        conn.commit()  # Guardar cambios

#        print("Cliente agregado exitosamente.")  # Mensaje consola

#        cursor.close()  # Cerrar cursor
#        conn.close()  # Cerrar conexión

#        return jsonify({"message": "Cliente agregado correctamente 🚀"}), 201  # Respuesta OK

#    except mysql.connector.Error as e:  # Errores específicos de MySQL
#        print(f"Error de MySQL: {e}")  # Log en consola
#        return jsonify({"error": f"Error en MySQL: {e}"}), 500  # Respuesta error

#    except Exception as e:  # Errores generales
#        print(f"Error inesperado: {e}")  # Log consola
#        return jsonify({"error": str(e)}), 500  # Respuesta error


## Ejecutar la aplicación Flask
#if __name__ == "__main__":  # Punto de entrada
#    app.run(host="0.0.0.0", port=5000, debug=True)  # Iniciar servidor Flask
