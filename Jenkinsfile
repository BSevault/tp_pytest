pipeline {
    agent any
    stages {
        stage('Checkout repository') {
            steps {
                // Clone le dépôt Git
                checkout scm
            }
        }
        // stage('Set up Python') {
        //     steps {
        //         // Installe la version de Python spécifiée
        //         sh 'apt-get update && apt-get install -y python3'
        //     }
        // }
        stage('Install dependencies') {
            steps {
                // Installe les dépendances Python
                sh 'pip install pytest pytest-cov'
            }
        }
        stage('Run unit tests') {
            steps {
                // Exécute les tests unitaires avec couverture de code
                sh 'pytest --cov-report term-missing --cov'
            }
        }
        stage('Display coverage percentage') {
            steps {
                // Affiche le pourcentage de couverture de code
                sh 'coverage report | grep TOTAL'
            }
        }
    }
    post {
        always {
            // Nettoyage après l'exécution de la pipeline
            cleanWs()
        }
    }
}
