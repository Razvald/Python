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
                sh 'pip install -r 11Lab/requirements.txt'
            }
        }
        stage('Run tests') {
            steps {
                sh 'pytest 11Lab/test_math_functions.py --junitxml=11Lab/report.xml'
            }
        }
        stage('Archive Results') {
            steps {
                archiveArtifacts artifacts: '11Lab/report.xml', allowEmptyArchive: true
            }
        }
    }
}
