pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/dhanyasn14/python-ci-cd-example.git'
            }
        }
        stage('Install Python') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh './venv/bin/python -m unittest test_app.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploy step placeholder (e.g., copy to server, run script, etc.)'
            }
        }
    }
}
