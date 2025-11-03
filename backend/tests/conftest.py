import sys
import os
import pytest
import mysql.connector

# Fuerza a Python a buscar app.py en la carpeta raíz del proyecto
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


db_config = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
    "port": int(os.getenv("DB_PORT")),
    "auth_plugin": "mysql_native_password",
    "ssl_disabled": True,
    "use_pure": True
}
from app import app as flask_app

@pytest.fixture
def client():
    flask_app.config.update(TESTING=True)
    with flask_app.test_client() as client:
        yield client


@pytest.fixture(autouse=True)
def run_around_tests():
    # Code that will run before your test, for example:
    #files_before = # ... do something to check the existing files
    # A test function will be run at this point

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

   # Verificar si ya existe el cliente
    cursor.execute(f"DELETE FROM Clientes WHERE DNI in (12345678, 11111111);")
    # cursor.execute(f"DELETE FROM Clientes WHERE DNI = {11111111};")
    conn.commit()
    cursor.close()
    conn.close()
    print("elimine los clientes al inicio")
    yield
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

   # Verificar si ya existe el cliente
    cursor.execute(f"DELETE FROM Clientes WHERE DNI in (12345678, 11111111);")
    # cursor.execute(f"DELETE FROM Clientes WHERE DNI = {12345678};")
    # cursor.execute(f"DELETE FROM Clientes WHERE DNI = {11111111};")
    conn.commit()
    cursor.close()
    conn.close()
    print("elimine los clientes al final")

    # Code that will run after your test, for example:
    #files_after = # ... do something to check the existing files
    #assert files_before == files_after

    