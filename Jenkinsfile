pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/karrasathwik/lakehouse.git'
            }
        }

        stage('Deploy Extract Notebook') {
            steps {
                bat 'databricks workspace import extract.ipynb /Repos/lakehouse/extract.ipynb -o'
            }
        }

        stage('Deploy Silver Notebook') {
            steps {
                bat 'databricks workspace import silver.ipynb /Repos/lakehouse/silver.ipynb -o'
            }
        }

        stage('Deploy Gold Notebook') {
            steps {
                bat 'databricks workspace import gold.ipynb /Repos/lakehouse/gold.ipynb -o'
            }
        }
    }

    post {
        success { echo 'Notebooks deployed successfully!' }
        failure { echo 'Deployment failed!' }
    }
}