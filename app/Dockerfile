
FROM python:3.12-slim

# Directorio de trabajo inicial
WORKDIR /app

# Instalar dependencias
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copiar toda la aplicación modular
COPY . /app/

# Ejecutar desde el directorio padre del paquete app
WORKDIR /

EXPOSE 5000

# Iniciar Flask mediante Application Factory
CMD ["python", "-c", "from app import create_app; create_app().run(host='0.0.0.0', port=5000)"]
