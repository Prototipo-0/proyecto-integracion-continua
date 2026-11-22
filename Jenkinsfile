
pipeline {
    agent any

    options {
        timestamps()
    }

    stages {
        stage('Verificar Docker') {
            steps {
                sh 'docker version'
            }
        }

        stage('Validar estructura del proyecto') {
            steps {
                sh '''
                    test -f app/Dockerfile
                    test -f app/requirements.txt
                    test -f app/tests/conftest.py
                    echo "Estructura del proyecto validada"
                '''
            }
        }

        stage('Construir imagen de pruebas') {
            steps {
                sh '''
                    docker build \
                        -t proyecto-integracion-continua-test:${BUILD_NUMBER} \
                        ./app
                '''
            }
        }

        stage('Ejecutar pruebas automatizadas') {
            steps {
                sh '''
                    docker run --rm \
                        proyecto-integracion-continua-test:${BUILD_NUMBER} \
                        pytest /app/tests -v
                '''
            }
        }

        stage('Construir imagen Flask') {
            steps {
                sh '''
                    docker build \
                        -t proyecto-integracion-continua-app:${BUILD_NUMBER} \
                        ./app
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline ejecutado correctamente. Todas las pruebas fueron aprobadas.'
        }
        failure {
            echo 'El Pipeline presentó un error.'
        }
    }
}
