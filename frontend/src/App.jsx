import React from "react";
import "./App.css";

export default function Home() {
  return (
    <div className="home-container">
      <header className="home-header">
        <div className="header-overlay">
   <h1 style={{ fontFamily: 'Rubik Gemstones', fontSize: '3rem', color: '#d2691e' }}>
  Rellenitas
</h1>

        </div>
      </header>

      <main className="home-main">
        <section className="section">
          <img
            src="/src/Nena.jpg"
            className="section-image"
          />
          <div className="section-text">
            <h2>¿Qué es Rellenitas?</h2>
            <p>
              Rellenitas es un emprendimiento que nació en abril de 2023, creado
              por una estudiante de 17 años con gran entusiasmo por la pastelería
              y las galletitas.
            </p>
            <p>
              Con mucho esfuerzo, dedicación y un gran pasión por la cocina,
              comenzó a preparar galletitas rellenas desde su casa, de a poco y
              con mucho amor.
            </p>
            <p>
              Hoy, Rellenitas sigue creciendo gracias al apoyo de cada persona que
              nos elige.
            </p>
          </div>
        </section>

        <section className="section reverse">
          <img
            src="/src/Nena.jpg"
            className="section-image"
          />
          <div className="section-text">
            <h2>Un poco de Rellenitas</h2>
            <p>
              En Rellenitas elaboramos galletas caseras con ingredientes de
              primera calidad, pensadas para que todos las disfruten.
            </p>
            <p>
              Contamos con una gran variedad de sabores: galletas rellenas con
              Nutella, pasta de mani, mermelada o crema de Oreo.
            </p>
            <p>
              Galletas sin relleno, pero con deliciosos sabores: vainilla,
              chocolate, frutas, Oreo o avena.
            </p>
          </div>
        </section>
      </main>

      <footer className="home-footer">
        <p>© 2025 Rellenitas - Las mejores galletitas</p>
      </footer>
    </div>
  );
}
