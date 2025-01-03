pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t django-crud-app:latest .'
            }
        }

        stage('Deploy to Staging') {
            steps {
                sh '''
                docker stop django-crud-app || true && docker rm django-crud-app || true
                docker run -d -p 8000:8000 --name django-crud-app django-crud-app:latest
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution complete!'
        }
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Pipeline failed. Please check logs.'
        }
    }
}
