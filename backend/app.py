from flask import Flask, request, jsonify
import mysql.connector
from dotenv import load_dotenv
import os

# Cargar las variables del archivo .env
load_dotenv()

app = Flask(__name__)

# Configuración de la base de datos desde las variables de entorno
db_config = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
    "port": int(os.getenv("DB_PORT")),
    "auth_plugin": "mysql_native_password"  # Forzar el plugin de autenticación adecuado
}
# Intentar la conexión
try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Clientes")  # Solo para probar la conexión
    results = cursor.fetchall()
    cursor.close()
    conn.close()
except Exception as e:
    print("Error en la conexión:", str(e))
# ---------------------------
# MENSAJE DE BIENVENIDA
# ---------------------------
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "API funcionando. Usá /cliente, /metodospago, /pagos, /pedidos 🚀"})

# ---------------------------
# CLIENTES
# ---------------------------
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

# ---------------------------
# SETUP - Insertar datos base
# ---------------------------
@app.route("/setup", methods=["POST"])
def setup_db():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Categorías
        cursor.execute("INSERT INTO Categorias (CategoriaID, Gusto) VALUES (%s, %s)", (1, "Vainilla"))
        cursor.execute("INSERT INTO Categorias (CategoriaID, Gusto) VALUES (%s, %s)", (2, "Chocolate"))
        cursor.execute("INSERT INTO Categorias (CategoriaID, Gusto) VALUES (%s, %s)", (3, "Avena"))

        # Galletitas
        cursor.execute("INSERT INTO Galletitas (GalletitasID, Relleno, Precio) VALUES (%s, %s, %s)", (1, "Nutella", 2000))
        cursor.execute("INSERT INTO Galletitas (GalletitasID, Relleno, Precio) VALUES (%s, %s, %s)", (2, "Bon o Bon", 2000))
        cursor.execute("INSERT INTO Galletitas (GalletitasID, Relleno, Precio) VALUES (%s, %s, %s)", (3, "Frutilla", 2500))

        # Sabores
        cursor.execute("INSERT INTO Sabores (SaboresID, CategoriaID, GalletitasID) VALUES (%s, %s, %s)", (1, 1, 1))
        cursor.execute("INSERT INTO Sabores (SaboresID, CategoriaID, GalletitasID) VALUES (%s, %s, %s)", (2, 2, 2))
        cursor.execute("INSERT INTO Sabores (SaboresID, CategoriaID, GalletitasID) VALUES (%s, %s, %s)", (3, 3, 3))

        # Métodos de pago
        cursor.execute("INSERT INTO Metodo_Pagos (Metodo_PagosID, Nombre) VALUES (%s, %s)", (1, "Efectivo"))
        cursor.execute("INSERT INTO Metodo_Pagos (Metodo_PagosID, Nombre) VALUES (%s, %s)", (2, "Transferencia"))
        cursor.execute("INSERT INTO Metodo_Pagos (Metodo_PagosID, Nombre) VALUES (%s, %s)", (3, "Tarjeta"))

        # Pagos
        cursor.execute("INSERT INTO Pagos (PagosID, Monto, Metodo_pagos, GalletitasID) VALUES (%s, %s, %s, %s)", (1, 2000, "Efectivo", 1))
        cursor.execute("INSERT INTO Pagos (PagosID, Monto, Metodo_pagos, GalletitasID) VALUES (%s, %s, %s, %s)", (2, 1500, "Transferencia", 2))
        cursor.execute("INSERT INTO Pagos (PagosID, Monto, Metodo_pagos, GalletitasID) VALUES (%s, %s, %s, %s)", (3, 2500, "Tarjeta", 3))

        # Pedidos (asegúrate que existan clientes con esos IDs)
        cursor.execute("INSERT INTO Pedidos (PedidosID, Fecha, Hora, Cantidad, ClientesID, PagosID, GalletitasID) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                       (1, "2025-05-19", "17:59:00", 3, 1, 1, 1))
        cursor.execute("INSERT INTO Pedidos (PedidosID, Fecha, Hora, Cantidad, ClientesID, PagosID, GalletitasID) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                       (2, "2025-05-19", "20:03:00", 1, 2, 2, 2))
        cursor.execute("INSERT INTO Pedidos (PedidosID, Fecha, Hora, Cantidad, ClientesID, PagosID, GalletitasID) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                       (3, "2025-05-20", "09:20:00", 4, 3, 3, 3))

        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"message": "Datos insertados correctamente 🚀"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------------------------
# SABORES
# ---------------------------
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

# ---------------------------
# MÉTODOS DE PAGO
# ---------------------------
@app.route("/metodospago", methods=["GET"])
def get_metodos_pago():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Metodo_Pagos")
        resultados = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(resultados)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------------------------
# PAGOS
# ---------------------------
@app.route("/pagos", methods=["GET"])
def get_pagos():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT p.PagosID, p.Monto, p.Metodo_pagos, g.Relleno AS Galletita
            FROM Pagos p
            JOIN Galletitas g ON p.GalletitasID = g.GalletitasID
        """)
        
        resultados = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(resultados)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------------------------
# PEDIDOS
# ---------------------------
@app.route("/pedidos", methods=["GET"])
def get_pedidos():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT pe.PedidosID, pe.Fecha, pe.Hora, pe.Cantidad,
                   c.Nombre, c.Apellido,
                   pa.Monto, pa.Metodo_pagos,
                   g.Relleno AS Galletita
            FROM Pedidos pe
            JOIN Clientes c ON pe.ClientesID = c.ClientesID
            JOIN Pagos pa ON pe.PagosID = pa.PagosID
            JOIN Galletitas g ON pe.GalletitasID = g.GalletitasID
        """)

        resultados = cursor.fetchall()

        # 🔥 Convertir Hora a string
        for r in resultados:
            if isinstance(r["Hora"], (dict,)):
                continue
            if r["Hora"] is not None:
                r["Hora"] = str(r["Hora"])

        cursor.close()
        conn.close()
        return jsonify(resultados)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ---------------------------
# PRODUCTOS (ADMIN)
# ---------------------------
@app.route("/productos", methods=["GET"])
def get_productos():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Galletitas")  # o tabla Productos si la creas aparte
        resultados = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(resultados)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/productos", methods=["POST"])
def add_producto():
    try:
        data = request.get_json()
        nombre = data.get("Relleno")
        precio = data.get("Precio")
        imagen_url = data.get("imagen_url", "")  # ruta relativa en /public/images

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Galletitas (Relleno, Precio, imagen_url) VALUES (%s, %s, %s)",
            (nombre, precio, imagen_url)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Producto agregado correctamente 🚀"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def create_app():
    return app

# -----------------------
# RUN APP
# ---------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
