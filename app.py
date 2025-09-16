from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Configuración de la base de datos
db_config = {
    "host": "10.9.120.5",
    "user": "rellenita",
    "password": "rellenita1234",
    "database": "Rellenitas",
    "port": 3306
}

# Mensaje de bienvenida
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "API funcionando. Usá /cliente para obtener datos."})

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

@app.route("/setup", methods=["POST"])
def setup_db():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # 1. Insertar Categorías sin lista
        cursor.execute(
            "INSERT INTO Categorias (CategoriaID, Gusto) VALUES (%s, %s)",
            (1, "Vainilla")
        )
        cursor.execute(
            "INSERT INTO Categorias (CategoriaID, Gusto) VALUES (%s, %s)",
            (2, "Chocolate")
        )
        cursor.execute(
            "INSERT INTO Categorias (CategoriaID, Gusto) VALUES (%s, %s)",
            (3, "Avena")
        )

        # 2. Insertar Galletitas sin lista
        cursor.execute(
            "INSERT INTO Galletitas (GalletitasID, Relleno, Precio) VALUES (%s, %s, %s)",
            (1, "Nutella", 2000)
        )
        cursor.execute(
            "INSERT INTO Galletitas (GalletitasID, Relleno, Precio) VALUES (%s, %s, %s)",
            (2, "Bon o Bon", 2000)
        )

        # 3. Insertar Sabores sin lista
        cursor.execute(
            "INSERT INTO Sabores (SaboresID, CategoriaID, GalletitasID) VALUES (%s, %s, %s)",
            (1, 1, 1)
        )
        cursor.execute(
            "INSERT INTO Sabores (SaboresID, CategoriaID, GalletitasID) VALUES (%s, %s, %s)",
            (2, 2, 1)
        )

        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"message": "Datos insertados correctamente 🚀"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# GET - Consultar Sabores con sus categorías y galletitas
@app.route("/sabores", methods=["GET"])
def get_sabores():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT s.SaboresID, c.Gusto, g.Relleno, g.Precio
            FROM Sabores s
            JOIN Categorias c ON s.CategoriaID = c.CategoriaID
            JOIN Galletitas g ON s.GalletitasID = g.GalletitasID
        """)

        resultados = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(resultados)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)





