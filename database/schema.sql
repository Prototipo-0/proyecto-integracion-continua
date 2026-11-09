
-- ==========================================
-- IT SERVICE DESK
-- Estructura de la base de datos
-- ==========================================

CREATE TABLE IF NOT EXISTS roles (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) UNIQUE NOT NULL,
    descripcion VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(120) NOT NULL,
    correo VARCHAR(150) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    rol_id INTEGER NOT NULL REFERENCES roles(id),
    activo BOOLEAN DEFAULT TRUE,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS categorias (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) UNIQUE NOT NULL,
    descripcion VARCHAR(255),
    activo BOOLEAN DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS prioridades (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(30) UNIQUE NOT NULL,
    nivel INTEGER UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS estados (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS incidencias (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    descripcion TEXT NOT NULL,
    solicitante_id INTEGER NOT NULL REFERENCES usuarios(id),
    tecnico_id INTEGER REFERENCES usuarios(id),
    categoria_id INTEGER NOT NULL REFERENCES categorias(id),
    prioridad_id INTEGER NOT NULL REFERENCES prioridades(id),
    estado_id INTEGER NOT NULL REFERENCES estados(id),
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_cierre TIMESTAMP
);

CREATE TABLE IF NOT EXISTS historial_incidencias (
    id SERIAL PRIMARY KEY,
    incidencia_id INTEGER NOT NULL REFERENCES incidencias(id),
    usuario_id INTEGER REFERENCES usuarios(id),
    accion VARCHAR(100) NOT NULL,
    detalle TEXT,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índices para optimizar consultas

CREATE INDEX IF NOT EXISTS idx_incidencias_estado
ON incidencias(estado_id);

CREATE INDEX IF NOT EXISTS idx_incidencias_solicitante
ON incidencias(solicitante_id);

CREATE INDEX IF NOT EXISTS idx_incidencias_tecnico
ON incidencias(tecnico_id);

CREATE INDEX IF NOT EXISTS idx_historial_incidencia
ON historial_incidencias(incidencia_id);
