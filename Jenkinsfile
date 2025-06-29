pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/dhanyasn14/python-ci-cd-example.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat '"C:\\Users\\charu\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" -m venv venv'
                bat '.\\venv\\Scripts\\pip install -r requirements.txt || exit 0'
            }
        }

        stage('Run Tests') {
            steps {
                bat '.\\venv\\Scripts\\python -m unittest test_app.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploy placeholder'
            }
        }
    }
}
