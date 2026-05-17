CREATE TABLE ventas (
    id SERIAL PRIMARY KEY,
    producto VARCHAR(100),
    cantidad INT,
    precio NUMERIC(10, 2),
    fecha_venta DATE
);
