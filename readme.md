# Script de Creación de Base de Datos SQLite

Este proyecto consiste en un script en Python que crea una base de datos SQLite con tres tablas: `usuarios`, `productos` y `pedidos`. Las tablas están relacionadas y se generan datos aleatorios utilizando la librería `Faker`.

## Requisitos

- Python 3.x
- Librería `Faker`

## Instalación

1. Clona este repositorio o descarga el script `create_database.py`.
2. Instala la librería `Faker` si aún no la tienes:

```sh
pip install faker
```

## Uso

Ejecuta el script `create_database.py` para crear la base de datos y las tablas, y para poblarlas con datos aleatorios:

```sh
python create_database.py
```

### Tablas

- **usuarios**

  - `id` (INTEGER, PRIMARY KEY)
  - `nombre` (TEXT)
  - `correo` (TEXT)
  - `direccion` (TEXT)
  - `fecha_nacimiento` (TEXT)

- **productos**

  - `id` (INTEGER, PRIMARY KEY)
  - `nombre` (TEXT)
  - `descripcion` (TEXT)
  - `precio` (REAL)

- **pedidos**
  - `id` (INTEGER, PRIMARY KEY)
  - `usuario_id` (INTEGER, FOREIGN KEY referencia a `usuarios(id)`)
  - `producto_id` (INTEGER, FOREIGN KEY referencia a `productos(id)`)
  - `cantidad` (INTEGER)
  - `fecha_pedido` (TEXT)

### Datos Generados

- **Usuarios**: Se generan 100 usuarios con nombres, correos electrónicos, direcciones y fechas de nacimiento aleatorias.
- **Productos**: Se generan 50 productos con nombres, descripciones y precios aleatorios.
- **Pedidos**: Se generan 100 pedidos con referencias a usuarios y productos, cantidades y fechas de pedido aleatorias.

### Script

El script realiza las siguientes acciones:

1. Conecta a la base de datos SQLite (creando una nueva base de datos llamada `usuarios.db` si no existe).
2. Crea las tablas `usuarios`, `productos` y `pedidos`.
3. Genera y añade 100 registros de usuarios.
4. Genera y añade 50 registros de productos.
5. Genera y añade 100 registros de pedidos.
6. Confirma los cambios y cierra la conexión a la base de datos.

```python
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
```

## Autor

Este script fue creado por lruizap. Siente libre de modificar y mejorar el script según tus necesidades.

Este archivo README proporciona una descripción clara del propósito del script, los requisitos, las instrucciones de instalación y uso, así como una breve explicación de la estructura de la base de datos y el código del script.
