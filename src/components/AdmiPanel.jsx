import React, { useState } from "react";

export default function AdminPanel() {
  const [formData, setFormData] = useState({
    Relleno: "nutella",
    Precio: "2000",
    imagen_url: "/images/flor.jpeg",
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch("http://localhost:5000/productos", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(formData),
    })
      .then((res) => res.json())
      .then((data) => alert(data.message));
  };

  return (
    <form
      onSubmit={handleSubmit}
      style={{ margin: "20px", textAlign: "center" }}
    >
      <input name="Relleno" placeholder="Nombre" onChange={handleChange} />
      <input
        name="Precio"
        placeholder="Precio"
        type="number"
        onChange={handleChange}
      />
      <input
        name="imagen_url"
        placeholder="URL imagen (ej: /images/cookie.jpg)"
        onChange={handleChange}
      />
      <button type="submit">Agregar Producto</button>
    </form>
  );
}
