
from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Configuración de la base de datos
db_config = {
    "host": "10.9.120.5",     # IP del servidor MySQL
    "user": "rellenita",       # Usuario MySQL
    "password": "rellenita1234",  # Contraseña
    "database": "Rellenitas",  # Nombre de la base de datos
    "port": 8080              # Puerto en el que está escuchando MySQL
}

# mensaje de bienvenida
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "API funcionando. Usá /users para obtener datos."})

# GET - Obtener todos los clientes
@app.route("/cliente", methods=["GET"])
def get_clientes():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM Clientes")
        results = cursor.fetchall()

        cursor.close()
        conn.close()

        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# POST - Insertar un cliente
@app.route("/clientes", methods=["POST"])
def add_cliente():
    try:
        data = request.get_json()
        nombre = data.get("Nombre")
        apellido = data.get("Apellido")
        dni = data.get("DNI")

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO Clientes (Nombre, Apellido, DNI) VALUES (%s, %s, %s)",
            (nombre, apellido, dni)
        )
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({"message": "Cliente agregado correctamente 🚀"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    



@app.route("/clientes2", methods=["POST"])
def add_cliente2():
    try:
        print("Iniciando solicitud POST")
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No se recibió el JSON."}), 400

        nombre = data.get("Nombre")
        apellido = data.get("Apellido")
        dni = data.get("DNI")

        if not nombre or not apellido or not dni:
            return jsonify({"error": "Faltan datos. Nombre, Apellido y DNI son obligatorios."}), 400

        print(f"Recibidos: Nombre: {nombre}, Apellido: {apellido}, DNI: {dni}")

        # Conectar a MySQL
        conn = mysql.connector.connect(**db_config)
        print("Conexión exitosa a MySQL.")

        cursor = conn.cursor()

        # Ejecutar el INSERT
        cursor.execute(
            "INSERT INTO Clientes (Nombre, Apellido, DNI) VALUES (%s, %s, %s)",
            (nombre, apellido, dni)
        )
        conn.commit()

        print("Cliente agregado exitosamente.")
        
        cursor.close()
        conn.close()

        return jsonify({"message": "Cliente agregado correctamente 🚀"}), 201

    except mysql.connector.Error as e:
        print(f"Error de MySQL: {e}")
        return jsonify({"error": f"Error en MySQL: {e}"}), 500

    except Exception as e:
        print(f"Error inesperado: {e}")
        return jsonify({"error": str(e)}), 500



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
