pipeline {
    agent any
    stages {
        stage("Cloner Github") {
            steps {
                git branch: "main", url: "https://github.com/WalkerStanislas/Gestion-de-taches-collaboratives.git"
            }
        }
        stage ("Installation des dépendances") {
            steps {
                bat "pip install -r requirements.txt"
            }
        }
        stage ("Execution des tests") {
            steps {
                bat "unittest -v"
            }
        }
    }
}
