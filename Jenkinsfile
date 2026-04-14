pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "ahmed277/todo-app"
        DOCKER_TAG = "latest"
    }

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/ahmedessam1197/Todo-App.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE:$DOCKER_TAG .'
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
