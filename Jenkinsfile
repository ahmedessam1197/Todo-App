pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'ahmed277/todo-app:latest'
    }
    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }
        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', passwordVariable: 'PASS', usernameVariable: 'USER')]) {
                    sh "echo $PASS | docker login -u $USER --password-stdin"
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                // بناء صورة Docker
                sh 'docker build -t $DOCKER_IMAGE ./Docker'
            }
        }
        stage('Push Docker Image') {
            steps {
                sh 'docker push $DOCKER_IMAGE'
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                withCredentials([file(credentialsId: 'kubeconfig', variable: 'KUBECONFIG')]) {
                    sh 'kubectl apply -f Kubernetes/'
                }
            }
        }
    }
    post {
        always {
            sh 'docker logout'
        }
    }
}
