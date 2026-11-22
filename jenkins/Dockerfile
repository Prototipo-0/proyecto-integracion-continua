
# Obtener el cliente Docker desde su imagen oficial
FROM docker:cli AS docker-cli

# Imagen base de Jenkins con Java 21
FROM jenkins/jenkins:lts-jdk21

# Incorporar el ejecutable Docker CLI
USER root

COPY --from=docker-cli /usr/local/bin/docker /usr/local/bin/docker

# Volver al usuario habitual de Jenkins
USER jenkins
