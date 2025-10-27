import mysql.connector

try:
    conn = mysql.connector.connect(
        host="10.9.120.5",
        user="rellenita",
        password="rellenita1234",
        database="Rellenitas",
        port=3306
    )
    print("✅ Conexión exitosa")
    conn.close()
except mysql.connector.Error as err:
    print("❌ Error:", err)
