import React from "react";
import "./Styles.css"; // importa tu CSS

export default function Pedido() {
  return (
    <div className="container">
      <header>
        <h1 className="cookie-title">Bienvenidos a Galletitas Deliciosas</h1>
      </header>

      <div className="card">
        <img src="/images/galletita.jpeg" alt="Galletita" />
        <div className="card-content">
          <h2 className="cookie-title">Galletita de Chocolate</h2>
          <p>Irresistible galletita casera con chips de chocolate.</p>
          <button>Agregar al carrito</button>
        </div>
      </div>

      <footer>© 2025 Galletitas Deliciosas</footer>
    </div>
  );
}
