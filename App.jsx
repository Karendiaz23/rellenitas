import React from "react";
import AdminPanel from "./components/AdminPanel";
import Producto from "./components/Producto";

function App() {
  return (
    <div>
      <h1 style={{ textAlign: "center" }}>Rellenitas</h1>
      <AdminPanel />
      <Producto />
    </div>
  );
}

export default App;
