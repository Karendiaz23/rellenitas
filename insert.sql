# -----------------------
# 1. Insertar Categorías
# -----------------------
categorias = [
    (1, "Vainilla"),
    (2, "Chocolate"),
    (3, "Avena"),
    (4, "Oreo"),
    (5, "Fruta")
]

# Ejecutamos la inserción de categorías
cursor.executemany("INSERT INTO Categorias (CategoriaID, Gusto) VALUES (%s, %s)", categorias)

# -----------------------
# 2. Insertar Galletitas
# -----------------------
galletitas = [
    (1, "Nutella", 2000),
    (2, "Bon o Bon", 2000),
    (3, "Sin relleno", 1500),
    (4, "Crema Oreo", 2000),
    (5, "Mermelada", 1500)
]

# Ejecutamos la inserción de galletitas
cursor.executemany("INSERT INTO Galletitas (GalletitasID, Relleno, Precio) VALUES (%s, %s, %s)", galletitas)

# -----------------------
# 3. Insertar Sabores (relación)
# -----------------------
sabores = [
    (1, 1, 1),
    (2, 1, 2),
    (3, 1, 3),
    (4, 1, 4),
    (5, 1, 5),
    (6, 2, 1),
    (7, 2, 2),
    (8, 2, 3),
    (9, 2, 4),
    (10, 2, 5),
    (11, 3, 1),
    (12, 3, 2),
    (13, 3, 3),
    (14, 4, 2),
    (15, 4, 3),
    (16, 4, 4),
    (17, 5, 3),
    (18, 5, 5)
]

# Ejecutamos la inserción de sabores
cursor.executemany("INSERT INTO Sabores (SaboresID, CategoriaID, GalletitasID) VALUES (%s, %s, %s)", sabores)

# Guardamos los cambios en la base de datos
conexion.commit()

# -----------------------
# 4. Consultar datos
# -----------------------
cursor.execute("""
    SELECT s.SaboresID, c.Gusto, g.Relleno, g.Precio
    FROM Sabores s
    JOIN Categorias c ON s.CategoriaID = c.CategoriaID
    JOIN Galletitas g ON s.GalletitasID = g.GalletitasID
""")

# Obtenemos todos los resultados
resultados = cursor.fetchall()

# Mostramos cada fila en consola
for fila in resultados:
    print(fila)

# Cerramos el cursor y la conexión
cursor.close()
conexion.close()
