
-- ==========================================
-- IT SERVICE DESK
-- Datos iniciales del sistema
-- ==========================================

-- ROLES

INSERT INTO roles (nombre, descripcion)
VALUES
    ('Administrador', 'Acceso completo al sistema'),
    ('Tecnico', 'Gestion y atencion de incidencias'),
    ('Solicitante', 'Creacion y consulta de incidencias')
ON CONFLICT (nombre) DO NOTHING;


-- CATEGORIAS

INSERT INTO categorias (nombre, descripcion)
VALUES
    ('Hardware', 'Equipos y componentes fisicos'),
    ('Software', 'Aplicaciones y sistemas operativos'),
    ('Redes', 'Conectividad y comunicaciones'),
    ('Accesos', 'Usuarios, contrasenas y permisos'),
    ('Telefonia', 'Telefonia IP y comunicaciones'),
    ('Otros', 'Otras solicitudes de soporte')
ON CONFLICT (nombre) DO NOTHING;


-- PRIORIDADES

INSERT INTO prioridades (nombre, nivel)
VALUES
    ('Critica', 1),
    ('Alta', 2),
    ('Media', 3),
    ('Baja', 4)
ON CONFLICT (nombre) DO NOTHING;


-- ESTADOS

INSERT INTO estados (nombre)
VALUES
    ('Abierta'),
    ('Asignada'),
    ('En progreso'),
    ('Pendiente'),
    ('Resuelta'),
    ('Cerrada')
ON CONFLICT (nombre) DO NOTHING;
