import React, { useEffect, useState } from "react";

export default function Producto() {
  const [productos, setProductos] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/productos")
      .then((res) => res.json())
      .then((data) => setProductos(data));
  }, []);

  return (
    <div
      style={{ display: "flex", flexWrap: "wrap", justifyContent: "center" }}
    >
      {productos.map((p) => (
        <div
          key={p.GalletitasID}
          style={{ margin: "20px", border: "1px solid #ccc", padding: "10px" }}
        >
          {p.imagen_url && (
            <img src={p.imagen_url} alt={p.Relleno} width="150" />
          )}
          <h3>{p.Relleno}</h3>
          <p>${p.Precio}</p>
        </div>
      ))}
    </div>
  );
}
