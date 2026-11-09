CREATE TABLE IF NOT EXISTS pruebas (
    id SERIAL PRIMARY KEY,
    descripcion VARCHAR(255) NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO pruebas (descripcion)
VALUES ('Base de datos inicializada correctamente');
