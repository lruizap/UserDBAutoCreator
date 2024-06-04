import sqlite3
from faker import Faker
import random

# Crear una instancia de Faker
fake = Faker()

# Conectar a la base de datos SQLite (se creará si no existe)
conn = sqlite3.connect('usuarios.db')
c = conn.cursor()

# Crear la tabla de usuarios
c.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        correo TEXT,
        direccion TEXT,
        fecha_nacimiento TEXT
    )
''')

# Crear la tabla de productos
c.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        descripcion TEXT,
        precio REAL
    )
''')

# Crear la tabla de pedidos
c.execute('''
    CREATE TABLE IF NOT EXISTS pedidos (
        id INTEGER PRIMARY KEY,
        usuario_id INTEGER,
        producto_id INTEGER,
        cantidad INTEGER,
        fecha_pedido TEXT,
        FOREIGN KEY(usuario_id) REFERENCES usuarios(id),
        FOREIGN KEY(producto_id) REFERENCES productos(id)
    )
''')

# Generar y añadir 100 registros de usuarios
for i in range(1, 101):
    nombre = fake.name()
    correo = fake.email()
    direccion = fake.address().replace('\n', ', ')
    fecha_nacimiento = fake.date_of_birth().isoformat()

    c.execute('''
        INSERT INTO usuarios (id, nombre, correo, direccion, fecha_nacimiento) 
        VALUES (?, ?, ?, ?, ?)
    ''', (i, nombre, correo, direccion, fecha_nacimiento))

# Generar y añadir 50 registros de productos
for i in range(1, 51):
    nombre = fake.word().capitalize()
    descripcion = fake.text()
    precio = round(random.uniform(10.0, 100.0), 2)

    c.execute('''
        INSERT INTO productos (id, nombre, descripcion, precio) 
        VALUES (?, ?, ?, ?)
    ''', (i, nombre, descripcion, precio))

# Generar y añadir 100 registros de pedidos
for i in range(1, 101):
    usuario_id = random.randint(1, 100)
    producto_id = random.randint(1, 50)
    cantidad = random.randint(1, 10)
    fecha_pedido = fake.date_this_year().isoformat()

    c.execute('''
        INSERT INTO pedidos (id, usuario_id, producto_id, cantidad, fecha_pedido) 
        VALUES (?, ?, ?, ?, ?)
    ''', (i, usuario_id, producto_id, cantidad, fecha_pedido))

# Confirmar los cambios
conn.commit()

# Cerrar la conexión
conn.close()

print("Base de datos y tablas creadas con éxito, y registros añadidos.")
