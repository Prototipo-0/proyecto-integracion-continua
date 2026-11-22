
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
                    echo "Estructura del proyecto validada"
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
            echo 'Pipeline ejecutado correctamente.'
        }
        failure {
            echo 'El Pipeline presentó un error.'
        }
    }
}
