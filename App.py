
from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# Configuración de la base de datos
db_config = {
    "host": "10.9.120.5",     # tu IP del servidor MySQL
    "user": "root",           # tu usuario MySQL
    "password": "1234",       # tu contraseña MySQL
    "database": "rellenitas"  # tu base de datos
}

# mensaje de bienvenida
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "API funcionando. Usá /users para obtener datos."})

# GET - Obtener todos los clientes
@app.route("clientes", methods=["GET"])
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
