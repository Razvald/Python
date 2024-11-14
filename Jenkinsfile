pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Set up Python') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run tests') {
            steps {
                sh 'pytest --junitxml=report.xml'
            }
        }
        stage('Archive Results') {
            steps {
                archiveArtifacts artifacts: 'report.xml', allowEmptyArchive: true
            }
        }
    }
}
