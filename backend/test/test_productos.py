def test_agregar_producto(client):
    payload = {
        "Relleno": "Dulce de leche",
        "Precio": 3000,
        "imagen_url": "images/dulce.jpg"
    }

    response = client.post("/productos", json=payload)
    assert response.status_code == 201
    data = response.get_json()
    assert "message" in data
    assert "Producto agregado correctamente" in data["message"]
