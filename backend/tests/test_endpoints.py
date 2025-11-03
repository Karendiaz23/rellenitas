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


def test_get_metodos_pago(client):
    res = client.get("/metodospago")
    assert res.status_code == 200

def test_get_pagos(client):
    res = client.get("/pagos")
    assert res.status_code == 200

def test_get_pedidos(client):
    res = client.get("/pedidos")
    assert res.status_code == 200

def test_get_productos(client):
    res = client.get("/productos")
    assert res.status_code == 200
