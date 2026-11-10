@"
# Proyecto de Integración Continua

## Descripción

Aplicación web desarrollada con Python y Flask para la gestión de incidencias de soporte tecnológico. Está conectada a una base de datos PostgreSQL y utiliza contenedores Docker para ejecutar y administrar sus servicios mediante Docker Compose.

## Tecnologías utilizadas
- Python 3.12
- Flask
- PostgreSQL 16
- Docker
- Docker Compose
- Git y GitHub
- GitHub Actions

## Estructura del proyecto

\`\`\`text
Aplicación web desarrollada con Python y Flask para la gestión de incidencias de soporte tecnológico. Está conectada a una base de datos PostgreSQL y utiliza contenedores Docker para ejecutar y administrar sus servicios mediante Docker Compose.

Tecnologías utilizadas

Python 3.12

Flask

PostgreSQL 16

Docker

Docker Compose

Git y GitHub

GitHub Actions

Estructura del proyecto

proyecto-integracion-continua/
│
├── .github/
│   └── workflows/
│       └── docker-build.yml
│
├── app/
│   ├── auth/
│   ├── dashboard/
│   ├── incidents/
│   ├── users/
│   ├── categories/
│   ├── services/
│   ├── templates/
│   ├── static/
│   ├── __init__.py
│   ├── app.py
│   ├── config.py
│   ├── extensions.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── database/
│   ├── init.sql
│   ├── schema.sql
│   └── seed.sql
│
├── .dockerignore
├── .env.example
├── .gitignore
├── docker-compose.yml
└── README.md
\`\`\`

## Requisitos

- Docker Desktop
- Docker Compose
- Git

## Configuración inicial

Clonar el repositorio: 

\`\`\`bash
git clone https://github.com/Prototipo-0/proyecto-integracion-continua.git
\`\`\`

Ingresar a la carpeta: 

\`\`\`bash
cd proyecto-integracion-continua
\`\`\`

Crear el archivo local de variables de entorno a partir de la plantilla: 

\`\`\`bash
Copy-Item .env.example .env
\`\`\`

Editar el archivo .env con los valores correspondientes al entorno local.

## Ejecución del proyecto

Construir las imágenes e iniciar los servicios:

Construir e iniciar los servicios:

\`\`\`bash
docker compose up -d --build
\`\`\`

Consultar el estado de los contenedores:

\`\`\`bash
docker compose ps
\`\`\`

Consultar los registros de ejecución:

\`\`\`bash
docker compose logs
\`\`\`

Detener los servicios:

\`\`\`bash
docker compose down
\`\`\`

## Acceso a la aplicación

La aplicación web Flask está disponible en: http://localhost:5000

La base de datos PostgreSQL utiliza el puerto 5432 y se comunica con Flask mediante el nombre del servicio db dentro de la red Docker red_proyecto.

## Persistencia de datos

PostgreSQL utiliza un volumen Docker denominado postgres_data, que permite conservar la información almacenada cuando los contenedores se detienen o se recrean.

## Red Docker

Los servicios app y db se encuentran conectados a una red personalizada denominada red_proyecto, configurada mediante el controlador bridge.

## Integración continua

El proyecto utiliza GitHub Actions para automatizar la construcción de la imagen Docker de la aplicación cuando se realizan cambios mediante eventos push o pull_request.

El flujo de trabajo se encuentra en:

.github/workflows/docker-build.yml

## Seguridad

Las credenciales y variables de entorno locales se almacenan en .env, archivo excluido del repositorio mediante .gitignore.

El archivo .env.example proporciona una plantilla de configuración sin incluir las credenciales reales. También se utiliza .dockerignore para excluir archivos innecesarios durante la construcción de la imagen Docker.
