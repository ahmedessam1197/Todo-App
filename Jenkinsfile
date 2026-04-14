pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "ahmed277/todo-app"
        DOCKER_TAG = "latest"
    }

    stages {

        stage('Checkout') {
            steps {
                git url: 'https://github.com/ahmedessam1197/Todo-App.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t $DOCKER_IMAGE:$DOCKER_TAG ./Docker"
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push ahmed277/todo-app:latest
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh "kubectl apply -f Kubernetes/"
            }
        }
    }

    post {
        success {
            echo "Pipeline SUCCESS"
        }
        failure {
            echo "Pipeline FAILED"
        }
    }
}
