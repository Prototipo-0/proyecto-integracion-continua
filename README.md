@"
# Proyecto de Integración Continua

## Descripción

Aplicación web desarrollada con Python y Flask, conectada a una base de datos PostgreSQL. Los servicios se ejecutan mediante contenedores Docker y se administran con Docker Compose.

## Tecnologías utilizadas

- Python 3.12
- Flask
- PostgreSQL 16
- Docker
- Docker Compose
- Git

## Estructura del proyecto

\`\`\`text
proyecto-integracion-continua/
│
├── app/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── database/
│   └── init.sql
│
├── .env
├── .gitignore
├── docker-compose.yml
└── README.md
\`\`\`

## Requisitos

- Docker Desktop
- Docker Compose
- Git

## Ejecución del proyecto

Construir e iniciar los servicios:

\`\`\`bash
docker compose up -d --build
\`\`\`

Consultar el estado de los contenedores:

\`\`\`bash
docker compose ps
\`\`\`

Detener los servicios:

\`\`\`bash
docker compose down
\`\`\`

## Endpoints

| Ruta | Descripción |
|---|---|
| / | Verifica el funcionamiento de Flask |
| /health | Verifica la conexión con PostgreSQL |

## Puertos

- Flask: 5000
- PostgreSQL: 5432

## Base de datos

PostgreSQL utiliza un volumen persistente denominado postgres_data.

La inicialización de la base de datos se realiza mediante el archivo database/init.sql.

## Seguridad

Las variables de entorno y credenciales se almacenan en el archivo .env, excluido del repositorio mediante .gitignore.
"@ | Set-Content README.md