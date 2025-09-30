import React, { useEffect, useState } from "react";
import "./Pedidos.css";

function Pedidos() {
  const [pedidos, setPedidos] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/pedidos")
      .then(res => res.json())
      .then(data => setPedidos(data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div className="pedidos-container">
      <h1>Lista de Pedidos</h1>
      {pedidos.length === 0 ? (
        <p>Cargando pedidos...</p>
      ) : (
        <table className="pedidos-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Nombre</th>
              <th>Apellido</th>
              <th>Galletita</th>
              <th>Cantidad</th>
              <th>Monto</th>
              <th>Fecha</th>
              <th>Hora</th>
              <th>Pago</th>
            </tr>
          </thead>
          <tbody>
            {pedidos.map(p => (
              <tr key={p.PedidosID}>
                <td>{p.PedidosID}</td>
                <td>{p.Nombre}</td>
                <td>{p.Apellido}</td>
                <td>{p.Galletita}</td>
                <td>{p.Cantidad}</td>
                <td>${p.Monto}</td>
                <td>{new Date(p.Fecha).toLocaleDateString()}</td>
                <td>{p.Hora}</td>
                <td>{p.Metodo_pagos}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default Pedidos;
