pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "ahmed277/todo-app"
        DOCKER_TAG = "latest"
    }

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'ls -la'
                sh 'docker build -t $DOCKER_IMAGE:$DOCKER_TAG ./Dockerfile'
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh 'docker login -u $USER -p $PASS'
                    sh 'docker push $DOCKER_IMAGE:$DOCKER_TAG'
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f Kubernetes/'
            }
        }

    }
}
