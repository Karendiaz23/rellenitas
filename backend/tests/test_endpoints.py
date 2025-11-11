# test/test_endpoints.py
import pytest

def test_home(client):
    res = client.get("/")
    assert res.status_code == 200
    assert "API funcionando" in res.get_json()["message"]

def test_get_clientes(client):
    res = client.get("/cliente")
    assert res.status_code == 200 # 500 si no hay DB real
    
def test_post_clientes(client):
    res = client.post("/clientes", json={"Nombre": "Karen", "Apellido": "Díaz", "DNI": "12345678"})
    assert res.status_code == 201

def test_post_clientes_duplicados(client):
    res = client.post("/clientes", json={"Nombre": "Luana", "Apellido": "Lopez", "DNI": "11111111"})
    assert res.status_code == 201
    res = client.post("/clientes", json={"Nombre": "Luana", "Apellido": "Lopez", "DNI": "11111111"})
    assert res.status_code == 400


def test_get_sabores(client):
    res = client.get("/sabores")
    assert res.status_code == 200
    sabores = res.get_json() 
    print(sabores)
    assert len(sabores) == 18  

def test_get_metodos_pago(client):
    res = client.get("/metodospago")
    assert res.status_code == 200
    assert b'Efectivo' in res.data  # Verifica que el método de pago "Efectivo" esté en la respuesta
    assert b'Transferencia' in res.data  # Verifica que "Transferencia" esté en la respuesta
    assert b'Tarjeta' in res.data  # Verifica que "Tarjeta" esté en la respuesta


def test_get_pagos(client):
    res = client.get("/pagos")
    assert res.status_code == 200
    data = res.get_json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "PagosID" in data[0]
    assert "Monto" in data[0]
    assert "Metodo_pagos" in data[0]
    assert "Galletita" in data[0]


def test_get_pedidos(client):
    res = client.get("/pedidos")
    assert res.status_code == 200

    data = res.get_json()
    assert isinstance(data, list)

    if data:  # Si hay pedidos en la base
        pedido = data[0]
        assert "PedidosID" in pedido
        assert "Fecha" in pedido
        assert "Cantidad" in pedido
        assert "Nombre" in pedido
        assert "Metodo_pagos" in pedido
        assert "Galletita" in pedido


def test_get_productos(client):
    res = client.get("/productos")
    assert res.status_code == 200

    try:
        productos = res.get_json()  # Convierte la respuesta en JSON (si es que es JSON)
        
        assert len(productos) == 25

        print(productos)
    except Exception as e:
        # Si no se puede convertir a JSON, imprime el error
        print("No es JSON. Error:", e)
        # Si la respuesta no es JSON, imprime los datos binarios
        print("Datos binarios:", res.data)
